# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:11:18 2021

@author: LIONS
"""

import pandas as pd
import os

filelist = os.listdir('C:\\Users\\LIONS\\.spyder-py3\\9월 3주\\외인 구종분류2')
namelist = []
for i in range(len(filelist)):
    if i%3 == 0:
        namelist.append(filelist[i])

for name in namelist:
    df1 = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\9월 3주\\외인 구종분류\\%s' % name, index_col=False, encoding='cp949')
    df2 = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\9월 3주\\외인 구종분류2\\%s' % name, index_col=False, encoding='cp949')
    df = pd.concat([df1, df2], ignore_index=True)
    df.to_csv('C:\\Users\\LIONS\\.spyder-py3\\9월 3주\\외인 구종분류 최종\\%s' % name, encoding='cp949')