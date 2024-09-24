# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 10:47:19 2021

@author: LIONS
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', index_col=False, encoding='cp949')

BSlist = ['Left', 'Right']

df = df[df.PitchCall == 'StrikeCalled']

for BS in BSlist:
    dfs = df[df.BatterSide == BS]
    
    fig, ax = plt.subplots(1, figsize=(7,10), constrained_layout=True)
    ax.set_xlim(-0.4, 0.4)
    ax.set_ylim(0.3, 1.2)
    
    ax.plot([0.254,0.254], [0.4572,1.0668], linewidth=3, color='black')
    ax.plot([-0.254,-0.254], [0.4572,1.0668], linewidth=3, color='black')
    ax.plot([-0.254,0.254], [0.4572,0.4572], linewidth=3, color='black')
    ax.plot([-0.254,0.254], [1.0668,1.0668], linewidth=3, color='black')
    ax.plot([-0.085,-0.085], [0.4572,1.0668], linewidth=1, color='black', ls='--')
    ax.plot([0.085,0.085], [0.4572,1.0668], linewidth=1, color='black', ls='--')
    ax.plot([-0.254,0.254], [0.6604,0.6604], linewidth=1, color='black', ls='--')
    ax.plot([-0.254,0.254], [0.8636,0.8636], linewidth=1, color='black', ls='--')
    ax.plot([-0.339,0.339], [0.3556,0.3556], linewidth=1, color='black', ls='--')
    ax.plot([-0.339,0.339], [1.1684,1.1684], linewidth=1, color='black', ls='--')
    ax.plot([-0.339,-0.339], [0.3556,1.1684], linewidth=1, color='black', ls='--')
    ax.plot([0.339,0.339], [0.3556,1.1684], linewidth=1, color='black', ls='--')
    ax.plot([0,0], [1.0668,1.1684], linewidth=1, color='black', ls='--')
    ax.plot([0,0], [0.3556,0.4572], linewidth=1, color='black', ls='--')
    ax.plot([-0.339,-0.254], [0.762,0.762], linewidth=1, color='black', ls='--')
    ax.plot([0.254,0.339], [0.762,0.762], linewidth=1, color='black', ls='--')
    
    ax.scatter(dfs.PlateLocSide, dfs.PlateLocHeight, c='red', alpha=0.1)
    
    if BS == 'Left':
        side = '좌타자'
    else:
        side = '우타자'
    
    ax.axis('off')
    plt.title("\n%s 스트라이크 존 (투수 시점)\n" % side, fontsize = 25)