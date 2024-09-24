# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 14:07:02 2021

@author: LIONS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import glob
import os

file_route = r'C:\\Users\\LIONS\\.spyder-py3\\7월 4주\\2군 투수 시각화'
allFile_list = glob.glob(os.path.join(file_route, '*.csv'))

idmap=pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\7월 4주\\투수.csv', index_col=False, encoding='cp949')

for file in allFile_list:
    df=pd.read_csv(file, index_col=False, encoding='cp949')
    
    ID = df['PitcherId'].iloc[0]
    idmap_pit = idmap[idmap['PitcherId'] == ID]
    name = idmap_pit['PitName1'].iloc[0]
    
    df['PitName1'] = name
    pitch = df['ClusterName'].drop_duplicates()
    pitchlist = pitch.tolist()
    
    totDist = pd.DataFrame()
    
    for ptype in pitchlist:
        ptypeDist = pd.DataFrame()
        df_type = df[df['ClusterName'] == ptype]
        n = len(df_type.index)
            
        RSrange = np.linspace(80, 160, 1000)
        RSlist = list(RSrange)
        ptypeDist['구속 범위'] = RSlist
        ptypeDist['구속 누적 분포'] = None
        for i in range(len(RSlist)):
            ptypeDist['구속 누적 분포'].iloc[i] = len(df_type[df_type['RelSpeed']<RSlist[i]])/n
            
        VMrange = np.linspace(-60, 80, 1000)
        VMlist = list(VMrange)
        ptypeDist['수직 무브먼트 범위'] = VMlist
        ptypeDist['수직 무브먼트 누적 분포'] = None
        for i in range(len(VMlist)):
            ptypeDist['수직 무브먼트 누적 분포'].iloc[i] = len(df_type[df_type['InducedVertBreak']<VMlist[i]])/n
            
        HMrange = np.linspace(-60, 60, 1000)
        HMlist = list(HMrange)
        ptypeDist['수평 무브먼트 범위'] = HMlist
        ptypeDist['수평 무브먼트 누적 분포'] = None
        for i in range(len(HMlist)):
            ptypeDist['수평 무브먼트 누적 분포'].iloc[i] = len(df_type[df_type['HorzBreak']<HMlist[i]])/n
            
        ptypeDist['구종'] = ptype
        
        totDist = pd.concat([ptypeDist, totDist], ignore_index=True)
        
    totDist['PitcherId'] = ID
    totDist['PitName1'] = name    
    totDist.to_csv('C:\\Users\\LIONS\\.spyder-py3\\7월 4주\\2군 투수 분포\\%s %d 누적 분포.csv' % (name, ID), encoding='cp949')
