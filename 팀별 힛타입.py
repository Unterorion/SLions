# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 19:51:33 2021

@author: LIONS
"""

import pandas as pd
import numpy as np

df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv", index_col=False, encoding='cp949')
df = df[(df['Level'] == 'KBO') & (df['PitchCall'] == 'InPlay')]
df.dropna(subset=['ExitSpeed'], inplace=True)

ind = df[df['HitType'] == 'Bunt'].index
df = df.drop(ind)

df = df.assign(GroundBallRate = np.where(df['HitType']=='GroundBall', 1, 0))
df = df.assign(LineDriveRate = np.where(df['HitType']=='LineDrive', 1, 0))
df = df.assign(FlyBallRate = np.where((df['HitType']=='FlyBall')|(df['HitType']=='Popup'), 1, 0))

df = df.assign(GroundBallRate_ang = np.where(df['Angle']<8, 1, 0))
df = df.assign(LineDriveRate_ang = np.where((df['Angle']>8)&(df['Angle']<20), 1, 0))
df = df.assign(FlyBallRate_ang = np.where(df['Angle']>20, 1, 0))

pt1 = pd.pivot_table(df, index='BatterTeam', values=['GroundBallRate', 'LineDriveRate', 'FlyBallRate'], aggfunc='mean')
pt2 = pd.pivot_table(df, index='BatterTeam', values=['GroundBallRate_ang', 'LineDriveRate_ang', 'FlyBallRate_ang'], aggfunc='mean')

pt1.to_csv("C:\\Users\\LIONS\\.spyder-py3\\9월 4주\\팀별 힛타입 비율.csv")
pt2.to_csv("C:\\Users\\LIONS\\.spyder-py3\\9월 4주\\팀별 힛타입 비율(각도).csv")
