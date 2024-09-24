# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 15:40:43 2021

@author: LIONS
"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv", index_col=False, encoding='cp949')
df = df[df['Level'] == 'KBO']

for i in range(len(df.index)):
    if df['Stadium'].iloc[i] == 'Gwangju':
        if df['pa_result'].iloc[i] == '몸에 맞는 볼':
            df['PitchCall'].iloc[i] = 'HitByPitch'

df = df.assign(PA=np.where(((df.PlayResult!='Undefined')|(df.KorBB!='Undefined')|(df.PitchCall=='HitByPitch'))&((df.PlayResult!='Sacrifice')|((df.HitType!='GroundBall')&(df.HitType!='Bunt'))), 1, 0))
df = df[df['PA']==1]

df['Result'] = np.nan

for i in range(len(df.index)):
    if df['PlayResult'].iloc[i] == 'Undefined':
        if df['KorBB'].iloc[i] == 'Strikeout':
            df['Result'].iloc[i] = 'K'
        elif df['KorBB'].iloc[i] == 'Walk':
            if df['PitchCall'].iloc[i] == 'BallCalled':
                df['Result'].iloc[i] = 'BB'
        elif df['PitchCall'].iloc[i] == 'HitByPitch':
            df['Result'].iloc[i] = 'HBP'
    else:
        df['Result'].iloc[i] = df['PlayResult'].iloc[i]
    
df.dropna(subset=['Result'], inplace=True)

pf = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\파크팩터(3년).csv", index_col=False, encoding='cp949')
pf.set_index('Stadium', inplace=True)

rv = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\리그 아웃 대비 RV.csv", index_col=False, encoding='cp949')
rv.set_index('Unnamed: 0', inplace=True)

df['PA+'] = 1
df['RE+'] = 0

for i in range(len(df.index)):
    venue = df['Stadium'].iloc[i]
    res = df['Result'].iloc[i]
    
    if res in ['K', 'BB', 'HBP']:
        df['PA+'].iloc[i] = 1/pf[res].loc[venue]
    
    if res in ['BB', 'HBP']:
        df['RE+'].iloc[i] = rv[res].loc['RE24_change']
    elif res in ['Error', 'Single', 'Double', 'Triple', 'HomeRun']:
        df['RE+'].iloc[i] = rv[res].loc['RE24_change']/pf[res].loc[venue]

df = df.assign(OBP=np.where((df.Result=='BB')|(df.Result=='HBP')|(df.Result=='Single')|(df.Result=='Double')|(df.Result=='Triple')|(df.Result=='HomeRun'), 1, 0))

lgOBP = df['OBP'].mean()
lgREPA = df['RE+'].sum()/df['PA+'].sum()

pt = pd.pivot_table(df, index=['kbo_bid','BatName1'], values=['PA+','RE+'], aggfunc='sum')

wOBA_scale = lgOBP/lgREPA

pt['wOBA+'] = (pt['RE+']/pt['PA+']) * wOBA_scale

pt.to_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\파크팩터 보정 wOBA(타석 당 수치 기반 - 3년) ver2.csv", encoding='cp949')