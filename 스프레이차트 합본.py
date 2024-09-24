# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 18:48:46 2021

@author: LIONS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df_batter = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\스카우팅 대상자(고졸타자) ID 및 스탯.csv", index_col=False, encoding='cp949')
df = pd.read_csv("C:\\Users\\LIONS\\Desktop\\고교야구\\황사기 청룡기 통합.csv", index_col=False, encoding='cp949')
dfHS = pd.read_csv("C:\\Users\\LIONS\\Desktop\\고교야구\\황사기 통합.csv", index_col=False, encoding='cp949')
dfCR = pd.read_csv("C:\\Users\\LIONS\\Desktop\\고교야구\\청룡기 통합.csv", index_col=False, encoding='cp949')

HSB = dfHS.BatterId.unique().tolist()
CRB = dfCR.BatterId.unique().tolist()

a=99.5/np.sqrt(2)
b=99.5*np.sqrt(2)-122.5

def color_hit(ExitSpeed):
    if ExitSpeed < 125:
        return 'blue'
    elif ExitSpeed > 125 and ExitSpeed < 155:
        return 'yellow'
    elif ExitSpeed > 155:
        return 'red'
    else:
        return 'grey'

for i in range(len(df_batter.index)):
    name = df_batter['이름'].iloc[i]
    ID = df_batter['ID'].iloc[i]
    
    contest = 0
    if ID in HSB:
        contest += 10
    if ID in CRB:
        contest += 1
    
    if contest == 1:
        contname = '청룡기'
    elif contest == 10:
        contname = '황금사자기'
    elif contest == 11:
        contname = '황사기+청룡기'
    
    mask = (df.BatterId == ID) & (df.PitchCall == 'InPlay')
    df_inplay = df[mask]
    if len(df_inplay.index) != 0:
        df_inplay['Bearing_Rad'] = (90 - df_inplay['Bearing'])*np.pi/180
        df_inplay['x_coord'] = df_inplay['Distance']*np.cos(df_inplay['Bearing_Rad'])
        df_inplay['y_coord'] = df_inplay['Distance']*np.sin(df_inplay['Bearing_Rad'])
        df_inplay['chart_color'] = df_inplay['ExitSpeed'].apply(color_hit)
        
        mask1 = (df_inplay['ExitSpeed'] < 125)
        mask2 = (df_inplay['ExitSpeed'] > 125) & (df_inplay['ExitSpeed'] < 155)
        mask3 = (df_inplay['ExitSpeed'] > 155)
        
        df_weak = df_inplay[mask1]
        df_mid = df_inplay[mask2]
        df_hard = df_inplay[mask3]
        
        fig, ax = plt.subplots(1, figsize=(8, 7.5), constrained_layout=True)
        
        ax.plot([-a, 0], [a, 0], color='black', linewidth=2)
        ax.plot([0, a], [0, a], color='black', linewidth=2)
        ax.plot([-a, -b], [a, 122.5], color='black', linewidth=2)
        ax.plot([b, a], [122.5, a], color='black', linewidth=2)
        ax.plot([-b, b], [122.5, 122.5], color='black', linewidth=2)
        
        ax.plot([-27.432/np.sqrt(2), 0], [27.432/np.sqrt(2), 27.432*np.sqrt(2)], color='grey', linewidth=1)
        ax.plot([27.432/np.sqrt(2), 0], [27.432/np.sqrt(2), 27.432*np.sqrt(2)], color='grey', linewidth=1)
        
        if len(df_weak.index) > 0:
            ax.scatter(df_weak['x_coord'], df_weak['y_coord'], c=df_weak['chart_color'], s=500, alpha=0.2, label='약한 타구')
        if len(df_mid.index) > 0:
            ax.scatter(df_mid['x_coord'], df_mid['y_coord'], c=df_mid['chart_color'], s=500, alpha=0.2, label='중간 타구')
        if len(df_hard.index) > 0:
            ax.scatter(df_hard['x_coord'], df_hard['y_coord'], c=df_hard['chart_color'], s=500, alpha=0.2, label='강한 타구')

        ax.set_xlim(-100, 100)
        ax.set_ylim(-20, 130)
        ax.axis('off')
        
        ax.legend(fontsize=20, loc='lower right')
        plt.title("\n%s 스프레이차트\n(%s)" % (name, contname), fontsize=30)
        plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\스카우팅 대상자 시각화\\%s_1 %s 스프레이차트.png" % (i+1, name), dpi=50)
        