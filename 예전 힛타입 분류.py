# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 20:52:35 2021

@author: LIONS
"""

import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv", index_col=False, encoding='cp949')
df = df[df['Level'] == 'KBO']
idmap = df[['kbo_pid', 'PitName1']].drop_duplicates(subset=['kbo_pid'])

#df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2020.csv", index_col=False, encoding='cp949')
df = df.assign(PA=np.where(((df.PlayResult!='Undefined')|(df.KorBB!='Undefined')|(df.PitchCall=='HitByPitch'))&((df.PlayResult!='Sacrifice')|((df.HitType!='GroundBall')&(df.HitType!='Bunt'))), 1, 0))
df = df[df['PA'] == 1]

df = df.assign(Out = np.where((df.PlayResult=='Out')|(df.KorBB=='Strikeout'), 1, 0))
pt1 = pd.pivot_table(df, index='kbo_pid', values='Out', aggfunc='sum')

bip = df[df['PitchCall']=='InPlay']
bip.dropna(subset=['Angle'], inplace=True)
bip = bip.assign(GBrate=np.where(bip.Angle<8, 1, 0))
bip = bip.assign(FBrate=np.where(bip.Angle>15, 1, 0))
bip = bip.assign(LDrate=np.where((bip.Angle>8)&(bip.Angle<15), 1, 0))

pt2 = pd.pivot_table(bip, index='kbo_pid', values=['GBrate','LDrate','FBrate'], aggfunc='mean')
#%%
pt = pd.concat([pt1, pt2], axis=1)
pt = pt.join(idmap.set_index('kbo_pid')['PitName1'], on='kbo_pid')
#%%
pt.dropna(subset=['PitName1'], inplace=True)
pt.to_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\2021hittype.csv", encoding='cp949')