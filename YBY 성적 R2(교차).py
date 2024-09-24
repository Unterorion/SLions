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

stat1 = 'ERA'
stat2 = 'FIP'
df = pd.read_excel('C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\YBY %s-%s.xlsx' % (stat1, stat2), index_col=False)

df = df[['Last'+stat1, 'Next'+stat2]]
df = df.dropna(subset = ['Next'+stat2])

R = df.corr()
corr = float(R['Last'+stat1].loc['Next'+stat2])
R2 = pd.DataFrame(columns=['Last'+stat1, 'Next'+stat2], index=['Last'+stat1, 'Next'+stat2])
R2['Last'+stat1] = R['Last'+stat1]**2
R2['Next'+stat2] = R['Next'+stat2]**2
Rsq = float(R2['Last'+stat1].loc['Next'+stat2])

fig = plt.figure(figsize=(10,12))
ax = fig.add_subplot(1,1,1)
sns.regplot(x='Last'+stat1, y='Next'+stat2, data=df, ax=ax)
ax.set_title("Year-by-year %s - %s\n(Correlation %.3f, R-square %.3f)\n" % (stat1, stat2, corr, Rsq), fontsize = 25)
ax.set_xlabel("전년도 %s" % stat1, fontsize=20)
ax.set_ylabel("다음 해 %s" % stat2, fontsize=20)

plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\YBY %s-%s.png" % (stat1, stat2))
