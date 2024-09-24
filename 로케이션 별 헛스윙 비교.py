# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 17:39:04 2021

@author: LIONS
"""

import pandas as pd

df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv", index_col=False, encoding='cp949')
df.dropna(subset=['RelSpeed'], inplace=True)
mask1 = (df.BatterTeam=='LG_TWI')|(df.BatterTeam=='DOO_BEA')|(df.BatterTeam=='KIW_HER')|(df.BatterTeam=='SSG_LAN')|(df.BatterTeam=='KT_WIZ')|(df.BatterTeam=='HAN_EAG')|(df.BatterTeam=='KIA_TIG')|(df.BatterTeam=='SAM_LIO')|(df.BatterTeam=='LOT_GIA')|(df.BatterTeam=='NC_DIN')
df = df[mask1]

maskH = (df.PlateLocSide>-0.1693)&(df.PlateLocSide<0.1693)&(df.PlateLocHeight>0.5588)&(df.PlateLocHeight<0.9652)
maskS = (df.PlateLocSide>-0.3387)&(df.PlateLocSide<0.3387)&(df.PlateLocHeight>0.3556)&(df.PlateLocHeight<1.1684)
maskC = (df.PlateLocSide>-0.508)&(df.PlateLocSide<0.508)&(df.PlateLocHeight>0.1524)&(df.PlateLocHeight<1.3716)

dfH = df[maskH]
dfS = df[maskS & ~maskH]
dfC = df[maskC & ~maskS]
dfW = df[~maskC]

Zone = ["Heart", "Shadow", "Chase", "Waste"]
dfs = [dfH, dfS, dfC, dfW]

for i in range(4):
    dfz = dfs[i]
    loc = len(dfz.index)/len(df.index)
    maskSwing = (dfz.PitchCall == 'StrikeSwinging') | (dfz.PitchCall == 'InPlay') | (dfz.PitchCall == 'FoulBall')
    maskWhiff = (dfz.PitchCall == 'StrikeSwinging')
    maskTake = (dfz.PitchCall == 'StrikeCalled') | (dfz.PitchCall == 'BallCalled') | (dfz.PitchCall == 'HitByPitch')
    dfzs = dfz[maskSwing]
    dfzw = dfz[maskWhiff]
    dfzt = dfz[maskTake]
    swing = len(dfzs.index)/len(dfz.index)
    take = len(dfzt.index)/len(dfz.index)
    whiff = len(dfzw.index)/len(dfzs.index)
    
    zone = Zone[i]
    print("%s : 구사율 %.1f%%, 스윙률 %.1f%%, 헛스윙률 %.1f%%" % (zone, loc*100, swing*100, whiff*100))

print("\n")
dfWhiff = df[df.PitchCall == 'StrikeSwinging']
maskWH = (dfWhiff.PlateLocSide>-0.1693)&(dfWhiff.PlateLocSide<0.1693)&(dfWhiff.PlateLocHeight>0.5588)&(dfWhiff.PlateLocHeight<0.9652)
maskWS = (dfWhiff.PlateLocSide>-0.3387)&(dfWhiff.PlateLocSide<0.3387)&(dfWhiff.PlateLocHeight>0.3556)&(dfWhiff.PlateLocHeight<1.1684)
maskWC = (dfWhiff.PlateLocSide>-0.508)&(dfWhiff.PlateLocSide<0.508)&(dfWhiff.PlateLocHeight>0.1524)&(dfWhiff.PlateLocHeight<1.3716)

dfWH = dfWhiff[maskWH]
dfWS = dfWhiff[maskWS & ~maskWH]
dfWC = dfWhiff[maskWC & ~maskWS]
dfWW = dfWhiff[~maskWC]

dfw = [dfWH, dfWS, dfWC, dfWW]

for i in range(4):
    zone = Zone[i]
    dfww = dfw[i]
    rate = len(dfww.index)/len(dfWhiff.index)
    print("%s : 헛스윙 비율 %.1f%%" % (zone, 100*rate))