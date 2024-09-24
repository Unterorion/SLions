# -*- coding: utf-8 -*-
"""
Created on Fri Oct 15 18:39:53 2021

@author: LIONS
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\HR% 연관성.xlsx")

R = df.corr()
R2 = R**2

R2.to_csv("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\HR% 연관성.csv", encoding='cp949')
#%%
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)
x = 'BB%'
y = 'HR%'
sns.regplot(x=x, y=y, data=df, ax=ax)
ax.set_title("%s - %s 연관성 (%.1f%%)\n" % (x,y,100*R2[x].loc[y]), fontsize=25)
ax.set_xlabel(x, fontsize=20)
ax.set_ylabel(y, fontsize=20)