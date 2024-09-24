# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 14:51:56 2021

@author: LIONS
"""

import matplotlib.pyplot as plt
import pandas as pd

from matplotlib import font_manager, rc
import matplotlib

matplotlib.rcParams['axes.unicode_minus'] = False

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv", index_col=False, encoding='cp949')
df.dropna(subset=['RelSpeed'], inplace=True)
dfAll = df[df.PitcherTeam == 'MIN_SAM']

df1 = df[df.Level == 'KBO']
maskH = (df1.PlateLocSide>-0.1693)&(df1.PlateLocSide<0.1693)&(df1.PlateLocHeight>0.5588)&(df1.PlateLocHeight<0.9652)
maskS = (df1.PlateLocSide>-0.3387)&(df1.PlateLocSide<0.3387)&(df1.PlateLocHeight>0.3556)&(df1.PlateLocHeight<1.1684)
maskC = (df1.PlateLocSide>-0.508)&(df1.PlateLocSide<0.508)&(df1.PlateLocHeight>0.1524)&(df1.PlateLocHeight<1.3716)

dfH = df1[maskH]
dfS = df1[maskS & ~maskH]
dfC = df1[maskC & ~maskS]
dfW = df1[~maskC]

Hmean = len(dfH.index)/len(df1.index)
Smean = len(dfS.index)/len(df1.index)
Cmean = len(dfC.index)/len(df1.index)
Wmean = len(dfW.index)/len(df1.index)

PitID = dfAll[['kbo_pid', 'PitName1']]
PitID.drop_duplicates(subset=['kbo_pid'], inplace=True)
PitID.set_index('kbo_pid', inplace=True)
PitID['PitName1'].loc[51454] = '이승현(좌)'
PitID['PitName1'].loc[60146] = '이승현(우)'
IDlist = PitID.index.tolist()

for ID in IDlist:
    name = PitID.PitName1.loc[ID]
    
    df = dfAll[dfAll.kbo_pid == ID]
    maskH = (df.PlateLocSide>-0.1693)&(df.PlateLocSide<0.1693)&(df.PlateLocHeight>0.5588)&(df.PlateLocHeight<0.9652)
    maskS = (df.PlateLocSide>-0.3387)&(df.PlateLocSide<0.3387)&(df.PlateLocHeight>0.3556)&(df.PlateLocHeight<1.1684)
    maskC = (df.PlateLocSide>-0.508)&(df.PlateLocSide<0.508)&(df.PlateLocHeight>0.1524)&(df.PlateLocHeight<1.3716)
    
    dfH = df[maskH]
    dfS = df[maskS & ~maskH]
    dfC = df[maskC & ~maskS]
    dfW = df[~maskC]
    
    Hrate = len(dfH.index)/len(df.index)
    Srate = len(dfS.index)/len(df.index)
    Crate = len(dfC.index)/len(df.index)
    Wrate = len(dfW.index)/len(df.index)
    
    fig, ax = plt.subplots(1, figsize=(10,12), constrained_layout=True)
    
    ax.plot([-0.254,0.254], [0.4572,0.4572], linewidth=3, color='darkgreen', ls='--')
    ax.plot([-0.254,-0.1], [1.0668,1.0668], linewidth=3, color='darkgreen', ls='--')
    ax.plot([0.1,0.254], [1.0668,1.0668], linewidth=3, color='darkgreen', ls='--')
    ax.plot([-0.254,-0.254], [0.4572,1.0668], linewidth=3, color='darkgreen', ls='--')
    ax.plot([0.254,0.254], [0.4572,1.0668], linewidth=3, color='darkgreen', ls='--')
    ax.plot([-0.508, -0.38], [0.06, 0.06], linewidth=3, color='darkgreen', ls='--')
    plt.annotate(": 스트라이크 존", xy=(-0.36,0.06), fontsize=25, va='center', ha='left')
    plt.annotate("(괄호 안은 1군 평균)", xy=(-0.508,-0.01), fontsize=25, va='center', ha='left')
    
    ax.plot([-0.508/3,0.508/3], [0.5588,0.5588], linewidth=1, color='black')
    ax.plot([-0.508/3,0.508/3], [0.9652,0.9652], linewidth=1, color='black')
    ax.plot([-0.508/3,-0.508/3], [0.5588,0.9652], linewidth=1, color='black')
    ax.plot([0.508/3,0.508/3], [0.5588,0.9652], linewidth=1, color='black')
    
    ax.plot([-1.016/3,1.016/3], [0.3556,0.3556], linewidth=1, color='black')
    ax.plot([-1.016/3,1.016/3], [1.1684,1.1684], linewidth=1, color='black')
    ax.plot([-1.016/3,-1.016/3], [0.3556,1.1684], linewidth=1, color='black')
    ax.plot([1.016/3,1.016/3], [0.3556,1.1684], linewidth=1, color='black')
    
    ax.plot([-0.508,0.508], [0.1524,0.1524], linewidth=1, color='black')
    ax.plot([-0.508,0.508], [1.3716,1.3716], linewidth=1, color='black')
    ax.plot([-0.508,-0.508], [0.1524,1.3716], linewidth=1, color='black')
    ax.plot([0.508,0.508], [0.1524,1.3716], linewidth=1, color='black')
    
    plt.fill_between([-0.508/3,0.508/3], 0.9652, 0.5588, color='purple', alpha=Hrate)
    
    plt.fill_between([-1.016/3,-0.508/3], 1.1684, 0.3556, color='pink', alpha=Srate)
    plt.fill_between([0.508/3,1.016/3], 1.1684, 0.3556, color='pink', alpha=Srate)
    plt.fill_between([-0.508/3,0.508/3], 1.1684, 0.9652, color='pink', alpha=Srate)
    plt.fill_between([-0.508/3,0.508/3], 0.5588, 0.3556, color='pink', alpha=Srate)
    
    plt.fill_between([-0.508,-1.016/3], 1.3716, 0.1524, color='yellow', alpha=Crate)
    plt.fill_between([1.016/3,0.508], 1.3716, 0.1524, color='yellow', alpha=Crate)
    plt.fill_between([-1.016/3,1.016/3], 1.3716, 1.1684, color='yellow', alpha=Crate)
    plt.fill_between([-1.016/3,1.016/3], 0.3556, 0.1524, color='yellow', alpha=Crate)
    
    plt.fill_between([-2.032/3,-0.508], 1.5748, -0.0508, color='grey', alpha=Wrate)
    plt.fill_between([0.508,2.032/3], 1.5748, -0.0508, color='grey', alpha=Wrate)
    plt.fill_between([-0.508,0.508], 1.5748, 1.3716, color='grey', alpha=Wrate)
    plt.fill_between([-0.508,0.508], 0.1524, -0.0508, color='grey', alpha=Wrate)
    
    plt.annotate("%.1f%%"%(100*Hrate), xy=(0, 0.762), fontsize=30, va='bottom', ha='center')
    plt.annotate("(%.1f%%)"%(100*Hmean), xy=(0, 0.762), fontsize=25, va='top', ha='center')
    plt.annotate("%.1f%%"%(100*Srate), xy=(0, 1.0668), fontsize=30, va='bottom', ha='center')
    plt.annotate("(%.1f%%)"%(100*Smean), xy=(0, 1.0668), fontsize=25, va='top', ha='center')
    plt.annotate("%.1f%%"%(100*Crate), xy=(0, 1.27), fontsize=30, va='bottom', ha='center')
    plt.annotate("(%.1f%%)"%(100*Cmean), xy=(0, 1.27), fontsize=25, va='top', ha='center')
    plt.annotate("%.1f%%"%(100*Wrate), xy=(0, 1.4732), fontsize=30, va='bottom', ha='center')
    plt.annotate("(%.1f%%)"%(100*Wmean), xy=(0, 1.4732), fontsize=25, va='top', ha='center')
    
    ax.axis('off')
    ax.set_title("\n%s 로케이션 구사율" % name, fontsize=30)
    plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\7월 5주\\로케이션 분포\\%s 로케이션 분포.png" % name)