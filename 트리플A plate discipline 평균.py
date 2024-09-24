# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 11:25:57 2021

@author: LIONS
"""

import pandas as pd

df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\AAA2021.csv", index_col=False, encoding='cp949')
df = df[df.Level == 'AAA']

maskZ = (df.PlateLocSide>-0.254) & (df.PlateLocSide<0.254) & (df.PlateLocHeight>0.4572) & (df.PlateLocHeight<1.0668)
dfZ = df[maskZ]
dfO = df[~maskZ]

maskZS = (dfZ.PitchCall == 'StrikeSwinging') | (dfZ.PitchCall == 'FoulBall') | (dfZ.PitchCall == 'InPlay')
maskZC = (dfZ.PitchCall == 'FoulBall') | (dfZ.PitchCall == 'InPlay')

maskOS = (dfO.PitchCall == 'StrikeSwinging') | (dfO.PitchCall == 'FoulBall') | (dfO.PitchCall == 'InPlay')
maskOC = (dfO.PitchCall == 'FoulBall') | (dfO.PitchCall == 'InPlay')

dfZS = dfZ[maskZS]
dfZC = dfZ[maskZC]
dfOS = dfO[maskOS]
dfOC = dfO[maskOC]

print("스윙률 : 존안 %.3f, 존밖 %.3f" % (len(dfZS.index)/len(dfZ.index), len(dfOS.index)/len(dfO.index)))
print("컨택률 : 존안 %.3f, 존밖 %.3f" % (len(dfZC.index)/len(dfZS.index), len(dfOC.index)/len(dfOS.index)))

dfBBE = df.dropna(subset=['Bearing'])

maskpull = ((dfBBE.BatterSide=='Left')&(dfBBE.Bearing>15)) | ((dfBBE.BatterSide=='Right')&(dfBBE.Bearing<-15))
maskoppo = ((dfBBE.BatterSide=='Left')&(dfBBE.Bearing<-15)) | ((dfBBE.BatterSide=='Right')&(dfBBE.Bearing>15))
maskcent = (dfBBE.Bearing>-15) & (dfBBE.Bearing<15)
maskhard = (dfBBE.ExitSpeed > 155)

dfpull = dfBBE[maskpull]
dfoppo = dfBBE[maskoppo]
dfcent = dfBBE[maskcent]
dfhard = dfBBE[maskhard]