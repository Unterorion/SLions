# -*- coding: utf-8 -*-
"""
Created on Tue Sep  7 17:07:31 2021

@author: LIONS
"""

import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', index_col=False, encoding='cp949')
df = df[df.Level == 'KBO']
df = df[df['Date'] >= '08/01/2021']
df = df.assign(PA=np.where((df.PlayResult!='Undefined') | (df.KorBB!='Undefined') | (df.PitchCall=='HitByPitch'), 1, 0))

df = df[df.PA == 1]

teamlist = df.PitcherTeam.unique().tolist()
bblist = []

lg = 0
lgbb = 0

for team in teamlist:
    temp = df[df.PitcherTeam == team]
    temp['PAofPitcher'] = np.nan
    
    for i in range(len(temp.index)):
        if i == 0:
            temp['PAofPitcher'].iloc[i] = 1
        else:
            if temp['kbo_pid'].iloc[i] == temp['kbo_pid'].iloc[i-1]:
                if temp['kbo_bid'].iloc[i] == temp['kbo_bid'].iloc[i-1]:
                    temp['PAofPitcher'].iloc[i] = temp['PAofPitcher'].iloc[i-1]
                else:
                    temp['PAofPitcher'].iloc[i] = temp['PAofPitcher'].iloc[i-1] + 1
            else:
                temp['PAofPitcher'].iloc[i] = 1
    temp = temp[(temp.PAofPitcher == 1)&((temp.Inning==7)|(temp.Inning==8))]
    mask = (temp.KorBB == 'Walk')|(temp.PitchCall == 'HitByPitch')
    bb = temp[mask]
    print("%s %.3f" % (team, len(bb.index)/len(temp.index)))
    bblist.append(len(bb.index)/len(temp.index))
    lg += len(temp.index)
    lgbb += len(bb.index)
    #temp.to_csv("C:\\Users\\LIONS\\.spyder-py3\\9월 2주\\불펜투수 첫타자 볼넷\\%s.csv" % team, encoding='cp949')
#temp.pivot_table(index='kbo_pid', values='BB')
teambb = pd.DataFrame({'Team':teamlist, 'BBrate':bblist})
teambb.to_csv("C:\\Users\\LIONS\\.spyder-py3\\9월 2주\\팀별 불펜투수 첫타자 사사구 비율(후반기).csv", encoding='cp949')
print("league average = %.3f" % (lgbb/lg))