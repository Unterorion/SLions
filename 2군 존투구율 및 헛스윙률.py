# -*- coding: utf-8 -*-
"""
Created on Wed Jul 28 16:47:43 2021

@author: LIONS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
import matplotlib

matplotlib.rcParams['axes.unicode_minus'] = False

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', index_col=False, encoding='cp949')
dfm = df[df['PitcherTeam']=='MIN_SAM']

idmap = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\7월 5주\\투수.csv', index_col=False, encoding='cp949')
idmap = idmap.set_index('PitcherId')

pitIDlist = dfm['PitcherId'].unique().tolist()
namelist = []
Zratelist = []
Wratelist = []

for ID in pitIDlist:
    name = idmap['PitName1'].loc[ID]
    maskID = (dfm['PitcherId']==ID)
    df_indi = dfm[maskID]
    
    maskZ = (df_indi['PlateLocHeight']>0.4572) & (df_indi['PlateLocHeight']<1.0668) & (df_indi['PlateLocSide']<0.254) & (df_indi['PlateLocSide']>-0.254)
    df_indiZ = df_indi[maskZ]
    
    maskS = (df_indi['PitchCall']=='StrikeSwinging') | (df_indi['PitchCall']=='FoulBall') | (df_indi['PitchCall']=='InPlay')
    df_indiS = df_indi[maskS]
    maskW = (df_indi['PitchCall']=='StrikeSwinging')
    df_indiW = df_indi[maskW]
    
    Zrate = 100*len(df_indiZ.index)/len(df_indi.index)
    Wrate = 100*len(df_indiW.index)/len(df_indiS.index)
    
    namelist.append(name)
    Zratelist.append(Zrate)
    Wratelist.append(Wrate)
    
dfZW = pd.DataFrame({'PitName1':namelist, 'PitcherId':pitIDlist, 'Zrate':Zratelist, 'Wrate':Wratelist})
dfZW.to_csv('C:\\Users\\LIONS\\.spyder-py3\\7월 5주\\2군 존투구율 및 헛스윙률.csv', encoding='cp949')

maskZ = (df['PlateLocHeight']>0.4572) & (df['PlateLocHeight']<1.0668) & (df['PlateLocSide']<0.254) & (df['PlateLocSide']>-0.254)
maskS = (df['PitchCall']=='StrikeSwinging') | (df['PitchCall']=='FoulBall') | (df['PitchCall']=='InPlay')
maskW = (df['PitchCall']=='StrikeSwinging')

dfZ = df[maskZ]
dfS = df[maskS]
dfW = df[maskW]

print("리그 전체 존 투구율 = %.1f%%" % (100*len(dfZ.index)/len(df.index)))
print("리그 전체 헛스윙률 = %.1f%%" % (100*len(dfW.index)/len(dfS.index)))