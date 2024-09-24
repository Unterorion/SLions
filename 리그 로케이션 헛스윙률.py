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
df = df[df.PitcherThrows == 'Left']

maskSw = (df.PitchCall == 'InPlay') | (df.PitchCall == 'FoulBall') | (df.PitchCall == 'StrikeSwinging')
maskWh = (df.PitchCall == 'StrikeSwinging')
dfSw = df[maskSw]
dfWh = df[maskWh]
LgWrate = 100*len(dfWh.index)/len(dfSw.index)

print("전체 헛스윙률: %.1f%%" % LgWrate)

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
    
    maskLgS = (dfi.PitchCall == 'StrikeSwinging') | (dfi.PitchCall == 'FoulBall') | (dfi.PitchCall == 'InPlay')
    maskLgW = (dfi.PitchCall == 'StrikeSwinging')
    dfLgS = dfi[maskLgS]
    dfLgW = dfi[maskLgW]
    
    if len(dfLgS.index) > 0:
        typeLgWrate = 100*len(dfLgW.index)/len(dfLgS.index)
    else:
        typeLgWrate = 0
    
    Wratelist = []
    for dfp in [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13]:
        maskS = (dfp.PitchCall == 'StrikeSwinging') | (dfp.PitchCall == 'FoulBall') | (dfp.PitchCall == 'InPlay')
        maskW = (dfp.PitchCall == 'StrikeSwinging')
        dfS = dfp[maskS]
        dfW = dfp[maskW]
        if len(dfS.index) == 0:
            Wrate = np.nan
        else:
            Wrate = 100*len(dfW.index)/len(dfS.index)
        Wratelist.append(Wrate)
    
    def fill_color(rate):
        global LgWrate
        if rate>LgWrate:
            return 'red'
        else:
            return 'blue'
    
    def fill_alpha(rate):
        global LgWrate
        alpha = np.abs(rate - LgWrate)/100
        return alpha
    
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
    
    plt.fill_between(x1, 0.8636, 1.0668, color=fill_color(Wratelist[0]), alpha=fill_alpha(Wratelist[0]))
    plt.fill_between(x2, 0.8636, 1.0668, color=fill_color(Wratelist[1]), alpha=fill_alpha(Wratelist[1]))
    plt.fill_between(x3, 0.8636, 1.0668, color=fill_color(Wratelist[2]), alpha=fill_alpha(Wratelist[2]))
    plt.fill_between(x1, 0.8636, 0.6604, color=fill_color(Wratelist[3]), alpha=fill_alpha(Wratelist[3]))
    plt.fill_between(x2, 0.8636, 0.6604, color=fill_color(Wratelist[4]), alpha=fill_alpha(Wratelist[4]))
    plt.fill_between(x3, 0.8636, 0.6604, color=fill_color(Wratelist[5]), alpha=fill_alpha(Wratelist[5]))
    plt.fill_between(x1, 0.4572, 0.6604, color=fill_color(Wratelist[6]), alpha=fill_alpha(Wratelist[6]))
    plt.fill_between(x2, 0.4572, 0.6604, color=fill_color(Wratelist[7]), alpha=fill_alpha(Wratelist[7]))
    plt.fill_between(x3, 0.4572, 0.6604, color=fill_color(Wratelist[8]), alpha=fill_alpha(Wratelist[8]))
    
    plt.fill_between(xo1, 0.762, 1.0688, color=fill_color(Wratelist[10]), alpha=fill_alpha(Wratelist[10]))
    plt.fill_between(xo2, 1.0668, 1.1684, color=fill_color(Wratelist[10]), alpha=fill_alpha(Wratelist[10]))
    plt.fill_between(xo3, 1.0668, 1.1684, color=fill_color(Wratelist[9]), alpha=fill_alpha(Wratelist[9]))
    plt.fill_between(xo4, 0.762, 1.0668, color=fill_color(Wratelist[9]), alpha=fill_alpha(Wratelist[9]))
    plt.fill_between(xo1, 0.762, 0.4572, color=fill_color(Wratelist[11]), alpha=fill_alpha(Wratelist[11]))
    plt.fill_between(xo2, 0.3556, 0.4572, color=fill_color(Wratelist[11]), alpha=fill_alpha(Wratelist[11]))
    plt.fill_between(xo3, 0.3556, 0.4572, color=fill_color(Wratelist[12]), alpha=fill_alpha(Wratelist[12]))
    plt.fill_between(xo4, 0.762, 0.4572, color=fill_color(Wratelist[12]), alpha=fill_alpha(Wratelist[12]))
    
    plt.text(-0.2, 0.95, "%.1f%%" % Wratelist[0], size=20)
    plt.text(-0.031, 0.95, "%.1f%%" % Wratelist[1], size=20)
    plt.text(0.138, 0.95, "%.1f%%" % Wratelist[2], size=20)
    plt.text(-0.2, 0.7468, "%.1f%%" % Wratelist[3], size=20)
    plt.text(-0.031, 0.7468, "%.1f%%" % Wratelist[4], size=20)
    plt.text(0.138, 0.7468, "%.1f%%" % Wratelist[5], size=20)
    plt.text(-0.2, 0.5436, "%.1f%%" % Wratelist[6], size=20)
    plt.text(-0.031, 0.5436, "%.1f%%" % Wratelist[7], size=20)
    plt.text(0.138, 0.5436, "%.1f%%" % Wratelist[8], size=20)
    
    plt.text(0.23, 1.1, "%.1f%%" % Wratelist[9], size=20)
    plt.text(-0.3, 1.1, "%.1f%%" % Wratelist[10], size=20)
    plt.text(-0.3, 0.4, "%.1f%%" % Wratelist[11], size=20)
    plt.text(0.23, 0.4, "%.1f%%" % Wratelist[12], size=20)

    ax.grid('off')
    ax.axis('off')
    plt.text(-0.339, 0.3, "%s 전체 헛스윙률 %.1f%%" % (ptype, typeLgWrate), size=20)
    plt.title("\n%s 로케이션 별 헛스윙률\n(우투수/좌타자)" % ptype, fontsize=30)
    plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\7월 5주\\로케이션 별 헛스윙률\\우투수 %s 로케이션 별 좌타 헛스윙률.png" % ptype)