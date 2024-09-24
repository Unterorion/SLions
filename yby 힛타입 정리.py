# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 19:12:35 2021

@author: LIONS
"""

import pandas as pd

df = pd.read_excel("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\50이닝 투수(2021).xlsx")
df.set_index('PitName1', inplace=True)
df.dropna(subset=['Next'], inplace=True)

ht18 = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\2020hittype.csv", index_col=False, encoding='cp949')
ht19 = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\2021hittype.csv", index_col=False, encoding='cp949')

fb1819 = df.join(ht18.set_index('PitName1')['FBrate'], on='PitName1')
fb1819.rename(columns={'FBrate':'FBrate20'}, inplace=True)
fb1819 = fb1819.join(ht19.set_index('PitName1')['FBrate'], on='PitName1')
fb1819.rename(columns={'FBrate':'FBrate21'}, inplace=True)
fb1819.drop(['Last', 'Next'], axis=1, inplace=True)
fb1819.dropna(subset=['FBrate21','FBrate20'], inplace=True)
fb1819.to_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\뜬공비 2021.csv", encoding='cp949')

ld1819 = df.join(ht18.set_index('PitName1')['LDrate'], on='PitName1')
ld1819.rename(columns={'LDrate':'LDrate20'}, inplace=True)
ld1819 = ld1819.join(ht19.set_index('PitName1')['LDrate'], on='PitName1')
ld1819.rename(columns={'LDrate':'LDrate21'}, inplace=True)
ld1819.drop(['Last', 'Next'], axis=1, inplace=True)
ld1819.dropna(subset=['LDrate21','LDrate20'], inplace=True)
ld1819.to_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\라이너 2021.csv", encoding='cp949')

gb1819 = df.join(ht18.set_index('PitName1')['GBrate'], on='PitName1')
gb1819.rename(columns={'GBrate':'GBrate20'}, inplace=True)
gb1819 = gb1819.join(ht19.set_index('PitName1')['GBrate'], on='PitName1')
gb1819.rename(columns={'GBrate':'GBrate21'}, inplace=True)
gb1819.drop(['Last', 'Next'], axis=1, inplace=True)
gb1819.dropna(subset=['GBrate21','GBrate20'], inplace=True)
gb1819.to_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\땅볼비 2021.csv", encoding='cp949')
