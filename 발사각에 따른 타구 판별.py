# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 12:48:08 2021

@author: LIONS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('2020_Classified_한글_4th_Edition_누락분_pitchfx.csv')

'''df['Angle sector'] = np.around(df['Angle'])

df['Angle sector'].replace('', np.nan, inplace=True)
df.dropna(subset=['Angle sector'], inplace=True)'''

mask_GB = (df.HitType == 'GroundBall')
mask_FB = (df.HitType == 'FlyBall')
mask_LD = (df.HitType == 'LineDrive')
mask_PU = (df.HitType == 'Popup')

df_GB = df[mask_GB]
df_FB = df[mask_FB]
df_LD = df[mask_LD]
df_PU = df[mask_PU]

df_GB['Angle'].plot(kind='hist', bins=100, color='blue', alpha=0.4)
df_LD['Angle'].plot(kind='hist', bins=100, color='orange', alpha=0.4)
df_FB['Angle'].plot(kind='hist', bins=100, color='green', alpha=0.4)
df_PU['Angle'].plot(kind='hist', bins=100, color='red', alpha=0.4)
plt.legend(labels=['Groundball', 'Linedrive', 'Flyball', 'Popup'], loc='upper left')
plt.xlabel('Launch angle')
plt.ylabel('Frequency')
plt.title('발사각에 따른 타구 판별')
plt.show