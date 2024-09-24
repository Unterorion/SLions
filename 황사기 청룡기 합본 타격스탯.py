# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 10:19:07 2021

@author: LIONS
"""

import pandas as pd
import numpy as np
from matplotlib import font_manager, rc

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

idmap = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\스카우팅 대상자(고졸타자) ID.csv", index_col=False, encoding='cp949')
df = pd.read_csv("C:\\Users\\LIONS\\Desktop\\고교야구\\황사기 청룡기 통합.csv", index_col=False, encoding='cp949')

for i in range(len(idmap.index)):
    ID = idmap.ID.iloc[i]
    df_indi = df[df.BatterId == ID]
    if len(df_indi.index) > 0:
        df_batted = df_indi.dropna(subset = ['ExitSpeed'])
        ESlist = df_batted.ExitSpeed.tolist()
        if len(ESlist) > 0:
            idmap['최고타구속도'].iloc[i] = max(ESlist)
        else:
            idmap['최고타구속도'].iloc[i] = '타구 없음'
        
        maskZ = (df_indi.PlateLocSide > -0.254) & (df_indi.PlateLocSide < 0.254) & (df_indi.PlateLocHeight < 1.0668) & (df_indi.PlateLocHeight > 0.4572)
        dfZ = df_indi[maskZ]
        dfO = df_indi[~maskZ]
        
        if len(dfZ.index) > 0:
            maskZS = (dfZ.PitchCall == 'InPlay') | (dfZ.PitchCall == 'FoulBall') | (dfZ.PitchCall == 'StrikeSwinging')
            dfZS = dfZ[maskZS]
            Zsr = 100*len(dfZS.index)/len(dfZ.index)
        else:
            Zsr = '해당 없음'
        idmap['존안 스윙률'].iloc[i] = Zsr
        
        if len(dfO.index) > 0:
            maskOS = (dfO.PitchCall == 'InPlay') | (dfO.PitchCall == 'FoulBall') | (dfO.PitchCall == 'StrikeSwinging')
            dfOS = dfO[maskOS]
            Osr = 100*len(dfOS.index)/len(dfO.index)
        else:
            Osr = '해당 없음'
        idmap['존밖 스윙률'].iloc[i] = Osr
        
        if Zsr != '해당 없음' and Osr != '해당 없음':
            idmap['존안-존밖 스윙률'].iloc[i] = Zsr - Osr
        else:
            idmap['존안-존밖 스윙률'].iloc[i] = '해당 없음'
        
        dfHS = df_indi[df_indi.RelSpeed > 135]
        maskHSS = (dfHS.PitchCall == 'InPlay') | (dfHS.PitchCall == 'FoulBall') | (dfHS.PitchCall == 'StrikeSwinging')
        maskHSW = (dfHS.PitchCall == 'StrikeSwinging')
        dfHSS = dfHS[maskHSS]
        dfHSW = dfHS[maskHSW]
        
        if len(dfHSS.index) > 0:
            idmap['135 이상 헛스윙률'].iloc[i] = 100*len(dfHSW.index)/len(dfHSS.index)
        else:
            idmap['135 이상 헛스윙률'].iloc[i] = '해당 없음'

idmap.to_csv("C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\스카우팅 대상자(고졸타자) ID 및 스탯.csv", encoding='cp949')