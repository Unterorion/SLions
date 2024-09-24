# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 13:56:10 2021

@author: LIONS
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv", index_col=None, encoding='cp949')
df.dropna(subset=['ExitSpeed'], inplace=True)
df = df[df['Stadium'] == 'DaeguPark']

def BA(pr):
    if pr=='Single' or pr=='Double' or pr=='Triple' or pr=='HomeRun':
        return 1
    else:
        return 0

def SLG(pr):
    if pr == 'Single':
        return 1
    elif pr == 'Double':
        return 2
    elif pr == 'Triple':
        return 3
    elif pr == 'HomeRun':
        return 4
    else:
        return 0

df['BA'] = df['PlayResult'].apply(BA)
df['SLG'] = df['PlayResult'].apply(SLG)

fig, ax = plt.subplots(1, figsize=(10,12), constrained_layout=True)
ax.scatter(df['SLG'], df['Angle'])

fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(1,1,1)
ax.set_xlim(-90,90)
sns.kdeplot(data=df[df['SLG']==1], x='Angle', label=1)
sns.kdeplot(data=df[df['SLG']==2], x='Angle', label=2)
sns.kdeplot(data=df[df['SLG']==3], x='Angle', label=3)
sns.kdeplot(data=df[df['SLG']==4], x='Angle', label=4)
plt.legend()
#%%
fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(1,1,1)
ax.set_xlim(-90,90)
sns.kdeplot(data=df, multiple='fill', x='Angle', hue='SLG')