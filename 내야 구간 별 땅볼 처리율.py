# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 13:33:57 2021

@author: LIONS
"""

import pandas as pd

#df20 = pd.read_csv('2020_Classified_한글_4th_Edition_누락분_pitchfx.csv')
df21 = pd.read_csv('C:\\Users\\kimyj\\OneDrive\\바탕 화면\\2021KBOwithFutures.csv')
#%%
#df = pd.concat([df20, df21], ignore_index=True)

#df.to_csv("통합.csv")

# 기간 선택하기
#df_temp = df
#df_temp = df20
df_temp = df21

SecList = []
HitNumList = []
OutNumList = []
PercList = []

for i in range(18):
    SecList.append("%d ~ %d" % (5*i-45, 5*i-40))
    mask1 = (df_temp.PlayResult != 'Sacrifice') & (df_temp.HitType != 'FlyBall') & (df_temp.PitchCall != 'FoulBall') & (df_temp.Angle <= 8) & (df_temp.Bearing > 5*i-45) & (df_temp.Bearing < 5*i-40)
    df_hit = df_temp[mask1]
    HitNum = len(df_hit.index)
    
    mask2 = (df_hit.PlayResult == 'Out')
    df_out = df_hit[mask2]
    OutNum = len(df_out.index)
    
    HitNumList.append(HitNum)
    OutNumList.append(OutNum)
    PercList.append(100*OutNum/HitNum)
    print("%d ~ %d : number of hit = %d, number of out = %d, fielding rate = %.1f%%" % (5*i-45, 5*i-40, HitNum, OutNum, 100*OutNum/HitNum))

FieldingRate_dict = {'Section' : SecList, 'HitNumber' : HitNumList, 'OutNumber' : OutNumList, 'FieldingRate' : PercList}
FieldingRate = pd.DataFrame(FieldingRate_dict)
FieldingRate.set_index('Section', inplace=True)

FieldingRate.to_csv("C:\\Users\\kimyj\\OneDrive\\바탕 화면\\2021 내야 구간 별 땅볼 처리율.csv")