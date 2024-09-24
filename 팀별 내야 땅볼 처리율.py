# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 19:20:00 2021

@author: LIONS
"""

import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', index_col=False, encoding='cp949')
TeamList = ['KIW_HER', 'KT_WIZ', 'KIA_TIG', 'DOO_BEA', 'NC_DIN', 'LOT_GIA', 'SSG_LAN', 'HAN_EAG', 'LG_TWI', 'SAM_LIO']

df['Bearing'].replace('', np.nan, inplace=True)
df.dropna(subset=['Bearing'], inplace=True)

HitList = []
OutList = []
PercList = []
TotalHitNum = 0
TotalOutNum = 0

for team in TeamList:
    mask = (df.BatterSide == 'Right') & (df.PlayResult != 'Sacrifice') & (df.PitchCall != 'FoulBall') & (df.HitType == 'GroundBall') & (df.Bearing > -45) & (df.Bearing < 45) & (df.PitcherTeam == team)
    df1 = df[mask]
    
    mask2 = (df1.PlayResult == 'Out')
    df2 = df1[mask2]
    
    HitNum = len(df1.index)
    OutNum = len(df2.index)
    OutPerc = 100*OutNum/HitNum
    print(team + " : Total groundball = %d, total out = %d, fielding percentage = %.1f%%" % (HitNum, OutNum, OutPerc))
    
    HitList.append(HitNum)
    OutList.append(OutNum)
    PercList.append(OutPerc)
    TotalHitNum += HitNum
    TotalOutNum += OutNum

AveOutPerc = 100*TotalOutNum/TotalHitNum
print("League total groundball = %d, league total out = %d, league average fielding percentage = %.1f%%" % (TotalHitNum, TotalOutNum, AveOutPerc))

HitList.append(TotalHitNum)
OutList.append(TotalOutNum)
PercList.append(AveOutPerc)

DictData = {'Groundball' : HitList, 'Out' : OutList, 'Fielding percentage' : PercList}
Result = pd.DataFrame(DictData, index = TeamList + ['League total'])

Result.to_csv("C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\2021 팀별 우타자 내야 땅볼 처리율.csv")

#%% 8도 아래 및 땅볼 분류된 것들 비율 비교

df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', index_col=False, encoding='cp949')
df['Angle'].replace('', np.nan, inplace=True)
df.dropna(subset=['Angle'], inplace=True)

mask1 = (df.PlayResult != 'Sacrifice') & (df.PitchCall != 'FoulBall') & (df.Angle <= 8) & (df.Bearing > -45) & (df.Bearing < 45)
mask2 = (df.PlayResult != 'Sacrifice') & (df.HitType == 'GroundBall') & (df.PitchCall != 'FoulBall') & (df.Bearing > -45) & (df.Bearing < 45)

df1 = df[mask1] # launch angle below 8deg
df2 = df[mask2] # manually categorized as ground ball

mask12 = (df1.HitType == 'GroundBall')
df12 = df1[mask12] # manually categorized ground ball among with launch angle below 8deg

mask21 = (df2.Angle <= 8)
df21 = df2[mask21] # launch angle below 8deg among the categorized ground ball

print("proportion of the groundballs among <8deg = %.1f%%" % (100*len(df12)/len(df1)))
print("proportion of <8deg among the groundballs = %.1f%%" % (100*len(df21)/len(df2)))