# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 17:03:17 2021

@author: LIONS
"""

import pandas as pd
df = pd.read_excel("C:\\Users\\LIONS\\.spyder-py3\\8월 4주\\투수 스탯들.xlsx", index_col=False)
R = df.corr()
R2 = R**2
R2.to_csv("C:\\Users\\LIONS\\.spyder-py3\\8월 4주\\투수 HR9 - 기타 스탯 R2.csv", encoding='cp949')