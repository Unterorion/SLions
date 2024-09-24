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

def color(pitchtype):
    if pitchtype == 'Fastball':
        return 'red'
    elif pitchtype == 'Slider':
        return 'darkgreen'
    elif pitchtype == 'ChangeUp':
        return 'blue'
    elif pitchtype == 'Sinker':
        return 'purple'
    elif pitchtype == 'Curveball':
        return 'orange'
    elif pitchtype == 'Cutter':
        return 'green'
    elif pitchtype == 'Undefined':
        return 'grey'

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

df['Color'] = df['TaggedPitchType'].apply(color)
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
    
    fig, ax = plt.subplots(1, figsize=(6, 7), constrained_layout=True)
    ax.set_ylim(-70,70)
    ax.set_xlim(-60,70)
    
    for pitchdf in pitchDFlist:
        if len(pitchdf.index) > 0:
            ax.scatter(pitchdf['HorzBreak'], pitchdf['InducedVertBreak'], s=200, c=pitchdf['Color'], alpha=0.1, label=pitchdf['PitchKorName'].iloc[0])
    ax.grid('on')
    ax.legend(fontsize=15)
    plt.title("%s 수평/수직 무브먼트\n" % name, fontsize=20)
    plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\7월 3주\\외인 투수 후보 시각화\\%s 무브먼트.png" % name, dpi=50)