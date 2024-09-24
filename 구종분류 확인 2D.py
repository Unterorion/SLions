# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 14:31:27 2021

@author: LIONS
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\외인 최종\\Camarena, Daniel.csv', index_col=False, encoding='cp949')
#df = df[(df['ClusterName']=='Fastball')|(df['ClusterName']=='Sinker')]
def coloring(x):
    if x==0:
        return 'red' # sinker
    if x==1:
        return 'blue' # slider
    if x==2:
        return 'green' # changeup
    if x==3:
        return 'black' # curve
    if x==4:
        return 'yellow' # fastball
    if x==5:
        return 'brown' #

def coloring2(x):
    if x=='Fastball':
        return 'red'
    if x=='Slider':
        return 'darkgreen'
    if x=='Curveball':
        return 'orange'
    if x=='ChangeUp':
        return 'blue'
    if x=='Splitter':
        return 'brown'
    if x=='Cutter':
        return 'lightgreen'
    if x=='Sinker':
        return 'purple'
    if x=='Knuckleball':
        return 'gray'

fig, ax = plt.subplots(1, figsize=(10,10), constrained_layout=True)
ax.legend()
for p in df['ClusterName'].unique().tolist():
    temp = df[df['ClusterName'] == p]
    ax.scatter(temp['RelSpeed'], temp['InducedVertBreak'], color=coloring2(p), s=500, alpha=0.2, label=p)
ax.set_xlim(60,160)
ax.set_ylim(-60,60)
ax.set_xlabel('Speed')
ax.set_ylabel('Vertical')
ax.grid('on')

fig, ax = plt.subplots(1, figsize=(10,10), constrained_layout=True)
ax.legend()
for p in df['ClusterName'].unique().tolist():
    temp = df[df['ClusterName'] == p]
    ax.scatter(temp['HorzBreak'], temp['RelSpeed'], color=coloring2(p), s=500, alpha=0.2, label=p)
ax.set_xlim(-60,60)
ax.set_ylim(160,90)
ax.set_ylabel('Speed')
ax.set_xlabel('Horizontal')
ax.grid('on')

fig, ax = plt.subplots(1, figsize=(10,10), constrained_layout=True)
ax.grid('on')
ax.plot([0,0], [-60,60], color='black', linewidth=2)
ax.plot([-60,60], [0,0], color='black', linewidth=2)
for p in df['ClusterName'].unique().tolist():
    temp = df[df['ClusterName'] == p]
    ax.scatter(temp['HorzBreak'], temp['InducedVertBreak'], color=coloring2(p), s=500, alpha=0.2, label=p)
ax.set_xlim(-60,60)
ax.set_ylim(-60,60)
ax.set_xlabel('Horizontal')
ax.set_ylabel('Vertical')
ax.set_title("Daniel Camarena. 무브먼트 차트 (투수 시점)\n", fontsize=30)
ax.legend()
plt.savefig('C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\외인 최종\\Camarena, Daniel.png')