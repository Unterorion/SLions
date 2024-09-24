# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 15:17:27 2021

@author: LIONS
"""

import pandas as pd
import xgboost as xgb
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib import font_manager, rc
import matplotlib

matplotlib.rcParams['axes.unicode_minus'] = False

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', index_col=False, encoding='cp949')
df = df[df.PitName1 == '데스파이네']
df = df[df.Level == 'KBO']
df.dropna(subset=['RelSpeed'], inplace=True)

X = df[['RelSpeed', 'InducedVertBreak', 'HorzBreak']]
Y = df['pitch_type']

Pclass = xgb.XGBClassifier()
Pclass.fit(X, Y)

df['PitchClass'] = Pclass.predict(df[['RelSpeed', 'InducedVertBreak', 'HorzBreak']])
ptlist = df.PitchClass.unique().tolist()

def coloring(x):
    if x=='직구':
        return 'red'
    if x=='슬라이더':
        return 'darkgreen'
    if x=='커브':
        return 'orange'
    if x=='체인지업':
        return 'blue'
    if x=='스플리터':
        return 'brown'
    if x=='커터':
        return 'lightgreen'
    if x=='투심' or '싱커':
        return 'purple'
    if x=='너클볼':
        return 'gray'

def coloring2(x):
    if x=='FastBall' or 'Fastball':
        return 'red'
    if x=='Slider':
        return 'darkgreen'
    if x=='CurveBall' or 'Curveball':
        return 'orange'
    if x=='ChangeUp' or 'Changeup':
        return 'blue'
    if x=='Splitter':
        return 'brown'
    if x=='Cutter':
        return 'lightgreen'
    if x=='Sinker':
        return 'purple'
    if x=='KnuckleBall':
        return 'gray'

def rotate(angle):
    ax.view_init(azim=angle)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for ptype in ptlist:
    temp = df[df.PitchClass == ptype]
    ax.scatter(temp.RelSpeed, temp.HorzBreak, temp.InducedVertBreak, c=coloring(ptype), alpha=0.1)
    
    ax.set_xlabel('구속')
    ax.set_ylabel('수평 무브먼트')
    ax.set_zlabel('수직 무브먼트')
    
    ax.set_xlim(90, 160)
    ax.set_ylim(-60, 60)
    ax.set_zlim(-60, 60)
    ax.grid('on')
ax.legend(ptlist)
ax.grid('on')
rot_animation = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 362, 2), interval=100)
rot_animation.save("C:\\Users\\LIONS\\.spyder-py3\\8월 4주\\xgb 데스파이네 구종분류2.gif", dpi=80, writer='imagemagick')
