# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 16:03:46 2021

@author: LIONS
"""

import pandas as pd
import glob
import os

input_file = r'C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\외인 구종분류'
allFile_list = glob.glob(os.path.join(input_file, '*csv'))

dfAll = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\AAA2021.csv', index_col=False, encoding='cp949')
pitidmap = dfAll[['PitcherId', 'Pitcher']]
pitidmap.drop_duplicates(subset=['PitcherId'], inplace=True)
pitidmap.set_index('PitcherId', inplace=True)

for file in allFile_list:
    df = pd.read_csv(file, encoding='cp949')
    ID = df.PitcherId.iloc[0]
    rawname = pitidmap.Pitcher.loc[ID]
    Name = rawname.split(', ')
    name = Name[1] + ' ' + Name[0]
    print(name)
    ptypelist = df.ClusterName.unique().tolist()
    
    info = pd.DataFrame(columns=['ClusterName', 'RelSpeed', 'SpinRate', 'InducedVertBreak', 'HorzBreak'])
    info.ClusterName = ptypelist
    info.set_index('ClusterName', inplace=True)
    
    for ptype in ptypelist:
        dfp = df[df.ClusterName == ptype]
        RS = dfp.RelSpeed.mean()
        SR = dfp.SpinRate.mean()
        VM = dfp.InducedVertBreak.mean()
        HM = dfp.HorzBreak.mean()
        
        info.RelSpeed.loc[ptype] = RS
        info.SpinRate.loc[ptype] = SR
        info.InducedVertBreak.loc[ptype] = VM
        info.HorzBreak.loc[ptype] = HM
        
        print("%s : 구속 %.1fkm/h, 회전수 %d, 수직 무브먼트 %.1fcm, 수평 무브먼트 %.1fcm" % (ptype, RS, SR, VM, HM))
    print("\n")
    info.to_csv('C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\외인 구종분류\\%s 구종 속성.csv' % name, encoding='cp949')