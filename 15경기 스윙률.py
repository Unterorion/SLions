# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 09:47:45 2021

@author: LIONS
"""

# recent 15 games

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', encoding='cp949')

BatterNameList = ['강민호']

graphind = list(range(5))

for Batter in BatterNameList:
    mask_indi = (df.BatName1 == Batter) & (df.BatterTeam == 'SAM_LIO')
    df_indi = df[mask_indi]
    
    gamesdf = df_indi['GameID'].drop_duplicates()
    gamesList = gamesdf.tolist()
    
    ZswingList = []
    OswingList = []
    
    for gameID in gamesList:
        if gamesList.index(gameID) >= 14:
            recentList = gamesList[gamesList.index(gameID)-14:gamesList.index(gameID)+1]
        else:
            recentList = gamesList[0:gamesList.index(gameID)+1]
    
        PitchNumZ = 0
        PitchNumO = 0
        SwingNumZ = 0
        SwingNumO = 0
        
        for recentID in recentList:
            maskZrecent = (df_indi.PlateLocHeight > 0.4572) & (df_indi.PlateLocHeight < 1.0668) & (df_indi.PlateLocSide > -0.254) & (df_indi.PlateLocSide < 0.254) & (df_indi.GameID == recentID)
            maskOrecent = ((df_indi.PlateLocHeight < 0.4572) | (df_indi.PlateLocHeight > 1.0668) | (df_indi.PlateLocSide < -0.254) | (df_indi.PlateLocSide > 0.254)) & (df_indi.GameID == recentID)
            df_indiZ = df_indi[maskZrecent]
            df_indiO = df_indi[maskOrecent]
            
            PitchNumZ += len(df_indiZ.index)
            PitchNumO += len(df_indiO.index)
            
            maskZswing = (df_indiZ.PitchCall == 'FoulBall') | (df_indiZ.PitchCall == 'StrikeSwinging') | (df_indiZ.PitchCall == 'InPlay')
            maskOswing = (df_indiO.PitchCall == 'FoulBall') | (df_indiO.PitchCall == 'StrikeSwinging') | (df_indiO.PitchCall == 'InPlay')
            df_indiZswing = df_indiZ[maskZswing]
            df_indiOswing = df_indiO[maskOswing]
            
            SwingNumZ += len(df_indiZswing.index)
            SwingNumO += len(df_indiOswing.index)
            
        if PitchNumZ == 0:
            Zswing = 0
        else:
            Zswing = 100*SwingNumZ/PitchNumZ
        if PitchNumO == 0:
            Oswing = 0
        else:
            Oswing = 100*SwingNumO/PitchNumO
        ZswingList.append(Zswing)
        OswingList.append(Oswing)
    
    gameind = []
    for ind in graphind:
        gameind.append(gamesList[ind*len(gamesList)//5])
    gameind.append(gamesList[len(gamesList)-1])
    
    fig = plt.figure(figsize=(12,9))
    ax = fig.add_subplot(1,1,1)
    ax.plot(gamesList, ZswingList, color='blue', label='Z-swing%')
    ax.plot(gamesList, OswingList, color='red', label='O-swing%')
    ax.legend(loc=0)
    ax.set_title('%s 존 안/밖 스윙률' % Batter)
    ax.set_xticks(gameind)
    plt.xticks(rotation=45, ha='center')
    plt.grid(True)
    plt.show()