# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 15:15:42 2021

@author: LIONS
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager, rc
import matplotlib

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\AAA2021.csv")
pitcher = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\7월 3주\\fangraphs-minor-league-leaders.csv", encoding='cp949')

def pitchname(pitchtype):
    if pitchtype == 'Fastball':
        return '직구'
    elif pitchtype == 'Slider':
        return '슬라이더'
    elif pitchtype == 'ChangeUp':
        return '체인지업'
    elif pitchtype == 'Sinker':
        return '싱커'
    elif pitchtype == 'Curveball':
        return '커브'
    elif pitchtype == 'Cutter':
        return '커터'
    elif pitchtype == 'Undefined':
        return '기타'

df['PitchKorName'] = df['TaggedPitchType'].apply(pitchname)

for i in range(len(pitcher.index)):
    ID = pitcher['ID'].iloc[i]
    name = pitcher['이름'].iloc[i]
    df_indi = df[df.PitcherId == ID]
    
    df_FB = df_indi[df_indi.TaggedPitchType == 'Fastball']
    df_SL = df_indi[df_indi.TaggedPitchType == 'Slider']
    df_CU = df_indi[df_indi.TaggedPitchType == 'ChangeUp']
    df_SK = df_indi[df_indi.TaggedPitchType == 'Sinker']
    df_CB = df_indi[df_indi.TaggedPitchType == 'Curveball']
    df_CF = df_indi[df_indi.TaggedPitchType == 'Cutter']
    df_UD = df_indi[df_indi.TaggedPitchType == 'Undefined']
    
    pitchDFlist = [df_FB, df_SL, df_CU, df_SK, df_CB, df_CF, df_UD]
    
    for pitchdf in pitchDFlist:
        if len(pitchdf.index) > 10:
            pitchKor = pitchdf['PitchKorName'].iloc[0]
            fig, ax = plt.subplots(1, figsize=(6, 8), constrained_layout=True)
            maskW = (pitchdf['PitchCall'] == 'StrikeSwinging')
            maskC = (pitchdf['PitchCall'] == 'InPlay') | (pitchdf['PitchCall'] == 'FoulBall')
            pitchdfW = pitchdf[maskW]
            pitchdfC = pitchdf[maskC]
            whiffPerc = 100*len(pitchdfW.index)/(len(pitchdfW.index)+len(pitchdfC.index))
            text = "헛스윙률 = %.1f%%" % whiffPerc
            
            ax.plot([-25.4, 25.4], [45.72, 45.72], color='black', linewidth=2)
            ax.plot([-25.4, 25.4], [106.68, 106.68], color='black', linewidth=2)
            ax.plot([-25.4, -25.4], [45.72, 106.68], color='black', linewidth=2)
            ax.plot([25.4, 25.4], [45.72, 106.68], color='black', linewidth=2)
            ax.scatter(100*pitchdfW['PlateLocSide'], 100*pitchdfW['PlateLocHeight'], c='red', s=200, alpha=0.2, label='헛스윙')
            ax.scatter(100*pitchdfC['PlateLocSide'], 100*pitchdfC['PlateLocHeight'], c='blue', s=200, alpha=0.2, label='컨택')
            ax.set_xlim(-50.8, 50.8)
            ax.set_ylim(20, 130)
            ax.legend(loc='upper left', fontsize=13)
            plt.text(-47, 130, text, fontsize=15)
            ax.axis('off')
            ax.grid('off')
            plt.title("%s %s 헛스윙 및 컨택\n\n" % (name, pitchKor), fontsize=20)
            plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\7월 3주\\외인 투수 후보 시각화\\%s %s 헛스윙 및 컨택.png" % (name, pitchKor), dpi=50)