# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 11:48:55 2021

@author: LIONS
"""

import pandas as pd
import numpy as np

df=pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', index_col=False, encoding='cp949')
df = df.dropna(subset=['ExitSpeed'])
df = df[df.PitchCall == 'InPlay']

def Hit(PR):
    if PR=='Single' or PR=='Double' or PR=='Triple' or PR=='HomeRun':
        return 1
    else:
        return 0

df['Hit'] = None
df.Hit = df.PlayResult.apply(Hit)

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

df['TotalBases'] = None
df.TotalBases = df.PlayResult.apply(TB)

ang = 3
ES = 120

mask = (df.ExitSpeed>ES-0.5) & (df.ExitSpeed<ES+0.5) & (df.Angle>ang-0.5) & (df.Angle<ang+0.5)
df_temp = df[mask]
TBlist = df_temp.TotalBases.tolist()
Htlist = df_temp.Hit.tolist()

xBA = np.mean(Htlist)
xSLG = np.mean(TBlist)

print("xBA for %dkm/h, %ddeg = %.3f" % (ES, ang, xBA))
print("xSLG for %dkm/h, %ddeg = %.3f" % (ES, ang, xSLG))