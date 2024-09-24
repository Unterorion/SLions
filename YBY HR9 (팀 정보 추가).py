# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 21:04:14 2021

@author: LIONS
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc
import matplotlib

matplotlib.rcParams['axes.unicode_minus'] = False

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

stat = 'HR/9'
df = pd.read_excel('C:\\Users\\LIONS\\.spyder-py3\\8월 4주\\YBY HR9(팀 정보 추가).xlsx', index_col=False)

df = df[['Last', 'Next']]
df = df.dropna(subset = ['Next'])
df.reset_index(inplace=True, drop=True)

R = df.iloc[32:].corr()
corr = float(R.Last.loc['Next'])
R2 = pd.DataFrame(columns=['Last', 'Next'], index=['Last', 'Next'])
R2.Last = R.Last**2
R2.Next = R.Next**2
Rsq = float(R2.Last.loc['Next'])

fig = plt.figure(figsize=(10,12))
ax = fig.add_subplot(1,1,1)
sns.regplot(x='Last', y='Next', data=df[32:], ax=ax)
ax.set_title("Year-by-year %s (팀 변동 X)\n(Correlation %.3f, R-square %.3f)\n" % (stat, corr, Rsq), fontsize = 25)
ax.set_xlabel("전년도 %s" % stat, fontsize=20)
ax.set_ylabel("다음 해 %s" % stat, fontsize=20)

plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\8월 4주\\YBY HR9 (17 팀변동X).png")
