# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 13:48:07 2021

@author: LIONS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv", index_col=None, encoding='cp949')
df = df[df.Level == 'KBO']
df['Number'] = 1

ID = 77446
pit = df[df.kbo_pid == ID]
name = pit['PitName1'].iloc[0]

ptype1 = pit.pivot_table(index='TaggedPitchType', values=['RelSpeed', 'Extension', 'RelHeight', 'RelSide', 'VertBreak', 'HorzBreak', 'InducedVertBreak'], aggfunc='mean')
ptype2 = pit.pivot_table(index='TaggedPitchType', values='Number', aggfunc='sum')
ptype = pd.concat([ptype1, ptype2], axis=1)
ptype['ThrowRate'] = ptype['Number']/len(pit.index)
ind = ptype[ptype['ThrowRate']<0.01].index
ptype.drop(ind, inplace=True)
ptype.sort_values(by='Number', ascending=False, inplace=True)
ptlist = ptype.index.tolist()

dif = pd.DataFrame(index=ptlist, columns=['VBvsAvg', 'VBvsAvg%', 'IVBvsAvg', 'IVBvsAvg%', 'HBvsAvg', 'HBvsAvg%'])

for pt in ptlist:
    VB = ptype['VertBreak'].loc[pt]
    IVB = ptype['InducedVertBreak'].loc[pt]
    HB = ptype['HorzBreak'].loc[pt]
    
    RS = ptype['RelSpeed'].loc[pt]
    ET = ptype['Extension'].loc[pt]
    RH = ptype['RelHeight'].loc[pt]
    RSd = ptype['RelSide'].loc[pt]
    
    maskRS = (df['RelSpeed']>RS-3.2)&(df['RelSpeed']<RS+3.2)
    maskET = (df['Extension']>ET-0.1524)&(df['Extension']<ET+0.1524)
    maskRH = (df['RelHeight']>RH-0.1524)&(df['RelHeight']<RH+0.1524)
    maskRSd = (df['RelSide']>RSd-0.1524)&(df['RelSide']<RSd+0.1524)
    
    temp = df[(df['AutoPitchType']==pt) & maskRS & maskET & maskRH & maskRSd]
    VBm = temp[temp['VertBreak'] < VB]
    IVBm = temp[temp['InducedVertBreak'] < IVB]
    HBm = temp[temp['HorzBreak'] < HB]
    
    dif['VBvsAvg'].loc[pt] = VB - temp['VertBreak'].mean()
    dif['IVBvsAvg'].loc[pt] = IVB - temp['InducedVertBreak'].mean()
    dif['HBvsAvg'].loc[pt] = HB - temp['HorzBreak'].mean()
    
    dif['VBvsAvg%'].loc[pt] = 100*len(VBm.index)/(len(temp.index)-1) - 50
    dif['IVBvsAvg%'].loc[pt] = 100*len(IVBm.index)/(len(temp.index)-1) - 50
    dif['HBvsAvg%'].loc[pt] = 100*len(HBm.index)/(len(temp.index)-1) - 50

dif.to_csv("C:\\Users\\LIONS\\.spyder-py3\\9월 2주\\무브먼트 비교\\%s(%s) 무브먼트 비교.csv" % (name, ID), encoding='cp949')

fig, ax = plt.subplots(1, figsize=(10,10), constrained_layout=True)

def color(rate):
    if rate<0:
        return 'blue'
    else:
        return 'red'

def alpha(rate):
    return np.abs(rate)/100

ax.plot([0,140], [0,0], linewidth=3, color='black')
ax.plot([0,140], [7,7], linewidth=3, color='black')
ax.plot([0,0], [0,7], linewidth=3, color='black')
for i in range(4):
    ax.plot([20+40*i, 20+40*i], [0,7], linewidth=3, color='black')
for i in range(3):
    ax.plot([40+40*i, 40+40*i], [0,7], linewidth=1, color='grey')

ax.annotate("구종", xy=(10,3.5), va='center', ha='center', fontsize=20)
ax.annotate("V-mov\n편차", xy=(30,3.5), va='center', ha='center', fontsize=20)
ax.annotate("V-mov\n분포", xy=(50,3.5), va='center', ha='center', fontsize=20)
ax.annotate("조정 V-mov\n편차", xy=(70,3.5), va='center', ha='center', fontsize=15)
ax.annotate("조정 V-mov\n분포", xy=(90,3.5), va='center', ha='center', fontsize=15)
ax.annotate("H-mov\n편차", xy=(110,3.5), va='center', ha='center', fontsize=20)
ax.annotate("H-mov\n분포", xy=(130,3.5), va='center', ha='center', fontsize=20)

h = -10
for pt in ptlist:
    ax.plot([0,140], [h,h], linewidth=3, color='black')
    ax.plot([0,0], [h, h+10], linewidth=3, color='black')
    for i in range(4):
        ax.plot([20+40*i, 20+40*i], [h, h+10], linewidth=3, color='black')
    for i in range(3):
        ax.plot([40+40*i, 40+40*i], [h, h+10], linewidth=1, color='grey')
        ax.annotate(pt, xy=(10,h+5), va='center', ha='center', fontsize=15)
        ax.annotate("%.1f"%dif['VBvsAvg'].loc[pt], xy=(30,h+5), va='center', ha='center', fontsize=20)
        ax.annotate("%.1f%%"%dif['VBvsAvg%'].loc[pt], xy=(50,h+5), va='center', ha='center', fontsize=20)
        plt.fill_between([40,60], h, h+10, color=color(dif['VBvsAvg%'].loc[pt]), alpha=alpha(dif['VBvsAvg%'].loc[pt]))
        ax.annotate("%.1f"%dif['IVBvsAvg'].loc[pt], xy=(70,h+5), va='center', ha='center', fontsize=20)
        ax.annotate("%.1f%%"%dif['IVBvsAvg%'].loc[pt], xy=(90,h+5), va='center', ha='center', fontsize=20)
        plt.fill_between([80,100], h, h+10, color=color(dif['IVBvsAvg%'].loc[pt]), alpha=alpha(dif['IVBvsAvg%'].loc[pt]))
        ax.annotate("%.1f"%dif['HBvsAvg'].loc[pt], xy=(110,h+5), va='center', ha='center', fontsize=20)
        ax.annotate("%.1f%%"%dif['HBvsAvg%'].loc[pt], xy=(130,h+5), va='center', ha='center', fontsize=20)
        plt.fill_between([120,140], h, h+10, color=color(dif['HBvsAvg%'].loc[pt]), alpha=alpha(dif['HBvsAvg%'].loc[pt]))
        
    h -= 10

ax.axis('off')
ax.set_ylim(-60,10)
ax.set_title("%s 구종 별 무브먼트 비교" % name, fontsize=30)
plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\9월 2주\\무브먼트 비교\\%s 구종 별 무브먼트 비교.png" % name, dpi=100)