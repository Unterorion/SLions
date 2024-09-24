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

df = pd.merge(df, dfBBE[['PitchUID','Hit','TB','xBA','xSLG']], how='outer', on=['PitchUID'])

for ID in IDlist:
    df_indi = df[df.kbo_bid == ID]
    name = BatIDstat.BatName1.loc[ID]
    maskBBEindi = (df_indi.PitchCall=='InPlay') & ((df_indi.PlayResult!='Sacrifice')|((df_indi.PlayResult=='Sacrifice')&(df_indi.HitType!='Undefined')&(df_indi.HitType!='Bunt')))
    df_indiBBE = df_indi[maskBBEindi]
    
    Kmask = (df_indi.KorBB == 'Strikeout')
    df_indiK = df_indi[Kmask]
    K = len(df_indiK.index)
    
    Hl = df_indiBBE.Hit.tolist()
    TBl = df_indiBBE.TB.tolist()
    AB = K + len(Hl)
    BA = sum(Hl)/AB
    SLG = sum(TBl)/AB
    
    xBA_list = df_indiBBE.xBA.tolist()
    xSLG_list = df_indiBBE.xSLG.tolist()
    xBA = sum(xBA_list)/AB
    xSLG = sum(xSLG_list)/AB
    
    maskBR = (df_indiBBE.xBA > 0.5) & (df_indiBBE.xSLG > 1.5)
    df_indiBR = df_indiBBE[maskBR]
    if len(df_indiBBE.index) > 0:
        BRR = 100*len(df_indiBR.index)/len(df_indiBBE.index)
    else:
        BRR = None
    
    maskPA_AB = (df_indi.PitchCall == 'HitByPitch') | (df_indi.PitchCall == 'BallIntentional') | (df_indi.KorBB == 'Walk') | (df_indi.PitchCall == 'CatchersInterference') | (df_indi.PlayResult=='Sacrifice')
    dfPA_AB = df_indi[maskPA_AB]
    maskWalk = (df_indi.PitchCall == 'HitByPitch') | (df_indi.PitchCall == 'BallIntentional') | (df_indi.KorBB == 'Walk') | (df_indi.PitchCall == 'CatchersInterference')
    dfWalk = df_indi[maskWalk]
    maskSBunt = (df_indi.PlayResult=='Sacrifice') & ((df_indi.HitType=='Bunt')|(df_indi.HitType=='GroundBall'))
    dfSBunt = df_indi[maskSBunt]
    
    PA_AB = len(dfPA_AB.index)
    walk = len(dfWalk.index)
    SBunt = len(dfSBunt)
    PA = AB + PA_AB
    OBP = (sum(Hl) + walk)/(PA - SBunt)
    xOBP = (sum(xBA_list) + walk)/(PA - SBunt)
    
    OPS = OBP + SLG
    xOPS = xOBP + xSLG
    
    print("\n" + name)
    print("BA/OBP/SLG/OPS = %.3f, %.3f, %.3f, %.3f" % (BA, OBP, SLG, OPS))
    print("xBA/xOBP/xSLG/xOPS = %.3f, %.3f, %.3f, %.3f" % (xBA, xOBP, xSLG, xOPS))
    if type(BRR) == float:
        print("Barrel rate = %.1f\n" % BRR)
    
    BatIDstat['PlateAppearance'].loc[ID] = PA
    BatIDstat['AtBat'].loc[ID] = AB
    BatIDstat['BA'].loc[ID] = BA
    BatIDstat['xBA'].loc[ID] = xBA
    BatIDstat['OBP'].loc[ID] = OBP
    BatIDstat['xOBP'].loc[ID] = xOBP
    BatIDstat['SLG'].loc[ID] = SLG
    BatIDstat['xSLG'].loc[ID] = xSLG
    BatIDstat['OPS'].loc[ID] = OPS
    BatIDstat['xOPS'].loc[ID] = xOPS
    BatIDstat['xOPS-OPS'].loc[ID] = xOPS - OPS
    BatIDstat['BarrelRate'].loc[ID] = BRR
    
BatIDstat.to_csv("C:\\Users\\LIONS\\.spyder-py3\\기대타격스탯.csv", encoding='cp949')