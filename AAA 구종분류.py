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
    elif x == 'ChangeUp':
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
        return 'green'
    if x=='싱커':
        return 'purple'
    if x=='너클볼':
        return 'black'

def rotate(angle):
    ax.view_init(azim=angle)

df.reset_index(inplace=True)

pitid = [649963]
yimsi=pd.DataFrame(columns=['RelSpeed', 'HorzBreak', 'InducedVertBreak', 'ZoneTime', 'Cluster', 'ClusterName', 'PitchUID'])

idList = pitidmap['PitcherId'].tolist()

for j in pitid:
    
    
    if j in idList:
        Name = id_index_pitidmap.loc[j, 'Pitcher'].split(', ')
        name = Name[1]+" "+Name[0]
    else:
        continue
    
    print(name)
    
    tempdf=df[df['PitcherId']==j]
    
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
            pitchlist=Y.groupby('Cluster').get_group(k).KorPitchType.value_counts(1).index.tolist()
            pitchname = pitchlist[0]
    
                
            
            Y['ClusterName'].replace(k, pitchname, inplace=True)
            
            temp=Y[Y['Cluster']==k]
            
           
            ax.scatter(temp['HorzBreak'], temp['InducedVertBreak'], c=coloring(k), label=uniquecl, alpha=0.1)
            ax.legend(uniquecl)
            
            ax.set_xlabel('수평 무브먼트')
            ax.set_ylabel('수직 무브먼트')
            
            ax.set_xlim(-60, 60)
            ax.set_ylim(-60, 60)
            ax.grid('on')
            
        #plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\외인 구종분류\\" + name + "_"+str(j)+"_by_Cluster.png")
                    
        #Y.to_csv('C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\외인 구종분류\\'+name+'.csv', index=False, encoding='cp949')
        
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
            throws = id_index_pitidmap.loc[j, 'PitcherThrows']
            mask = (df.KorPitchType == k) & (df.Level == 'AAA') & (df.PitcherThrows == throws)
            df_pitchtype = df[mask]
            meanx = df_pitchtype['HorzBreak'].mean()
            meany = df_pitchtype['InducedVertBreak'].mean()
            ax.scatter(meanx, meany, c=coloring2(k), edgecolor='black', marker='o', s=150, label="%s AAA 평균"%k)
            ax.legend()
        
        plt.title("\n" + name + " 구종 분류\n", fontsize = 20)
        #plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\외인 구종분류\\" + name + "_"+str(j)+"_by_Cluster_Name.png")
        
        Z=Y[['PitchUID', 'Cluster', 'ClusterName']]
        
        yimsi=pd.concat([Z, yimsi], ignore_index=True)
    
    

dfcopy=pd.merge(dfcopy, yimsi, how='outer', on=['PitchUID'])
    
    
#dfcopy.to_csv('C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\외인 구종분류.csv', index=False, encoding='cp949')
