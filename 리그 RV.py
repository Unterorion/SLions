# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 16:37:18 2021

@author: LIONS
"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv", index_col=False, encoding='cp949')
df = df[df['Level'] == 'KBO']

pf = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\파크팩터.csv", index_col=False, encoding='cp949')
pf.set_index('Stadium', inplace=True)
pf.drop(['K'], axis=1, inplace=True)

for i in range(len(df.index)):
    if df['Stadium'].iloc[i] == 'Gwangju':
        if df['pa_result'].iloc[i] == '몸에 맞는 볼':
            df['PitchCall'].iloc[i] = 'HitByPitch'

df = df.assign(PA=np.where(((df.PlayResult!='Undefined')|(df.KorBB!='Undefined')|(df.PitchCall=='HitByPitch'))&((df.PlayResult!='Sacrifice')|((df.HitType!='GroundBall')&(df.HitType!='Bunt'))), 1, 0))

df['Result'] = np.nan

for i in range(len(df.index)):
    if df['PlayResult'].iloc[i] == 'Undefined':
        if df['KorBB'].iloc[i] == 'Strikeout':
            df['Result'].iloc[i] = 'Out'
        elif df['KorBB'].iloc[i] == 'Walk':
            if df['PitchCall'].iloc[i] == 'BallCalled':
                df['Result'].iloc[i] = 'BB'
        elif df['PitchCall'].iloc[i] == 'HitByPitch':
            df['Result'].iloc[i] = 'HBP'
    else:
        df['Result'].iloc[i] = df['PlayResult'].iloc[i]

df.dropna(subset=['Result'], inplace=True)

rv = pd.pivot_table(df, values='RE24_change', index='Result', aggfunc='mean')
rv = rv.transpose()
rrv = pd.DataFrame()

for res in ['BB','HBP','Error','Single','Double','Triple','HomeRun']:
    rrv[res] = rv[res] - rv['Out']

rrv.to_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\리그 아웃 대비 RV.csv", encoding='cp949')