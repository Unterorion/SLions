# -*- coding: utf-8 -*-
"""
Created on Wed Sep 29 13:37:34 2021

@author: LIONS
"""

import pandas as pd
import xgboost as xgb
import numpy as np

df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', index_col=False, encoding='cp949')
df = df[(df['Level'] == 'KBO') & (df['PitchCall'] == 'InPlay')]
df.dropna(subset=['ExitSpeed'], inplace=True)

ind = df[df['HitType'] == 'Bunt'].index
df = df.drop(ind)
df2 = df.copy()

X = df[['ExitSpeed', 'Angle']]
Y = df['HitType']

Hclass = xgb.XGBClassifier()
Hclass.fit(X, Y)
df['HitTypeClass'] = Hclass.predict(df[['ExitSpeed', 'Angle']])

df = df.assign(inc = np.where(df['HitType']==df['HitTypeClass'], 1, 0))

pt1 = pd.pivot_table(df, index='HitType', values='inc', aggfunc='mean')
pt2 = pd.pivot_table(df, index='HitTypeClass', values='inc', aggfunc='mean')

ind2 = df2[df2['HitType'] == 'Popup'].index
df2['HitType'][ind2] = 'FlyBall'

X2 = df2[['ExitSpeed', 'Angle']]
Y2 = df2['HitType']

Hclass2 = xgb.XGBClassifier()
Hclass2.fit(X2, Y2)
df2['HitTypeClass'] = Hclass2.predict(df2[['ExitSpeed', 'Angle']])

df2 = df2.assign(inc = np.where(df2['HitType']==df2['HitTypeClass'], 1, 0))

pt3 = pd.pivot_table(df2, index='HitType', values='inc', aggfunc='mean')
pt4 = pd.pivot_table(df2, index='HitTypeClass', values='inc', aggfunc='mean')

'''
df = df.assign(GroundBallRate = np.where(df['HitTypeClass']=='GroundBall', 1, 0))
df = df.assign(LineDriveRate = np.where(df['HitTypeClass']=='LineDrive', 1, 0))
df = df.assign(FlyBallRate = np.where((df['HitTypeClass']=='FlyBall')|(df['HitTypeClass']=='Popup'), 1, 0))

pt = pd.pivot_table(df, index='BatterTeam', values=['GroundBallRate', 'LineDriveRate', 'FlyBallRate'], aggfunc='mean')
pt.to_csv("C:\\Users\\LIONS\\.spyder-py3\\9월 4주\\팀별 힛타입 비율(xgb).csv")
'''

#%%
import matplotlib.pyplot as plt

pu1 = df[df['HitType']=='FlyBall']
pu2 = df[df['HitTypeClass']=='FlyBall']

for pu in [pu1, pu2]:
    pu['x'] = pu['Distance']*np.cos(np.pi*(90-pu['Bearing'])/180)
    pu['y'] = pu['Distance']*np.sin(np.pi*(90-pu['Bearing'])/180)
    
    fig, ax = plt.subplots(1, figsize=(10,10), constrained_layout=True)
        
    ax.set_xlim(-99.5/np.sqrt(2), 99.5/np.sqrt(2))  
    ax.set_ylim(0, 99.5*np.sqrt(2)) 
    ax.axis('off')
    
    ax.plot([-99.5/np.sqrt(2),0], [99.5/np.sqrt(2),0], linewidth=2, color='black')
    ax.plot([0,99.5/np.sqrt(2)], [0,99.5/np.sqrt(2)], linewidth=2, color='black')
    ax.plot([-99.5/np.sqrt(2),122.5-99.5*np.sqrt(2)], [99.5/np.sqrt(2),122.5], linewidth=2, color='black')
    ax.plot([99.5*np.sqrt(2)-122.5,99.5/np.sqrt(2)], [122.5,99.5/np.sqrt(2)], linewidth=2, color='black')
    ax.plot([122.5-99.5*np.sqrt(2),99.5*np.sqrt(2)-122.5],[122.5,122.5], linewidth=2, color='black')
    
    x_bd = np.linspace(-38.91/np.sqrt(2), 38.91/np.sqrt(2))
    y_bd = 18.47 + np.sqrt(28.96**2 - x_bd**2)
    ax.plot(x_bd, y_bd, linewidth=1, color='black')
    
    ax.plot([-27.44/np.sqrt(2),0], [27.44/np.sqrt(2),27.44*np.sqrt(2)], linewidth=1, color='black')
    ax.plot([0,27.44/np.sqrt(2)], [27.44*np.sqrt(2),27.44/np.sqrt(2)], linewidth=1, color='black')
    
    ax.scatter(pu['x'], pu['y'], c='red', s=200)