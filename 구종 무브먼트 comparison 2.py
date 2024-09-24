# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 12:34:27 2021

@author: LIONS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib

matplotlib.rcParams['axes.unicode_minus'] = False

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv", index_col=None, encoding='cp949')
df = df[df.Level == 'KBO']
df['Number'] = 1

ptable1 = df.pivot_table(index=['kbo_pid', 'TaggedPitchType'], values=['RelSpeed', 'Extension', 'RelHeight', 'RelSide', 'VertBreak', 'HorzBreak', 'InducedVertBreak'], aggfunc='mean')
ptable2 = df.pivot_table(index=['kbo_pid', 'TaggedPitchType'], values='Number', aggfunc='sum')
ptable = pd.concat([ptable1, ptable2], axis=1)
ptable.dropna(subset=['Extension'], inplace=True)

ID = 50404
name = df[df['kbo_pid']==ID]['PitName1'].iloc[0]
throws = df[df['kbo_pid']==ID]['PitcherThrows'].iloc[0]

temp = ptable.loc[ID]
tot = temp['Number'].sum()
temp['ThrowRate'] = temp['Number']/tot
ind = temp[temp['ThrowRate']<0.01].index
temp.drop(ind, inplace=True)
temp.sort_values(by='Number', ascending=False, inplace=True)

plist = temp.index.tolist()

dif = pd.DataFrame(index=plist, columns=['HBvsAvg', 'HBdist', 'VBvsAvg', 'VBdist', 'IVBvsAvg', 'IVBdist'])

for pt in plist:
    VB = temp['VertBreak'].loc[pt]
    IVB = temp['InducedVertBreak'].loc[pt]
    HB = temp['HorzBreak'].loc[pt]
    
    Rsp = temp['RelSpeed'].loc[pt]
    Ext = temp['Extension'].loc[pt]
    Rht = temp['RelHeight'].loc[pt]
    Rsd = temp['RelSide'].loc[pt]
    
    maskRsp = (ptable['RelSpeed']>Rsp-3.2)&(ptable['RelSpeed']<Rsp+3.2)
    maskExt = (ptable['Extension']>Ext-0.1524)&(ptable['Extension']<Ext+0.1524)
    maskRht = (ptable['RelHeight']>Rht-0.1524)&(ptable['RelHeight']<Rht+0.1524)
    maskRsd = (ptable['RelSide']>Rsd-0.1524)&(ptable['RelSide']<Rsd+0.1524)
    
    comp = ptable[maskRsp & maskExt & maskRht & maskRsd]
    VBm = comp['VertBreak'].mean()
    IVBm = comp['InducedVertBreak'].mean()
    HBm = comp['HorzBreak'].mean()
    VBstd = np.std(comp['VertBreak'])
    IVBstd = np.std(comp['InducedVertBreak'])
    HBstd = np.std(comp['HorzBreak'])
    
    dif['VBvsAvg'].loc[pt] = VB - VBm
    dif['IVBvsAvg'].loc[pt] = IVB - IVBm
    dif['HBvsAvg'].loc[pt] = HB - HBm
    
    VBl = comp[comp['VertBreak']<=VB]
    IVBl = comp[comp['InducedVertBreak']<=IVB]
    HBl = comp[comp['HorzBreak']<=HB]
    
    if len(comp.index)>1:
        dif['VBdist'].loc[pt] = len(VBl.index)/(len(comp.index)-1)
        dif['IVBdist'].loc[pt] = len(IVBl.index)/(len(comp.index)-1)
        dif['HBdist'].loc[pt] = len(HBl.index)/(len(comp.index)-1)
    else:
        dif['VBdist'].loc[pt] = len(VBl.index)
        dif['IVBdist'].loc[pt] = len(IVBl.index)
        dif['HBdist'].loc[pt] = len(HBl.index)

fig, ax = plt.subplots(1, figsize=(10,10), constrained_layout=True)
ax.plot([0,140], [0,0], linewidth=1.5, color='black')
ax.plot([0,140], [0.3,0.3], linewidth=1.5, color='black')
ax.plot([0,140], [7,7], linewidth=3, color='black')
ax.plot([0,0], [0,7], linewidth=3, color='black')
for i in range(4):
    ax.plot([20+40*i, 20+40*i], [0,7], linewidth=3, color='black')
for i in range(3):
    ax.plot([40+40*i, 40+40*i], [0,7], linewidth=1, color='grey')

ax.annotate("구종", xy=(10,3.5), va='center', ha='center', fontsize=20)
ax.annotate("평균 대비\nH-mov", xy=(30,3.5), va='center', ha='center', fontsize=20)
ax.annotate("H-mov\n분포", xy=(50,3.5), va='center', ha='center', fontsize=20)
ax.annotate("평균 대비\nV-mov", xy=(70,3.5), va='center', ha='center', fontsize=20)
ax.annotate("V-mov\n분포", xy=(90,3.5), va='center', ha='center', fontsize=20)
ax.annotate("평균 대비\n조정 V-mov", xy=(110,3.5), va='center', ha='center', fontsize=15)
ax.annotate("조정 V-mov\n분포", xy=(130,3.5), va='center', ha='center', fontsize=15)

h = 0

def color(sg):
    if sg>0.5:
        return 'red'
    else:
        return 'blue'

for pt in plist:
    ax.plot([0,140], [h-5,h-5], linewidth=3, color='black')
    ax.plot([0,0], [h-5, h], linewidth=3, color='black')
    for i in range(4):
        ax.plot([20+40*i, 20+40*i], [h-5, h], linewidth=3, color='black')
    for i in range(3):
        ax.plot([40+40*i, 40+40*i], [h-5, h], linewidth=1, color='grey')
    ax.annotate(pt, xy=(10,h-2.5), va='center', ha='center', fontsize=15)
    ax.annotate("%.1f"%dif['HBvsAvg'].loc[pt], xy=(30,h-2.5), va='center', ha='center', fontsize=20)
    ax.annotate("%d%%"%(100*dif['HBdist'].loc[pt]), xy=(50,h-2.5), va='center', ha='center', fontsize=20)
    plt.fill_between([40,60], h-5, h, color=color(dif['HBdist'].loc[pt]), alpha=np.abs(dif['HBdist'].loc[pt]-0.5))
    ax.annotate("%.1f"%dif['VBvsAvg'].loc[pt], xy=(70,h-2.5), va='center', ha='center', fontsize=20)
    ax.annotate("%d%%"%(100*dif['VBdist'].loc[pt]), xy=(90,h-2.5), va='center', ha='center', fontsize=20)
    plt.fill_between([80,100], h-5, h, color=color(dif['VBdist'].loc[pt]), alpha=np.abs(dif['VBdist'].loc[pt]-0.5))
    ax.annotate("%.1f"%dif['IVBvsAvg'].loc[pt], xy=(110,h-2.5), va='center', ha='center', fontsize=20)
    ax.annotate("%d%%"%(100*dif['IVBdist'].loc[pt]), xy=(130,h-2.5), va='center', ha='center', fontsize=20)
    plt.fill_between([120,140], h-5, h, color=color(dif['IVBdist'].loc[pt]), alpha=np.abs(dif['IVBdist'].loc[pt]-0.5))
    
    h -= 5

ax.set_title("\n%s 구종 별 무브먼트 비교" % name, fontsize=30)
ax.axis('off')
ax.set_ylim(-50,10)
plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\9월 3주\\%s 구종 별 대조군 비교.png" % name)