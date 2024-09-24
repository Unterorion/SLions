# -*- coding: utf-8 -*-
"""
Created on Thu Sep  2 09:35:54 2021

@author: LIONS
"""

import pandas as pd

df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2020.csv", index_col=None, encoding='cp949')
K = pd.read_excel("C:\\Users\\LIONS\\.spyder-py3\\8월 4주\\20K.xlsx", index_col=None)
B = pd.read_excel("C:\\Users\\LIONS\\.spyder-py3\\8월 4주\\20BB.xlsx", index_col=None)

df = df[df.Level == 'KBO']
batid = df[['BatName1', 'kbo_bid']].drop_duplicates(subset=['kbo_bid'])
batid.set_index('kbo_bid', inplace=True)
SR = []
TR = []
WR = []
tWR = []
for j in range(len(K.index)):
    name = K.BatName1.iloc[j]
    ind = batid.index[batid['BatName1'] == name].tolist()
    if len(ind) == 1:
        ID = ind[0]
    else:
        print(batid.kbo_bid.iloc[ind])
        ID = input("Choose ID among ones above : ")
    temp = df[df.kbo_bid == ID]
    temp.dropna(subset=['RelSpeed'], inplace=True)
    maskS = (temp.PitchCall=='StrikeSwinging')|(temp.PitchCall=='FoulBall')|(temp.PitchCall=='InPlay')
    maskW = (temp.PitchCall=='StrikeSwinging')
    swing = temp[maskS]
    take = temp[~maskS]
    whiff = temp[maskW]
    SR.append(len(swing.index)/len(temp.index))
    TR.append(len(take.index)/len(temp.index))
    WR.append(len(whiff.index)/len(swing.index))
    tWR.append(len(whiff.index)/len(temp.index))

K['SwingRate'] = SR
K['TakeRate'] = TR
K['WhiffRate'] = WR
K['TotalWhiffRate'] = tWR
RK = K.corr()
R2K = RK**2

SR = []
TR = []
WR = []
tWR = []
for i in range(len(B.index)):
    name = B.BatName1.iloc[i]
    ind = batid.index[batid['BatName1'] == name].tolist()
    if len(ind) == 1:
        ID = ind[0]
    else:
        print(batid.kbo_bid.iloc[ind])
        ID = input("Choose ID among ones above : ")
    temp = df[df.kbo_bid == ID]
    temp.dropna(subset=['RelSpeed'], inplace=True)
    maskS = (temp.PitchCall=='StrikeSwinging')|(temp.PitchCall=='FoulBall')|(temp.PitchCall=='InPlay')
    maskW = (temp.PitchCall=='StrikeSwinging')
    swing = temp[maskS]
    take = temp[~maskS]
    whiff = temp[maskW]
    SR.append(len(swing.index)/len(temp.index))
    TR.append(len(take.index)/len(temp.index))
    WR.append(len(whiff.index)/len(swing.index))
    tWR.append(len(whiff.index)/len(temp.index))

B['SwingRate'] = SR
B['TakeRate'] = TR
B['WhiffRate'] = WR
B['TotalWhiffRate'] = tWR
RB = B.corr()
R2B = RB**2

R2K.to_csv("C:\\Users\\LIONS\\.spyder-py3\\8월 4주\\타자 K% - plate discipline R2.csv", encoding='cp949')
R2B.to_csv("C:\\Users\\LIONS\\.spyder-py3\\8월 4주\\타자 BB% - plate discipline R2.csv", encoding='cp949')