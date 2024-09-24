# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 14:31:55 2021

@author: LIONS
"""

# 메모리 딸려서 merge 못할 때 쓰는 코드

import pandas as pd
import xgboost as xgb

year = 2020
df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\%s.csv" % year, index_col=False, encoding='cp949')
df = df[df.Level == 'KBO']
mask = ((df.KorBB=='Walk')&(df.PitchCall=='BallIntentional')) | ((df.PlayResult=='Sacrifice')&(df.HitType=='Bunt'))
df = df[~mask]
inplay = df.copy()
inplay = inplay[inplay.PitchCall == 'InPlay']
inplay[['RunExpectancy', 'xRE']] = None

out = 0.32
SG = out+0.5
DB = out+0.87
TP = out+1.21
HR = out+1.43
SF = out-0.08
K = out-0.32
BB = out+0.36
HBP = out+0.41

for i in range(len(inplay.index)):
    if inplay.PitchCall.iloc[i] == 'InPlay':
        if inplay.PlayResult.iloc[i] == 'Out' or inplay.PlayResult.iloc[i] == 'FieldersChoice' or inplay.PlayResult.iloc[i] == 'Error':
            inplay.RunExpectancy.iloc[i] = 0
        elif inplay.PlayResult.iloc[i] == 'Single':
            inplay.RunExpectancy.iloc[i] = SG
        elif inplay.PlayResult.iloc[i] == 'Double':
            inplay.RunExpectancy.iloc[i] = DB
        elif inplay.PlayResult.iloc[i] == 'Triple':
            inplay.RunExpectancy.iloc[i] = TP
        elif inplay.PlayResult.iloc[i] == 'HomeRun':
            inplay.RunExpectancy.iloc[i] = HR
        elif inplay.PlayResult.iloc[i] == 'Sacrifice':
            inplay.RunExpectancy.iloc[i] = SF

X = inplay[['ExitSpeed', 'Angle']]
Y = inplay['RunExpectancy']

xRE = xgb.XGBRegressor()
xRE.fit(X, Y)
inplay['xRE'] = xRE.predict(X)

df.set_index('PitchUID', inplace=True)
df['xRE'] = None
for k in range(len(inplay.index)):
    UID = inplay.PitchUID.iloc[k]
    xRE = inplay.xRE.iloc[k]
    df.xRE.loc[UID] = xRE

df.reset_index(inplace=True)
df.dropna(subset=['xRE'], inplace=True)

maskob = ((df.PitchCall=='InPlay')&(df.PlayResult!='Out')&(df.PlayResult!='Sacrifice'))|(df.KorBB=='Walk')
ob = df[maskob]
lgobp = len(ob.index)/len(df.index)

lgxRElist = df.xRE.tolist()
lgxRE = sum(lgxRElist)/len(lgxRElist)

scale = lgobp/lgxRE

for j in range(len(df.index)):
    if df.KorBB.iloc[j] == 'Strikeout':
        df.xRE.iloc[j] = K
    elif df.KorBB.iloc[j] == 'Walk':
        if df.PitchCall.iloc[j] == 'BallCalled':
            df.xRE.iloc[j] = BB
        elif df.PitchCall.iloc[j] == 'HitByPitch':
            df.xRE.iloc[j] = HBP

df.dropna(subset=['xRE'], inplace=True)

pitidmap = df[['PitcherId', 'Pitcher']].drop_duplicates(subset=['PitcherId'])
pitid = pitidmap.PitcherId.tolist()
xwOBAlist = []
IPlist = []

for ID in pitid:
    temp = df[df.PitcherId == ID]
    xRElist = temp.xRE.tolist()
    xwOBA = scale*sum(xRElist)/len(temp.index)
    xwOBAlist.append(xwOBA)
    
    maskout = (temp.PlayResult=='Out') | (temp.KorBB=='Strikeout')
    tempout = temp[maskout]
    IP = len(tempout.index)/3
    IPlist.append(IP)

pitidmap['IP'] = IPlist
pitidmap['xwOBA'] = xwOBAlist
pitidmap.set_index('PitcherId', inplace=True)
pitidmap.to_csv("C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\%s xwOBA.csv" % year, encoding='cp949')