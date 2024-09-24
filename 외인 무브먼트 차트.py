# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:11:18 2021

@author: LIONS
"""

import pandas as pd
import os
import matplotlib.pyplot as plt

filelist = os.listdir('C:\\Users\\LIONS\\.spyder-py3\\9월 3주\\외인 구종분류 최종')
namelist = []
for i in range(len(filelist)):
    if i%2 == 0:
        namelist.append(filelist[i])

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

for name in namelist:
    df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\9월 3주\\외인 구종분류 최종\\%s' % name, index_col=False, encoding='cp949')
    fig, ax = plt.subplots(1, figsize=(10,12), constrained_layout=True)
    
    for p in df['ClusterName'].unique().tolist():
        temp = df[df['ClusterName'] == p]
        ax.scatter(temp['HorzBreak'], temp['InducedVertBreak'], color=coloring2(p), s=500, alpha=0.2, label=p)
    ax.set_title(name[:-4]+"\n", fontsize=30)
    ax.set_xlim(-60,60)
    ax.set_ylim(-60,60)
    ax.set_xlabel('Horizontal')
    ax.set_ylabel('Vertical')
    ax.legend()
    ax.grid('on')
    
    plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\외인\\%s.png"%name[:-4])