# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:43:38 2021

@author: LIONS
"""

import pandas as pd

stat = 'BB9'

df = pd.read_excel("C:\\Users\\LIONS\\.spyder-py3\\9월 3주\\pbp 상관관계(%s).xlsx"%stat, index_col=None)

R = df.corr()
R2 = R**2

R2.to_csv("C:\\Users\\LIONS\\.spyder-py3\\9월 3주\\pbp R2(%s).csv"%stat, encoding='cp949')