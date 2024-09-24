# -*- coding: utf-8 -*-
"""
Created on Tue Aug 31 21:34:46 2021

@author: LIONS
"""

import pandas as pd
df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', encoding='cp949')
df = df[df.Level == 'KBO']
df = df[df.PitchCall == 'InPlay']
df.dropna(subset=['ExitSpeed'], inplace=True)

def TB(PR):
    if PR == 'Single':
        return 1
    elif PR == 'Double':
        return 2
    elif PR == 'Triple':
        return 3
    elif PR == 'HomeRun':
        return 4
    else:
        return 0

df['TB'] = df['PlayResult'].apply(TB)

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
    zone = Zone[i]
    slg = dfz.TB.mean()
    print("%s : 장타율 %.3f" % (zone, slg))
