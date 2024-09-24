# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 13:43:38 2021

@author: LIONS
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("C:\\Users\\LIONS\\.spyder-py3\\10월 2주\\홈런 등가교환.xlsx", index_col=None)

R = df.corr()
R2 = R**2

R2.to_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 2주\\HR% R2.csv", encoding='cp949')

cols = R2.columns.tolist()
cols = cols[1:]

for col in cols:
    fig = plt.figure(figsize=(10,12))
    ax = fig.add_subplot(1,1,1)
    
    corr = R[col].loc['HR%']
    r2 = R2[col].loc['HR%']
    sns.regplot(x='HR%', y=col, data=df, ax=ax)
    ax.set_title("HR%% - %s correlation\n(corr = %.3f, R-square = %.3f)" % (col, corr, r2), fontsize=30)
    ax.set_xlabel('HR%')
    ax.set_ylabel(col)
    plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\10월 2주\\HR%% corr\\HR%% - %s corr.png" % col)
