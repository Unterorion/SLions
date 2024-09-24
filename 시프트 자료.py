# -*- coding: utf-8 -*-
"""
Created on Fri Jul  9 13:53:25 2021

@author: LIONS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)


df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', index_col=False, encoding='cp949')
df = df.dropna(subset=['kbo_pid'])
BatterNameList = ['터커']

IDnamepairs = df[['kbo_bid', 'batter']].drop_duplicates()
IDnamepairs = IDnamepairs.dropna(subset=['kbo_bid'])
IDnamepairs.set_index(['batter'], inplace=True)

df['DistX'] = df['Distance']*np.cos(np.pi*(45-df['Bearing'])/180)
df['DistY'] = df['Distance']*np.sin(np.pi*(45-df['Bearing'])/180)

idmap = pd.read_excel('C:\\Users\\LIONS\\.spyder-py3\\idmap_update_210628.xlsx')
idmap = idmap.set_index(['PitcherId'])

df['Under'] = None
for l in range(len(df)):
    pid = df['kbo_pid'].iloc[l]
    if idmap['언더'].loc[pid] == 1:
        df['Under'].iloc[l] = 1

for i in range(len(BatterNameList)):
    fig, ax = plt.subplots(1, figsize=(5,6), constrained_layout=True)
    
    name = BatterNameList[i]
    batterID = IDnamepairs['kbo_bid'].loc[name]
    
    mask = (df['kbo_bid'] == batterID) & (df['PitchCall'] == 'InPlay') & (df['PitcherThrows'] == 'Left') & (df['DistX'] < 99.5) & (df['DistY'] < 99.5) & (df['DistX']+df['DistY'] < 122*np.sqrt(2))
    #mask = (df['kbo_bid'] == batterID) & (df['PitchCall'] == 'InPlay') & (df['PitcherThrows'] == 'Right') & (df['DistX'] < 99.5) & (df['DistY'] < 99.5) & (df['DistX']+df['DistY'] < 122*np.sqrt(2))
    #mask = (df['kbo_bid'] == batterID) & (df['PitchCall'] == 'InPlay') & (df['Under'] == 1) & (df['DistX'] < 99.5) & (df['DistY'] < 99.5) & (df['DistX']+df['DistY'] < 122*np.sqrt(2))
    
    df_temp = df[mask]
    df_temp = df_temp.dropna(subset=['Distance'])
    
    if len(df_temp.index) >= 50:
        lastind = len(df_temp.index)
        dfRecent = df_temp.iloc[lastind-50:lastind]
    else:
        dfRecent = df_temp
    
    dfRecent['color'] = 'black'
    
    for j in range(len(dfRecent.index)):
        if dfRecent['Strikes'].iloc[j] == 2:
            dfRecent['color'].iloc[j] = 'red'
        elif dfRecent['PitcherTeam'].iloc[j] == 'SAM_LIO':
            dfRecent['color'].iloc[j] = 'blue'
    
    aIn = 28.96
    cIn = 18.44/np.sqrt(2)
    bIn = np.sqrt(aIn**2-cIn**2)
    ref_angIn = np.arccos((aIn**2+bIn**2-cIn**2)/(2*aIn*bIn))
    angIn = np.linspace(-ref_angIn, ref_angIn+np.pi/2)
    ax.plot(cIn+aIn*np.cos(angIn), cIn+aIn*np.sin(angIn), color='black', linewidth=1)
    
    ax.plot([0, 0], [0, 99.5], color='black', linewidth=2)
    ax.plot([0, 99.5], [0, 0], color='black', linewidth=2)
    ax.plot([99.5, 99.5], [0, 122*np.sqrt(2)-99.5], color='black', linewidth=2)
    ax.plot([0, 122*np.sqrt(2)-99.5], [99.5, 99.5], color='black', linewidth=2)
    ax.plot([122*np.sqrt(2)-99.5, 99.5], [99.5, 122*np.sqrt(2)-99.5], color='black', linewidth=2)
    ax.plot([27.43, 27.43], [0, 27.43], color='black', linewidth=1)
    ax.plot([0, 27.43], [27.43, 27.43], color='black', linewidth=1)
    ax.set_xlim(0, 99.5)
    ax.set_ylim(0, 99.5)
    ax.axis('off')
    ax.set_title(name+"\n", fontsize=30)
    
    for j in range(len(dfRecent.index)):
        ang = np.pi*(45 - dfRecent['Bearing'].iloc[j])/180
        x = dfRecent['Distance'].iloc[j]*np.cos(ang)
        y = dfRecent['Distance'].iloc[j]*np.sin(ang)
        
        ax.plot([0,x], [0,y], color = dfRecent['color'].iloc[j], linewidth = 2)
        ax.scatter(x, y, color = dfRecent['color'].iloc[j])