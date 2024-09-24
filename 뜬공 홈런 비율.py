# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 16:35:59 2021

@author: LIONS
"""

import pandas as pd
import numpy as np

df18 = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2018.csv", index_col=None, encoding='cp949')
df19 = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2019.csv", index_col=None, encoding='cp949')
df20 = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2020.csv", index_col=None, encoding='cp949')
df21 = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv", index_col=None, encoding='cp949')

df = pd.concat([df18,df19,df20,df21], axis=0)
#%%
df = df[(df['Level']=='KBO')&(df['PitchCall']=='InPlay')]
df.dropna(subset=['Angle'], inplace=True)

df = df.assign(HR = np.where(df['PlayResult']=='HomeRun', 1, 0))
df = df[df['Angle']>15]

pt = df.pivot_table(values='HR', index='Stadium', aggfunc='mean')
#%%
pt.to_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 4주\\뜬공 홈런 비율(18~21).csv", encoding='cp949')