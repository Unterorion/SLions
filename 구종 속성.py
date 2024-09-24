# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 10:51:33 2021

@author: LIONS
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv", index_col=None, encoding='cp949')
df = df[(df.Level=='KBO')&(df.PitcherThrows=='Right')]
df.dropna(subset=['RelSpeed'], inplace=True)
ptlist = df.TaggedPitchType.unique().tolist()
ptlist = ptlist[0:7]

def color(x):
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

fig, ax = plt.subplots(1, figsize=(6,6), constrained_layout=True)

for ptype in ptlist:
    temp = df[df.TaggedPitchType == ptype]
    RS = temp.RelSpeed.mean()
    SR = temp.SpinRate.mean()
    SA = temp.SpinAxis.mean()
    HM = temp.HorzBreak.mean()
    VM = temp.InducedVertBreak.mean()
    if VM > 20:
        va = 'bottom'
        ha = 'right'
    else:
        va = 'top'
        ha = 'left'
    ax.scatter(HM, VM, s=500, c=color(ptype))
    ax.annotate("RS %.1f\nSR %d\nSA %d" % (RS, SR, SA), xy=(HM, VM), ha=ha, va=va)
    print("%s(%d) speed = %.1f, spin rate = %d, axis = %d, HM = %.2f, VM = %.2f" % (ptype, len(temp.index), RS, SR, SA, HM, VM))

ax.legend(ptlist)
ax.plot([-50,50], [0,0], color='grey', ls='--')
ax.plot([0,0], [-50,50], color='grey', ls='--')
ax.set_xlim(-50, 50)
ax.set_ylim(-50, 50)
plt.savefig("C:\\Users\\LIONS\\Desktop\\참고용 이미지\\구종 속성.png")