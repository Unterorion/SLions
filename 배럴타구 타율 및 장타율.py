# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 13:57:45 2021

@author: LIONS
"""

import pandas as pd
import xgboost as xgb

df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv", index_col=False, encoding='cp949')
df.dropna(subset=['RelSpeed'], inplace=True)
df = df[df.Level == 'KBO']

BatIDstat = df[['kbo_bid', 'BatName1', 'BatterTeam']]
BatIDstat.drop_duplicates(subset=['kbo_bid'], inplace=True)
BatIDstat.set_index('kbo_bid', inplace=True)
IDlist = BatIDstat.index.tolist()

BatIDstat[['PlateAppearance','AtBat','BA','OBP','SLG','OPS','xBA','xOBP','xSLG','xOPS','xOPS-OPS','BarrelRate']] = None

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

dfBBE['Hit'] = dfBBE['PlayResult'].apply(Hit)
dfBBE['TB'] = dfBBE['PlayResult'].apply(TB)
dfBBE = dfBBE.dropna(subset = ['Hit'])

#X = dfBBE[['ExitSpeed', 'Angle', 'Bearing']]
X = dfBBE[['ExitSpeed', 'Angle']] # 배럴은 Bearing이랑 무관하기 때문에 속도랑 발사각만
Y = dfBBE['Hit']
Z = dfBBE['TB']

xBA_model = xgb.XGBRegressor()
xSLG_model = xgb.XGBRegressor()

xBA_model.fit(X, Y)
xSLG_model.fit(X, Z)

dfBBE['xBA'] = xBA_model.predict(dfBBE[['ExitSpeed', 'Angle']])
dfBBE['xSLG'] = xSLG_model.predict(dfBBE[['ExitSpeed', 'Angle']])

brls = dfBBE[(dfBBE.xBA>0.5) & (dfBBE.xSLG>1.5)]
brBA = brls.xBA.mean()
brSLG = brls.xSLG.mean()
print("BA of barrels = %.3f" % brBA)
print("SLG of barrels = %.3f" % brSLG)

ES = float(input("Exit speed : "))
LA = float(input("Launch angle : "))
temp = pd.DataFrame([[ES, LA]], columns=['ExitSpeed', 'Angle'])
xBA = xBA_model.predict(temp)
xSLG = xSLG_model.predict(temp)
print("xBA = %.3f, xSLG = %.3f" % (xBA, xSLG))