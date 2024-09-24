# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 11:43:10 2021

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
df = df.dropna(subset=['ClusterName'])
ptypelist = df['ClusterName'].unique().tolist()
df = df[df.BatterSide == 'Right']
df = df[df.PitcherThrows == 'Right']
df = df[df.PitchCall == 'InPlay']

def TB(PR):
    if PR == 'Single':
        return 1
    elif PR == 'Double':
        return 2
    elif PR == 'Triple':
        return 3
    elif PR == 'HomeRun':
        return 4
    else:
        return 0

df['TotalBases'] = None
df.TotalBases = df.PlayResult.apply(TB)

TBlist = df.TotalBases.tolist()
totSLG = sum(TBlist)/len(TBlist)
print("전체 타구 피장타율: %.3f" % totSLG)

def fill_color(SLG):
    global totSLG
    if SLG>totSLG:
        return 'red'
    else:
        return 'blue'
    
def fill_alpha(SLG):
    global totSLG
    alpha = np.abs(SLG - totSLG)
    return alpha

for ptype in ptypelist:
    dfi = df[df.ClusterName == ptype]
    
    mask1 = (dfi.PlateLocSide>-0.254) & (dfi.PlateLocSide<-0.085) & (dfi.PlateLocHeight>0.8636) & (dfi.PlateLocHeight<1.0668)
    mask2 = (dfi.PlateLocSide>-0.085) & (dfi.PlateLocSide<0.085) & (dfi.PlateLocHeight>0.8636) & (dfi.PlateLocHeight<1.0668)
    mask3 = (dfi.PlateLocSide>0.085) & (dfi.PlateLocSide<0.254) & (dfi.PlateLocHeight>0.8636) & (dfi.PlateLocHeight<1.0668)
    mask4 = (dfi.PlateLocSide>-0.254) & (dfi.PlateLocSide<-0.085) & (dfi.PlateLocHeight<0.8636) & (dfi.PlateLocHeight>0.6604)
    mask5 = (dfi.PlateLocSide>-0.085) & (dfi.PlateLocSide<0.085) & (dfi.PlateLocHeight<0.8636) & (dfi.PlateLocHeight>0.6604)
    mask6 = (dfi.PlateLocSide>0.085) & (dfi.PlateLocSide<0.254) & (dfi.PlateLocHeight<0.8636) & (dfi.PlateLocHeight>0.6604)
    mask7 = (dfi.PlateLocSide>-0.254) & (dfi.PlateLocSide<-0.085) & (dfi.PlateLocHeight>0.4572) & (dfi.PlateLocHeight<0.6604)
    mask8 = (dfi.PlateLocSide>-0.085) & (dfi.PlateLocSide<0.085) & (dfi.PlateLocHeight>0.4572) & (dfi.PlateLocHeight<0.6604)
    mask9 = (dfi.PlateLocSide>0.085) & (dfi.PlateLocSide<0.254) & (dfi.PlateLocHeight>0.4572) & (dfi.PlateLocHeight<0.6604)
    mask10 = ((dfi.PlateLocSide>0)&(dfi.PlateLocSide<0.339)&(dfi.PlateLocHeight>1.0668)&(dfi.PlateLocHeight<1.1684)) | ((dfi.PlateLocSide>0.254)&(dfi.PlateLocSide<0.339)&(dfi.PlateLocHeight>0.762)&(dfi.PlateLocHeight<1.1684))
    mask11 = ((dfi.PlateLocSide<0)&(dfi.PlateLocSide>-0.339)&(dfi.PlateLocHeight>1.0668)&(dfi.PlateLocHeight<1.1684)) | ((dfi.PlateLocSide<-0.254)&(dfi.PlateLocSide>-0.339)&(dfi.PlateLocHeight>0.762)&(dfi.PlateLocHeight<1.1684))
    mask12 = ((dfi.PlateLocSide<0)&(dfi.PlateLocSide>-0.339)&(dfi.PlateLocHeight>0.3556)&(dfi.PlateLocHeight<0.4572)) | ((dfi.PlateLocSide<-0.254)&(dfi.PlateLocSide>-0.339)&(dfi.PlateLocHeight>0.3556)&(dfi.PlateLocHeight<0.762))
    mask13 = ((dfi.PlateLocSide>0)&(dfi.PlateLocSide<0.339)&(dfi.PlateLocHeight>0.3556)&(dfi.PlateLocHeight<0.4572)) | ((dfi.PlateLocSide>0.254)&(dfi.PlateLocSide<0.339)&(dfi.PlateLocHeight>0.3556)&(dfi.PlateLocHeight<0.762))
    
    df1 = dfi[mask1]
    df2 = dfi[mask2]
    df3 = dfi[mask3]
    df4 = dfi[mask4]
    df5 = dfi[mask5]
    df6 = dfi[mask6]
    df7 = dfi[mask7]
    df8 = dfi[mask8]
    df9 = dfi[mask9]
    df10 = dfi[mask10]
    df11 = dfi[mask11]
    df12 = dfi[mask12]
    df13 = dfi[mask13]
    
    typeTBlist = dfi.TotalBases.tolist()
    typeSLG = sum(typeTBlist)/len(dfi.index)
    
    locSLGlist = []
    for dfp in [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13]:
        if len(dfp.index) > 0:
            locTBlist = dfp.TotalBases.tolist()
            locSLG = sum(locTBlist)/len(dfp.index)
        else:
            locSLG = np.nan
        locSLGlist.append(locSLG)
    
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
    
    x1 = np.linspace(-0.254,-0.085)
    x2 = np.linspace(-0.085,0.085)
    x3 = np.linspace(0.085,0.254)
    xo1 = np.linspace(-0.339,-0.254)
    xo2 = np.linspace(-0.339,0)
    xo3 = np.linspace(0,0.339)
    xo4 = np.linspace(0.254,0.339)
    
    plt.fill_between(x1, 0.8636, 1.0668, color=fill_color(locSLGlist[0]), alpha=fill_alpha(locSLGlist[0]))
    plt.fill_between(x2, 0.8636, 1.0668, color=fill_color(locSLGlist[1]), alpha=fill_alpha(locSLGlist[1]))
    plt.fill_between(x3, 0.8636, 1.0668, color=fill_color(locSLGlist[2]), alpha=fill_alpha(locSLGlist[2]))
    plt.fill_between(x1, 0.8636, 0.6604, color=fill_color(locSLGlist[3]), alpha=fill_alpha(locSLGlist[3]))
    plt.fill_between(x2, 0.8636, 0.6604, color=fill_color(locSLGlist[4]), alpha=fill_alpha(locSLGlist[4]))
    plt.fill_between(x3, 0.8636, 0.6604, color=fill_color(locSLGlist[5]), alpha=fill_alpha(locSLGlist[5]))
    plt.fill_between(x1, 0.4572, 0.6604, color=fill_color(locSLGlist[6]), alpha=fill_alpha(locSLGlist[6]))
    plt.fill_between(x2, 0.4572, 0.6604, color=fill_color(locSLGlist[7]), alpha=fill_alpha(locSLGlist[7]))
    plt.fill_between(x3, 0.4572, 0.6604, color=fill_color(locSLGlist[8]), alpha=fill_alpha(locSLGlist[8]))
    
    plt.fill_between(xo1, 0.762, 1.0688, color=fill_color(locSLGlist[10]), alpha=fill_alpha(locSLGlist[10]))
    plt.fill_between(xo2, 1.0668, 1.1684, color=fill_color(locSLGlist[10]), alpha=fill_alpha(locSLGlist[10]))
    plt.fill_between(xo3, 1.0668, 1.1684, color=fill_color(locSLGlist[9]), alpha=fill_alpha(locSLGlist[9]))
    plt.fill_between(xo4, 0.762, 1.0668, color=fill_color(locSLGlist[9]), alpha=fill_alpha(locSLGlist[9]))
    plt.fill_between(xo1, 0.762, 0.4572, color=fill_color(locSLGlist[11]), alpha=fill_alpha(locSLGlist[11]))
    plt.fill_between(xo2, 0.3556, 0.4572, color=fill_color(locSLGlist[11]), alpha=fill_alpha(locSLGlist[11]))
    plt.fill_between(xo3, 0.3556, 0.4572, color=fill_color(locSLGlist[12]), alpha=fill_alpha(locSLGlist[12]))
    plt.fill_between(xo4, 0.762, 0.4572, color=fill_color(locSLGlist[12]), alpha=fill_alpha(locSLGlist[12]))
    
    plt.text(-0.2, 0.95, "%.3f" % locSLGlist[0], size=20)
    plt.text(-0.031, 0.95, "%.3f" % locSLGlist[1], size=20)
    plt.text(0.138, 0.95, "%.3f" % locSLGlist[2], size=20)
    plt.text(-0.2, 0.7468, "%.3f" % locSLGlist[3], size=20)
    plt.text(-0.031, 0.7468, "%.3f" % locSLGlist[4], size=20)
    plt.text(0.138, 0.7468, "%.3f" % locSLGlist[5], size=20)
    plt.text(-0.2, 0.5436, "%.3f" % locSLGlist[6], size=20)
    plt.text(-0.031, 0.5436, "%.3f" % locSLGlist[7], size=20)
    plt.text(0.138, 0.5436, "%.3f" % locSLGlist[8], size=20)
    
    plt.text(0.23, 1.1, "%.3f" % locSLGlist[9], size=20)
    plt.text(-0.3, 1.1, "%.3f" % locSLGlist[10], size=20)
    plt.text(-0.3, 0.4, "%.3f" % locSLGlist[11], size=20)
    plt.text(0.23, 0.4, "%.3f" % locSLGlist[12], size=20)

    ax.grid('off')
    ax.axis('off')
    plt.text(-0.339, 0.3, "%s 전체 타구 피장타율 %.3f" % (ptype, typeSLG), size=20)
    plt.title("\n%s 로케이션 별 타구 피장타율\n(우투수/우타자)" % ptype, fontsize=20)
    plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\7월 5주\\로케이션 별 타구 피장타율\\우투수 %s 로케이션 별 우타자 타구 피장타율.png" % ptype)