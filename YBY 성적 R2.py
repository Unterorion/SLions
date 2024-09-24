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

stat = 'K%'

df = pd.read_excel("C:\\Users\\kimyj\\OneDrive\\바탕 화면\\YBY %s.xlsx" % stat, index_col=False)

R = df.corr()
corr = float(R.Last.loc['Next'])
R2 = pd.DataFrame(columns=['Last', 'Next'], index=['Last', 'Next'])
R2.Last = R.Last**2
R2.Next = R.Next**2
Rsq = float(R2.Last.loc['Next'])

fig = plt.figure(figsize=(10,12))
ax = fig.add_subplot(1,1,1)
sns.regplot(x='Last', y='Next', data=df, ax=ax)
ax.set_title("Year-by-year record\n(Correlation %.3f, R-squared %.3f)\n" % (corr, Rsq), fontsize = 25)
ax.set_xlabel("Year n", fontsize=20)
ax.set_ylabel("Year n+1", fontsize=20)

#plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\YBY\\YBY %s.png" % stat)
