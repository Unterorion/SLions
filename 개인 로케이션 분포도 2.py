# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 09:28:41 2021

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

df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\7월 4주\\전체 투수 구종분류.csv', index_col=False, encoding='cp949')
df = df.dropna(subset = ['RelSpeed', 'ClusterName'])

def RevLocSide(PlateLocSide):
    if PlateLocSide < -0.4:
        return -0.4
    elif PlateLocSide > 0.4:
        return 0.4
    else:
        return PlateLocSide

def RevLocHeight(PlateLocHeight):
    if PlateLocHeight < 0.3:
        return 0.3
    elif PlateLocHeight > 1.2:
        return 1.2
    else:
        return PlateLocHeight

df['RevLocSide'] = None
df['RevLocHeight'] = None
df['RevLocSide'] = df['PlateLocSide'].apply(RevLocSide)
df['RevLocHeight'] = df['PlateLocHeight'].apply(RevLocHeight)

dfm = df[df['PitcherTeam']=='MIN_SAM']

idmap = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\7월 5주\\투수.csv', index_col=False, encoding='cp949')
idmap = idmap.set_index('PitcherId')

pitIDlist = dfm['PitcherId'].unique().tolist()
ID = 64498
cID = 67603
dfindi = dfm[dfm['PitcherId']==ID]
dfindic = df[df['PitcherId']==cID]

ptypelist = dfindi['ClusterName'].unique().tolist()

BSlist = ['Left', 'Right']

for ptype in ptypelist:
    dfip = dfindi[dfindi.ClusterName == ptype]
    dfcp = dfindic[dfindic.ClusterName == ptype]
    for BS in BSlist:
        dfis = dfip[dfip.BatterSide == BS]
        dfcs = dfcp[dfcp.BatterSide == BS]
        for dfi in [dfis, dfcs]:
            if len(dfi.index) > 0:
                name = dfi['PitName1'].iloc[0]
                
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
                
                ax.scatter(dfi['RevLocSide'], dfi['RevLocHeight'], c='red', marker='o', s=500)
                
                if BS == 'Left':
                    bside = '좌타자'
                else:
                    bside = '우타자'
                
                if name == '이승현':
                    if ID == 51454:
                        name = '이승현(좌)'
                    elif ID == 60146:
                        name = '이승현(우)'
                
                ax.grid('off')
                ax.axis('off')
                plt.title("\n%s %s 상대 %s 로케이션 분포\n" % (name, bside, ptype), fontsize=20)
                #plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\7월 5주\\로케이션 분포\\%s %s 상대 로케이션 분포.png" % (name, bside))

ctypelist = dfindic['ClusterName'].unique().tolist()
nctypelist = []
for ptype in ptypelist:
    if ptype in ctypelist:
        ctypelist.remove(ptype)

for ctype in ctypelist:
    dfc = dfindic[dfindic.ClusterName == ctype]
    for BS in BSlist:
        dfs = dfc[dfc.BatterSide == BS]
        if len(dfs.index) > 0:
            name = dfs['PitName1'].iloc[0]
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
            
            ax.scatter(dfs['RevLocSide'], dfs['RevLocHeight'], c='red', marker='o', s=500)
            
            if BS == 'Left':
                bside = '좌타자'
            else:
                bside = '우타자'
            
            if name == '이승현':
                if ID == 51454:
                    name = '이승현(좌)'
                elif ID == 60146:
                    name = '이승현(우)'
            
            ax.grid('off')
            ax.axis('off')
            plt.title("\n%s %s 상대 %s 로케이션 분포\n" % (name, bside, ctype), fontsize=20)
            #plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\7월 5주\\로케이션 분포\\%s %s 상대 로케이션 분포.png" % (name, bside))
            