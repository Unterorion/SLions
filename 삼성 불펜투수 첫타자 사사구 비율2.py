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
            df['PAofPitcher'].iloc[i] = df['PAofPitcher'].iloc[i-1] + 1
        else:
            j = i - 1
            while df['kbo_pid'].iloc[j] != df['kbo_pid'].iloc[i]:
                j -= 1
            if j != -1:
                if df['GameID'].iloc[j] == df['GameID'].iloc[i]:
                    df['PAofPitcher'].iloc[i] = df['PAofPitcher'].iloc[j]
                else:
                    df['PAofPitcher'].iloc[i] = 1
            else:
                df['PAofPitcher'].iloc[i] = 1

df = df[(df.PAofPitcher == 1)&((df.Inning==7)|(df.Inning==8))]

def walk(KorBB):
    if KorBB == 'Walk':
        return 1
    else:
        return 0

def HBP(pc):
    if pc == 'HitByPitch':
        return 1
    else:
        return 0

df['BB'] = df['KorBB'].apply(walk)
df['HBP'] = df['PitchCall'].apply(HBP)
df['Walk'] = df['BB'] + df['HBP']

pt1 = pd.pivot_table(df, index=['kbo_pid', 'PitName1'], values='Walk', aggfunc='mean')
pt2 = pd.pivot_table(df, index=['kbo_pid', 'PitName1'], values='PA', aggfunc='sum')
pt = pd.concat([pt1, pt2], axis=1)