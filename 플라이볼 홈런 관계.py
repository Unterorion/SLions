# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:10:46 2021

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

df = pd.read_excel("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\홈런비 뜬공비.xlsx")
#%%
df.dropna(subset=['FB%'], inplace=True)

R = df.corr()
R2 = R**2

corr = R['FB%'].loc['HR/BIP']
Rsq = corr**2

fig = plt.figure(figsize=(10,12))
ax = fig.add_subplot(1,1,1)

sns.regplot(x=df['FB%'], y=df['HR/BIP'], ax=ax)
ax.set_xlabel("뜬공비", fontsize=20)
ax.set_ylabel("타구 당 홈런", fontsize=20)
ax.set_title("18~21 뜬공비 - 홈런비 관계\n(Correlation %.3f, R-squared %.3f)\n"%(corr,Rsq), fontsize=25)
#%%
plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\뜬공비 홈런비 관계(타구) 2.png")