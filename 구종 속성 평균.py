# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 11:57:05 2021

@author: LIONS
"""

import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\7월 4주\\전체 투수 구종분류.csv', index_col=False, encoding='cp949')
mask1 = (df.BatterTeam=='LG_TWI')|(df.BatterTeam=='DOO_BEA')|(df.BatterTeam=='KIW_HER')|(df.BatterTeam=='SSG_LAN')|(df.BatterTeam=='KT_WIZ')|(df.BatterTeam=='HAN_EAG')|(df.BatterTeam=='KIA_TIG')|(df.BatterTeam=='SAM_LIO')|(df.BatterTeam=='LOT_GIA')|(df.BatterTeam=='NC_DIN')
df = df[mask1]

df = df.dropna(subset = ['ClusterName'])
dfl = df[df.PitcherThrows == 'Left']
dfr = df[df.PitcherThrows == 'Right']

for dfs in [dfl, dfr]:
    print('\n')
    print(dfs.PitcherThrows.iloc[0])
    ptypelist = dfs.ClusterName.unique().tolist()
    
    for ptype in ptypelist:
        dftype = dfs[dfs.ClusterName == ptype]
        RSlist = dftype['RelSpeed'].tolist()
        SRlist = dftype['SpinRate'].tolist()
        VMlist = dftype['InducedVertBreak'].tolist()
        HMlist = dftype['HorzBreak'].tolist()
        
        RSmean = np.mean(RSlist)
        SRmean = np.mean(SRlist)
        VMmean = np.mean(VMlist)
        HMmean = np.mean(HMlist)
        
        print("%s 평균 구속 %.1f, 회전수 %d, 수직 무브먼트 %.3f, 수평 무브먼트 %.3f" % (ptype, RSmean, SRmean, VMmean, HMmean))
        