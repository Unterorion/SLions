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
                
                rate1 = 100*len(df1.index)/len(dfi.index)
                rate2 = 100*len(df2.index)/len(dfi.index)
                rate3 = 100*len(df3.index)/len(dfi.index)
                rate4 = 100*len(df4.index)/len(dfi.index)
                rate5 = 100*len(df5.index)/len(dfi.index)
                rate6 = 100*len(df6.index)/len(dfi.index)
                rate7 = 100*len(df7.index)/len(dfi.index)
                rate8 = 100*len(df8.index)/len(dfi.index)
                rate9 = 100*len(df9.index)/len(dfi.index)
                rate10 = 100*len(df10.index)/len(dfi.index)
                rate11 = 100*len(df11.index)/len(dfi.index)
                rate12 = 100*len(df12.index)/len(dfi.index)
                rate13 = 100*len(df13.index)/len(dfi.index)
                
                Rlist = [rate1, rate2, rate3, rate4, rate5, rate6, rate7, rate8, rate9, rate10, rate11, rate12, rate13]
                rateM = sum(Rlist)/len(Rlist)
                
                def fill_color(rate):
                    global rateM
                    if rate > rateM:
                        return 'red'
                    else:
                        return 'blue'
                    
                def fill_alpha(rate):
                    global rateM
                    alpha = np.abs(rate - rateM)/100
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
                
                plt.fill_between(x1, 0.8636, 1.0668, color=fill_color(rate1), alpha=fill_alpha(rate1))
                plt.fill_between(x2, 0.8636, 1.0668, color=fill_color(rate2), alpha=fill_alpha(rate2))
                plt.fill_between(x3, 0.8636, 1.0668, color=fill_color(rate3), alpha=fill_alpha(rate3))
                plt.fill_between(x1, 0.8636, 0.6604, color=fill_color(rate4), alpha=fill_alpha(rate4))
                plt.fill_between(x2, 0.8636, 0.6604, color=fill_color(rate5), alpha=fill_alpha(rate5))
                plt.fill_between(x3, 0.8636, 0.6604, color=fill_color(rate6), alpha=fill_alpha(rate6))
                plt.fill_between(x1, 0.4572, 0.6604, color=fill_color(rate7), alpha=fill_alpha(rate7))
                plt.fill_between(x2, 0.4572, 0.6604, color=fill_color(rate8), alpha=fill_alpha(rate8))
                plt.fill_between(x3, 0.4572, 0.6604, color=fill_color(rate9), alpha=fill_alpha(rate9))
                
                plt.fill_between(xo1, 0.762, 1.0688, color=fill_color(rate11), alpha=fill_alpha(rate11))
                plt.fill_between(xo2, 1.0668, 1.1684, color=fill_color(rate11), alpha=fill_alpha(rate11))
                plt.fill_between(xo3, 1.0668, 1.1684, color=fill_color(rate10), alpha=fill_alpha(rate10))
                plt.fill_between(xo4, 0.762, 1.0668, color=fill_color(rate10), alpha=fill_alpha(rate10))
                plt.fill_between(xo1, 0.762, 0.4572, color=fill_color(rate12), alpha=fill_alpha(rate12))
                plt.fill_between(xo2, 0.3556, 0.4572, color=fill_color(rate12), alpha=fill_alpha(rate12))
                plt.fill_between(xo3, 0.3556, 0.4572, color=fill_color(rate13), alpha=fill_alpha(rate13))
                plt.fill_between(xo4, 0.762, 0.4572, color=fill_color(rate13), alpha=fill_alpha(rate13))
                
                if BS == 'Left':
                    bside = '좌타자'
                else:
                    bside = '우타자'
                
                if name == '이승현':
                    if ID == 51454:
                        name = '이승현(좌)'
                    elif ID == 60146:
                        name = '이승현(우)'
                    
                plt.text(-0.2, 0.95, "%.1f%%" % rate1, size=20)
                plt.text(-0.031, 0.95, "%.1f%%" % rate2, size=20)
                plt.text(0.138, 0.95, "%.1f%%" % rate3, size=20)
                plt.text(-0.2, 0.7468, "%.1f%%" % rate4, size=20)
                plt.text(-0.031, 0.7468, "%.1f%%" % rate5, size=20)
                plt.text(0.138, 0.7468, "%.1f%%" % rate6, size=20)
                plt.text(-0.2, 0.5436, "%.1f%%" % rate7, size=20)
                plt.text(-0.031, 0.5436, "%.1f%%" % rate8, size=20)
                plt.text(0.138, 0.5436, "%.1f%%" % rate9, size=20)
                
                plt.text(0.23, 1.1, "%.1f%%" % rate10, size=20)
                plt.text(-0.3, 1.1, "%.1f%%" % rate11, size=20)
                plt.text(-0.3, 0.4, "%.1f%%" % rate12, size=20)
                plt.text(0.23, 0.4, "%.1f%%" % rate13, size=20)
                
                ax.grid('off')
                ax.axis('off')
                plt.title("\n%s %s 상대 %s 로케이션 분포\n" % (name, bside, ptype), fontsize=20)
                #plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\7월 5주\\로케이션 분포\\%s %s 상대 로케이션 분포.png" % (name, bside))
