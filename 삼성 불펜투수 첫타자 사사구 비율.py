# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 17:07:31 2021

@author: LIONS
"""

import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', index_col=False, encoding='cp949')
df = df[df.PitcherTeam == 'SAM_LIO']
df = df[df.Date >= '08/01/2021']
df = df.assign(PA=np.where((df.PlayResult!='Undefined') | (df.KorBB!='Undefined') | (df.PitchCall=='HitByPitch'), 1, 0))
df = df[df.PA == 1]

df['PAofPitcher'] = np.nan
for i in range(len(df.index)):
    if i == 0:
        df['PAofPitcher'].iloc[i] = 1
    else:
        if df['kbo_pid'].iloc[i] == df['kbo_pid'].iloc[i-1]:
            if df['kbo_bid'].iloc[i] == df['kbo_bid'].iloc[i-1]:
                df['PAofPitcher'].iloc[i] = df['PAofPitcher'].iloc[i-1]
            else:
                df['PAofPitcher'].iloc[i] = df['PAofPitcher'].iloc[i-1] + 1
        else:
            df['PAofPitcher'].iloc[i] = 1
df = df[(df.PAofPitcher == 1)&((df.Inning==7)|(df.Inning==8))]

sambb = df[['kbo_pid', 'PitName1']].drop_duplicates(subset=['kbo_pid'])

pitlist = sambb.kbo_pid.tolist()
bblist = []
for pit in pitlist:
    temp = df[df.kbo_pid == pit]
    mask = (temp.KorBB == 'Walk')
    bb = temp[mask]
    bblist.append(len(bb.index)/len(temp.index))

sambb['BBrate'] = bblist
sambb.to_csv("C:\\Users\\LIONS\\.spyder-py3\\9월 2주\\삼성 불펜투수 첫타자 볼넷 비율(후반기).csv", encoding='cp949')