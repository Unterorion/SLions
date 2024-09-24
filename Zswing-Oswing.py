# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 18:02:26 2021

@author: LIONS
"""

import pandas as pd

df_draft = pd.read_excel('C:\\Users\\LIONS\\.spyder-py3\\7월 3주\\스카우팅 대상자(고졸타자) 청룡기.xlsx')
df_all = pd.read_csv('C:\\Users\\LIONS\\Desktop\\고교야구\\청룡기 통합.csv')
SwingPercList = []

for i in range(len(df_draft.index)):
    ID = df_draft['ID'].iloc[i]
    df_indi = df_all[df_all['BatterId'] == ID]
    df_indi = df_indi.dropna(subset = ['RelSpeed'])
    if len(df_indi.index) > 0:
        maskZ = (df_indi.PlateLocSide>-0.254) & (df_indi.PlateLocSide<0.254) & (df_indi.PlateLocHeight>0.4572) & (df_indi.PlateLocSide<1.0668)
        maskO = (df_indi.PlateLocSide<-0.254) | (df_indi.PlateLocSide>0.254) | (df_indi.PlateLocHeight<0.4572) | (df_indi.PlateLocSide>1.0668)
        dfZ = df_indi[maskZ]
        dfO = df_indi[maskO]
        
        maskZS = (dfZ.PitchCall=='StrikeSwinging') | (dfZ.PitchCall=='FoulBall') | (dfZ.PitchCall=='InPlay')
        maskOS = (dfO.PitchCall=='StrikeSwinging') | (dfO.PitchCall=='FoulBall') | (dfO.PitchCall=='InPlay')
        dfZS = dfZ[maskZS]
        dfOS = dfO[maskOS]
        
        perc = 100*(len(dfZS.index)/len(dfZ.index)-len(dfOS.index)/len(dfO.index))
        SwingPercList.append(perc)
    else:
        SwingPercList.append(None)

SwingPercDict = {'존안-존밖스윙률' : SwingPercList}
ResultDF = pd.DataFrame(SwingPercDict)
ResultDF.to_csv('C:\\Users\\LIONS\\.spyder-py3\\7월 3주\\청룡기 존안-존밖스윙률.csv', encoding = 'cp949')