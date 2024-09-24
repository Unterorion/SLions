# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 13:57:45 2021

@author: LIONS
"""

import pandas as pd
import xgboost as xgb
import numpy as np

df = pd.read_csv("C:\\Users\\kimyj\\OneDrive\\바탕 화면\\2021KBOwithFutures.csv", index_col=False, encoding='cp949')
df.dropna(subset=['RelSpeed'], inplace=True)
df = df[df.Level == 'KBO']

df = df.assign(PA=np.where((df.PlayResult!='Undefined') | (df.KorBB!='Undefined') | (df.PitchCall=='HitByPitch'), 1, 0))
df = df[df['PA'] == 1]
df = df.assign(Walk=np.where((df.KorBB=='Walk')|(df.PitchCall=='HitByPitch'), 1, 0))

dfAB = df[(df['PitchCall']!='HitByPitch') & (df['KorBB']!='Walk')]

def Hit(PlayResult):
    if PlayResult in ['Single','Double', 'Triple', 'HomeRun']:
        return 1
    else:
        return 0

def TB(PlayResult):
    if PlayResult == 'Single':
        return 1
    elif PlayResult == 'Double':
        return 2
    elif PlayResult == 'Triple':
        return 3
    elif PlayResult == 'HomeRun':
        return 4
    else:
        return 0


maskBBE = (df.PitchCall=='InPlay') & ((df.PlayResult!='Sacrifice')|((df.PlayResult=='Sacrifice')&(df.HitType!='Undefined')&(df.HitType!='Bunt')))
dfBBE = df[maskBBE]

dfBBE['BA'] = dfBBE['PlayResult'].apply(Hit)
dfBBE['SLG'] = dfBBE['PlayResult'].apply(TB)

#X = dfBBE[['ExitSpeed', 'Angle', 'Bearing']]
X = dfBBE[['ExitSpeed', 'Angle']] # 배럴은 Bearing이랑 무관하기 때문에 속도랑 발사각만
Y = dfBBE['BA']
Z = dfBBE['SLG']

xBA_model = xgb.XGBRegressor()
xSLG_model = xgb.XGBRegressor()

xBA_model.fit(X, Y)
xSLG_model.fit(X, Z)

dfBBE['xBA'] = xBA_model.predict(dfBBE[['ExitSpeed', 'Angle']])
dfBBE['xSLG'] = xSLG_model.predict(dfBBE[['ExitSpeed', 'Angle']])

dfBBE = dfBBE.assign(BarrelRate=np.where((dfBBE.xBA>0.5)&(dfBBE.xSLG>1.5), 1, 0))

dfAB = pd.merge(dfAB, dfBBE[['PitchUID','BA','SLG','xBA','xSLG']], how='outer', on=['PitchUID'])
dfAB['BA'].fillna(0, inplace=True)
dfAB['SLG'].fillna(0, inplace=True)
dfAB['xBA'].fillna(0, inplace=True)
dfAB['xSLG'].fillna(0, inplace=True)
dfAB.rename(columns={'PA':'AB'}, inplace=True)

df = pd.merge(df, dfAB[['PitchUID','BA','SLG','xBA']], how='outer', on=['PitchUID'])
df['BA'].fillna(0, inplace=True)
df['SLG'].fillna(0, inplace=True)
df['xBA'].fillna(0, inplace=True)
df['OBP'] = df['Walk'] + df['BA']
df['xOBP'] = df['Walk'] + df['xBA']

pa = pd.pivot_table(df, index=['kbo_bid', 'BatName1'], values='PA', aggfunc='sum')
ab = pd.pivot_table(dfAB, index=['kbo_bid', 'BatName1'], values='AB', aggfunc='sum')

pt1 = pd.pivot_table(dfAB, index=['kbo_bid', 'BatName1'], values=['BA', 'xBA'], aggfunc='mean')
pt2 = pd.pivot_table(df, index=['kbo_bid', 'BatName1'], values=['OBP', 'xOBP'], aggfunc='mean')
pt3 = pd.pivot_table(dfAB, index=['kbo_bid', 'BatName1'], values=['SLG', 'xSLG'], aggfunc='mean')
pt = pd.concat([pa, ab, pt1, pt2, pt3], axis=1)

pt['OPS'] = pt['OBP'] + pt['SLG']
pt['xOPS'] = pt['xOBP'] + pt['xSLG']
pt['xOPS-OPS'] = pt['xOPS'] - pt['OPS']

pt4 = pd.pivot_table(dfBBE, index=['kbo_bid', 'BatName1'], values=['BarrelRate'], aggfunc='mean')
pt = pd.concat([pt, pt4], axis=1)

pt.to_csv("C:\\Users\\kimyj\\OneDrive\\바탕 화면\\기대타격스탯(new).csv", encoding='cp949')