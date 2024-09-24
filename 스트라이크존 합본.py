# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 20:02:50 2021

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

def color_loc(PitchCall):
    if PitchCall == 'StrikeSwinging':
        return 'blue'
    elif PitchCall == 'InPlay' or PitchCall == 'FoulBall':
        return 'red'

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
    
    mask = (df.BatterId == ID)
    df_zone = df[mask]
    if len(df_zone.index) != 0:
        df_zone['chart_color'] = df_zone['PitchCall'].apply(color_loc)
        df_zone['CalibLocSide'] = df_zone['PlateLocSide']
        df_zone['CalibLocHeight'] = df_zone['PlateLocHeight']
        
        for j in range(len(df_zone.index)):
            if df_zone['PlateLocSide'].iloc[j] < -0.6096:
                df_zone['CalibLocSide'].iloc[j] = -0.6096
            elif df_zone['PlateLocSide'].iloc[j] > 0.6096:
                df_zone['CalibLocSide'].iloc[j] = 0.6096
            
            if df_zone['PlateLocHeight'].iloc[j] < 0.1524:
                df_zone['CalibLocHeight'].iloc[j] = 0.1524
            elif df_zone['PlateLocHeight'].iloc[j] > 1.3716:
                df_zone['CalibLocHeight'].iloc[j] = 1.3716
                
        mask1 = (df_zone['PitchCall'] == 'StrikeSwinging')
        mask2 = (df_zone['PitchCall'] == 'InPlay') | (df_zone['PitchCall'] == 'FoulBall')
        
        df_swing = df_zone[mask1]
        df_cont = df_zone[mask2]
        
        fig, ax = plt.subplots(1, figsize=(6, 8), constrained_layout=True)
        ax.plot([-0.254, 0.254], [0.4572, 0.4572], color='black', linewidth=2)
        ax.plot([-0.254, 0.254], [1.0668, 1.0668], color='black', linewidth=2)
        ax.plot([-0.254, -0.254], [0.4572, 1.0668], color='black', linewidth=2)
        ax.plot([0.254, 0.254], [0.4572, 1.0668], color='black', linewidth=2)
        
        if len(df_swing.index) > 0:
            ax.scatter(df_swing['CalibLocSide'], df_swing['CalibLocHeight'], c=df_swing['chart_color'], marker='o', s=500, alpha=0.2, label='헛스윙')
        if len(df_cont.index) > 0:
            ax.scatter(df_cont['CalibLocSide'], df_cont['CalibLocHeight'], c=df_cont['chart_color'], marker='o', s=500, alpha=0.2, label='컨택')
    
        ax.set_xlim(-0.6096,0.6096)
        ax.set_ylim(0.1524,1.3716)
        ax.axis('off')
        if df_zone['BatterSide'].iloc[0] == 'Right':
            ax.legend(loc='lower right', fontsize=20)
        elif df_zone['BatterSide'].iloc[0] == 'Left':
            ax.legend(loc='lower left', fontsize=20)
    
        plt.title("\n%s 헛스윙 및 컨택\n(%s)" % (name, contname), fontsize=30)
        plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\스카우팅 대상자 시각화\\%s_2 %s 컨택.png" % (i+1, name), dpi=50)
    