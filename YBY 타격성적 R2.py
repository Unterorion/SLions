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

df = pd.read_excel('C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\YBY wOBA.xlsx', index_col=False)
dflist = [df]

for i in range(len(dflist)):
    df = dflist[i]
    stat = "wOBA"
    statK = "wOBA"
    
    df = df[['Last', 'Next']]
    df = df.dropna(subset = ['Next'])
    
    fig = plt.figure(figsize=(10,12))
    ax = fig.add_subplot(1,1,1)
    sns.regplot(x='Last', y='Next', data=df, ax=ax)
    ax.set_title("Year-by-year %s\n" % statK, fontsize = 25)
    ax.set_xlabel("전년도 %s" % statK, fontsize=20)
    ax.set_ylabel("다음 해 %s" % statK, fontsize=20)
    plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\YBY %d.%s.png" % (i+1, statK))
    
    R = df.corr()
    R2 = pd.DataFrame(columns=['Last', 'Next'], index=['Last', 'Next'])
    R2.Last = R.Last**2
    R2.Next = R.Next**2
    
    print("R square of year-by-year %s = %f, R = %f" % (stat, R2.Last.loc['Next'], R.Last.loc['Next']))