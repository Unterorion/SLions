# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 13:32:31 2021

@author: LIONS
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import os

from matplotlib import font_manager, rc
import matplotlib

matplotlib.rcParams['axes.unicode_minus'] = False

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

name = 'Leiter, Mark'
j = 643615

def coloring2(x):
    if x=='Fastball':
        return 'red'
    if x=='Slider':
        return 'darkgreen'
    if x=='Curveball':
        return 'orange'
    if x=='ChangeUp':
        return 'blue'
    if x=='Splitter':
        return 'brown'
    if x=='Cutter':
        return 'lightgreen'
    if x=='Sinker':
        return 'purple'
    if x=='Knuckleball':
        return 'gray'

def rotate(angle):
    ax.view_init(azim=angle)

filelist = os.listdir('C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\라이터')
flielist = filelist[0:1]

for file in filelist:
    df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\라이터\\%s' % file, index_col=False, encoding='cp949')
    name = file[:-4]
    ID = df['PitcherId'].unique().tolist()[0]
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    uniquecl = df['NewClusterName'].unique().tolist()
    for k in uniquecl:
        temp = df[df['NewClusterName'] == k]
        ax.scatter(temp['RelSpeed'], temp['HorzBreak'], temp['InducedVertBreak'], c=coloring2(k), label=uniquecl)
        ax.legend(uniquecl)
        
        ax.set_xlabel('구속')
        ax.set_ylabel('수평 무브먼트')
        ax.set_zlabel('수직 무브먼트')
        
        ax.set_xlim(90, 160)
        ax.set_ylim(-60, 60)
        ax.set_zlim(-60, 60)
        ax.grid('on')
        
    rot_animation = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 362, 2), interval=100)
    rot_animation.save("C:\\Users\\LIONS\\.spyder-py3\\10월 3주\\라이터\\%s_%d_by_Cluster_Name.gif" % (name, ID), dpi=80, writer='imagemagick')