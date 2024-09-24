# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 13:20:17 2021

@author: LIONS
"""

import pandas as pd

df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', encoding='cp949')
df = df[df.Level == 'KBO']
maskS = (df.PitchCall=='StrikeSwinging') | (df.PitchCall=='FoulBall') | (df.PitchCall=='InPlay')
maskW = (df.PitchCall=='StrikeSwinging')

dfS = df[maskS]
dfW = df[maskW]

print("Total swing rate = %.3f, total whiff rate = %.3f" % (len(dfS.index)/len(df.index), len(dfW.index)/len(dfS.index)))

maskZ = (df.PlateLocSide>-0.254)&(df.PlateLocSide<0.254)&(df.PlateLocHeight>0.4572)&(df.PlateLocHeight<1.0668)
maskZS = (dfS.PlateLocSide>-0.254)&(dfS.PlateLocSide<0.254)&(dfS.PlateLocHeight>0.4572)&(dfS.PlateLocHeight<1.0668)
maskZW = (dfW.PlateLocSide>-0.254)&(dfW.PlateLocSide<0.254)&(dfW.PlateLocHeight>0.4572)&(dfW.PlateLocHeight<1.0668)

dfZ = df[maskZ]
dfZS = dfS[maskZS]
dfZW = dfW[maskZW]

print("Zone swing rate = %.3f, zone whiff rate = %.3f" % (len(dfZS.index)/len(dfZ.index), len(dfZW.index)/len(dfZS.index)))

dfO = df[~maskZ]
dfOS = dfS[~maskZS]
dfOW = dfW[~maskZW]

print("Outzone swing rate = %.3f, outzone whiff rate = %.3f" % (len(dfOS.index)/len(dfO.index), len(dfOW.index)/len(dfOS.index)))

df = df[df.Strikes == 2]
print("\nAfter 2 strikes")
maskS = (df.PitchCall=='StrikeSwinging') | (df.PitchCall=='FoulBall') | (df.PitchCall=='InPlay')
maskW = (df.PitchCall=='StrikeSwinging')

dfS = df[maskS]
dfW = df[maskW]

print("Total swing rate = %.3f, total whiff rate = %.3f" % (len(dfS.index)/len(df.index), len(dfW.index)/len(dfS.index)))

maskZ = (df.PlateLocSide>-0.254)&(df.PlateLocSide<0.254)&(df.PlateLocHeight>0.4572)&(df.PlateLocHeight<1.0668)
maskZS = (dfS.PlateLocSide>-0.254)&(dfS.PlateLocSide<0.254)&(dfS.PlateLocHeight>0.4572)&(dfS.PlateLocHeight<1.0668)
maskZW = (dfW.PlateLocSide>-0.254)&(dfW.PlateLocSide<0.254)&(dfW.PlateLocHeight>0.4572)&(dfW.PlateLocHeight<1.0668)

dfZ = df[maskZ]
dfZS = dfS[maskZS]
dfZW = dfW[maskZW]

print("Zone swing rate = %.3f, zone whiff rate = %.3f" % (len(dfZS.index)/len(dfZ.index), len(dfZW.index)/len(dfZS.index)))

dfO = df[~maskZ]
dfOS = dfS[~maskZS]
dfOW = dfW[~maskZW]

print("Outzone swing rate = %.3f, outzone whiff rate = %.3f" % (len(dfOS.index)/len(dfO.index), len(dfOW.index)/len(dfOS.index)))
