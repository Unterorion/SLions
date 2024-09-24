# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 17:30:12 2021

@author: LIONS
"""

import pandas as pd
import numpy as np
import xgboost as xgb

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
    elif df['PlayResult'].iloc[i] == 'Sacrifice' or df['PlayResult'].iloc[i] == 'FieldersChoice':
        df['Result'].iloc[i] = 'Out'
    else:
        df['Result'].iloc[i] = df['PlayResult'].iloc[i]
    
df.dropna(subset=['Result'], inplace=True)

pf = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\파크팩터.csv", index_col=False, encoding='cp949')
pf.set_index('Stadium', inplace=True)

rv = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\리그 아웃 대비 RV.csv", index_col=False, encoding='cp949')
rv.set_index('Unnamed: 0', inplace=True)

mask = (df['Result']!='K')&(df['Result']!='BB')&(df['Result']!='HBP')
bbe = df[mask]

model = xgb.XGBClassifier()
X = bbe[['ExitSpeed','Angle','Bearing']]
Y = bbe['Result']
model.fit(X, Y)

bbe['Xbase'] = model.predict(bbe[['ExitSpeed', 'Angle', 'Bearing']])
add = bbe[['PitchUID', 'Xbase']]
#%%
df['Xbase'] = np.nan
df.set_index('PitchUID', inplace=True)
for i in range(len(add.index)):
    pid = add['PitchUID'].iloc[i]
    df['Xbase'].loc[pid] = add['Xbase'].iloc[i]

for i in range(len(df.index)):
    if df['Result'].iloc[i] == 'K' or df['Result'].iloc[i] == 'BB' or df['Result'].iloc[i] == 'HBP':
        df['Xbase'].iloc[i] = df['Result'].iloc[i]
#%%
df['RE+'] = 0

for i in range(len(df.index)):
    res = df['Xbase'].iloc[i]
    
    if res in ['BB', 'HBP', 'Error', 'Single', 'Double', 'Triple', 'HomeRun']:
        df['RE+'].iloc[i] = rv[res].loc['RE24_change']

df = df.assign(OBP=np.where((df.Result=='BB')|(df.Result=='HBP')|(df.Result=='Single')|(df.Result=='Double')|(df.Result=='Triple')|(df.Result=='HomeRun'), 1, 0))

lgOBP = df['OBP'].mean()
lgREPA = df['RE+'].sum()/df['PA'].sum()

pt = pd.pivot_table(df, index=['kbo_bid','BatName1'], values=['PA','RE+'], aggfunc='sum')

pt['wOBA+'] = (pt['RE+']/pt['PA']) * (lgOBP/lgREPA)

pt.to_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\파크팩터 보정 wOBA(모델링 기반).csv", encoding='cp949')