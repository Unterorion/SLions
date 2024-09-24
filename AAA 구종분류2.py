# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:38:39 2020

@author: user
"""

import pandas as pd
from sklearn import preprocessing
from sklearn.mixture import GaussianMixture as GMM

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import glob
import os
from matplotlib import font_manager, rc
import matplotlib

matplotlib.rcParams['axes.unicode_minus'] = False

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df=pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\AAA2021.csv', index_col=False, encoding='cp949')

def translate(x):
    if x == 'Fastball' or x == 'Four-Seam':
        return '직구'
    elif x == 'Slider':
        return '슬라이더'
    elif x == 'Curveball':
        return '커브'
    elif x == 'ChangeUp' or x == 'Changeup':
        return '체인지업'
    elif x == 'Splitter':
        return '스플리터'
    elif x == 'Cutter':
        return '커터'
    elif x == 'Sinker':
        return '싱커'
    elif x == 'Knuckleball':
        return '너클볼'

df['KorPitchType'] = df['AutoPitchType'].apply(translate)

dfcopy=df.copy()

pitidmap = df[['Pitcher', 'PitcherId', 'PitcherThrows']]
pitidmap.drop_duplicates(subset=['PitcherId'], inplace=True)
id_index_pitidmap=pitidmap.set_index('PitcherId')

df.dropna(subset=['RelSpeed', 'SpinRate', 'HorzBreak', 'InducedVertBreak', 'BatterId', 'ZoneTime'], how='any', inplace=True)

def coloring(x):
    if x==0:
        return 'red'
    if x==1:
        return 'blue'
    if x==2:
        return 'green'
    if x==3:
        return 'black'
    if x==4:
        return 'yellow'
    if x==5:
        return 'brown'
    if x==6:
        return 'purple'
    
def coloring2(x):
    if x=='직구' or x=='포심':
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
    if x=='싱커' or x=='투심':
        return 'purple'
    if x=='너클볼':
        return 'black'

def rotate(angle):
    ax.view_init(azim=angle)

df.reset_index(inplace=True)

pitid = [547176, 643615, 621112, 596071, 605541,656457, 596049, 656725, 608650, 621097, 623454, 642659, 592716, 605138, 626929, 656818]
j = pitid[15]
yimsi=pd.DataFrame(columns=['RelSpeed', 'HorzBreak', 'InducedVertBreak', 'ZoneTime', 'Cluster', 'ClusterName', 'PitchUID'])

idList = pitidmap['PitcherId'].tolist()

if j in idList:
    Name = id_index_pitidmap.loc[j, 'Pitcher'].split(', ')
    name = Name[1]+" "+Name[0]
    
print(name)
    
tempdf=df[df['PitcherId']==j]
throws = tempdf.PitcherThrows.iloc[0]
    
X=tempdf[['RelSpeed', 'SpinRate', 'HorzBreak', 'InducedVertBreak', 'ZoneTime']]
Y=tempdf[['PitcherId', 'TaggedPitchType', 'AutoPitchType','KorPitchType','RelSpeed', 'SpinRate', 'HorzBreak', 'InducedVertBreak', 'ZoneTime', 'PitchUID']]

X=preprocessing.MinMaxScaler().fit(X).transform(X)
    
    
if len(tempdf)<=2:
    pass
else:
    i=4
    while i<=6:
        gmm1=GMM(n_components=i, n_init=100).fit(X)
        bic1=gmm1.bic(X)
        gmm2=GMM(n_components=i-1, n_init=100).fit(X)
        bic2=gmm2.bic(X)
        gmm3=GMM(n_components=i+1, n_init=100).fit(X)
        bic3=gmm3.bic(X)
    
      
        if bic1<=bic2 and bic1<=bic3:
            num=i
            gmm=gmm1
            break
        else:
            i=i+1
            num=i
            gmm=gmm1
            if i>len(X):
                break
    labels=gmm.predict(X)
        
        
    Y['Cluster']=labels
    Y['ClusterName']=Y['Cluster']
    fig, ax = plt.subplots(1, figsize=(6, 6), constrained_layout=True)
    
    uniquecl=Y['Cluster'].unique().tolist()
    
    for k in uniquecl:
        
        temp=Y[Y['Cluster']==k]
        
          
        ax.scatter(temp['HorzBreak'], temp['InducedVertBreak'], c=coloring(k), label=uniquecl, alpha=0.1)
        ax.legend(uniquecl)
        
        ax.set_xlabel('수평 무브먼트')
        ax.set_ylabel('수직 무브먼트')
        
        ax.set_xlim(-60, 60)
        ax.set_ylim(-60, 60)
        ax.grid('on')
            
    plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\외인 구종분류 2\\" + name + "_"+str(j)+"_by_Cluster.png")
    

#%%
if len(tempdf)<=2:
    pass
else:
    for k in uniquecl:
        if k==0:
            pitchname = '포심'
        elif k==1:
            pitchname = '체인지업'
        elif k==2:
            pitchname = '커브'
        elif k==3:
            pitchname = '슬라이더'
        elif k==4:
            pitchname = '포심'
        elif k==5:
            pitchname = '포심'
        Y['ClusterName'].replace(k, pitchname, inplace=True)
    uniqueclname=Y['ClusterName'].unique().tolist()
        
    fig, ax = plt.subplots(1, figsize=(6, 7), constrained_layout=True)
    for k in uniqueclname:
        temp=Y[Y['ClusterName']==k]
            
            
        ax.scatter(temp['HorzBreak'], temp['InducedVertBreak'], c=coloring2(k), label=k, alpha=0.1)
        ax.legend()
        
        ax.set_xlabel('수평 무브먼트')
        ax.set_ylabel('수직 무브먼트')
        
        ax.set_xlim(-60, 60)
        ax.set_ylim(-60, 60)
        ax.grid('on')
        
    for k in uniqueclname:
        if throws == 'Right':
            if k == '포심':
                meanx = 28.5
                meany = 41.3
            elif k == '슬라이더':
                meanx = -4.1
                meany = 14.7
            elif k == '커터':
                meanx = -1.9
                meany = 22
            elif k == '커브':
                meanx = -24
                meany = -19.1
            elif k == '스플리터':
                meanx = 26.4
                meany = 17
            elif k == '체인지업':
                meanx = 38.4
                meany = 17.7
            elif k == '투심' or k == '싱커':
                meanx = 38.6
                meany = 23.6
        elif throws == 'Left':
            if k == '포심':
                meanx = -22.7
                meany = 48.3
            elif k == '슬라이더':
                meanx = 8.9
                meany = 10.9
            elif k == '커터':
                meanx = -0.6
                meany = 14.1
            elif k == '커브':
                meanx = 21.4
                meany = -22.5
            elif k == '스플리터':
                meanx = -25.5
                meany = 16.4
            elif k == '체인지업':
                meanx = -31.9
                meany = 31.2
            elif k == '투심' or k == '싱커':
                meanx = -35.1
                meany = 25.3
        
        ax.scatter(meanx, meany, c=coloring2(k), edgecolor='black', marker='o', s=150, label="%s KBO 평균"%k)
        ax.legend()
        
    plt.title("\n" + name + " 구종 분류\n", fontsize = 20)
    plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\외인 구종분류 2\\" + name + "_"+str(j)+"_by_Cluster_Name.png", dpi=50)                
    Y.to_csv('C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\외인 구종분류 2\\'+name+'.csv', index=False, encoding='cp949')
    
    Z=Y[['PitchUID', 'Cluster', 'ClusterName']]
    
    yimsi=pd.concat([Z, yimsi], ignore_index=True)
    
    

dfcopy=pd.merge(dfcopy, yimsi, how='outer', on=['PitchUID'])
    
    
#dfcopy.to_csv('C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\외인 구종분류.csv', index=False, encoding='cp949')
