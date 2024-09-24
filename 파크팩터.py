# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 15:36:33 2021

@author: LIONS
"""

import pandas as pd
import numpy as np

df19 = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2019.csv", index_col=False, encoding='cp949')
df20 = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2020.csv", index_col=False, encoding='cp949')
df21 = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv", index_col=False, encoding='cp949')
df = pd.concat([df19,df20,df21], axis=0)

df = df[df['Level'] == 'KBO']

for i in range(len(df.index)):
    if df['Stadium'].iloc[i] == 'Gwangju':
        if df['pa_result'].iloc[i] == '몸에 맞는 볼':
            df['PitchCall'].iloc[i] = 'HitByPitch'

df = df.assign(PA=np.where(((df.PlayResult!='Undefined')|(df.KorBB!='Undefined')|(df.PitchCall=='HitByPitch'))&((df.PlayResult!='Sacrifice')|((df.HitType!='GroundBall')&(df.HitType!='Bunt'))), 1, 0))
df = df[df['PA'] == 1]

df = df.assign(PA=np.where((df.PlayResult!='Undefined') | (df.KorBB!='Undefined') | (df.PitchCall=='HitByPitch'), 1, 0))

df = df.assign(BB=np.where((df['KorBB']=='Walk')&(df['PitchCall']!='BallIntentional'), 1, 0))
df = df.assign(K=np.where(df['KorBB']=='Strikeout', 1, 0))
df = df.assign(HBP=np.where(df['PitchCall']=='HitByPitch', 1, 0))

pfb = pd.pivot_table(df, index='BatterTeam', columns='Stadium', values='BB', aggfunc='mean')
pfk = pd.pivot_table(df, index='BatterTeam', columns='Stadium', values='K', aggfunc='mean')
pfh = pd.pivot_table(df, index='BatterTeam', columns='Stadium', values='HBP', aggfunc='mean')

pfb.loc['Average'] = pfb.mean()
pfk.loc['Average'] = pfk.mean()
pfh.loc['Average'] = pfh.mean()

pfk.loc['K'] = pfk.loc['Average']/pfk.loc['Average'].mean()
pfb.loc['BB'] = pfb.loc['Average']/pfb.loc['Average'].mean()
pfh.loc['HBP'] = pfh.loc['Average']/pfh.loc['Average'].mean()

mask = (df['PlayResult']=='Out')|(df['PlayResult']=='Error')|(df['PlayResult']=='Single')|(df['PlayResult']=='Double')|(df['PlayResult']=='Triple')|(df['PlayResult']=='HomeRun')|((df['PlayResult']=='Sacrifice')&(df['HitType']!='GroundBall')&(df['HitType']!='Bunt'))
df = df[mask]

stats = ['Error', 'Single', 'Double', 'Triple', 'HomeRun']

concatlist = []

for stat in stats:
    temp = df.assign(Stat=np.where(df['PlayResult']==stat, 1, 0))
    pt = pd.pivot_table(temp, index='BatterTeam', columns='Stadium', aggfunc='mean', values='Stat')
    
    pt.loc['Average'] = pt.mean()
    meanmean = pt.loc['Average'].mean()
    pt.loc[stat] = pt.loc['Average']/meanmean
    
    pfrow = pd.DataFrame(pt.loc[stat])
    concatlist.append(pfrow)

pf = pd.concat(concatlist, axis=1)

pf = pd.concat([pf, pfb.loc['BB'], pfk.loc['K'], pfh.loc['HBP']], axis=1)
pf.to_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\파크팩터(3년).csv", encoding='cp949')