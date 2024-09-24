# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 16:35:21 2021

@author: LIONS
"""

import pandas as pd

dfAll = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\AAA2021.csv', index_col=False, encoding='cp949')
dfAll = dfAll[dfAll.Level == 'AAA']
pitidmap = dfAll[['PitcherId', 'Pitcher']]
pitidmap.drop_duplicates(subset=['PitcherId'], inplace=True)
pitidmap.set_index('PitcherId', inplace=True)

pitid = [547176, 643615, 621112, 596071, 605541,656457, 596049, 656725, 608650, 621097, 623454, 642659, 592716, 605138, 626929, 656818]

info = pd.DataFrame(columns=['PitcherId', 'Pitcher', 'ZswingRate', 'OswingRate', 'ZcontRate', 'OcontRate', 'PullRate', 'CenterRate', 'OppoRate', 'HardHitRate', 'NonHardHitRate'])
info['PitcherId'] = pitid
info.set_index('PitcherId', inplace=True)

for ID in pitid:
    rawname = pitidmap.Pitcher.loc[ID]
    Name = rawname.split(', ')
    name = Name[1] + ' ' + Name[0]
    info.Pitcher.loc[ID] = name
    
    mask = (dfAll.PitcherId == ID)
    df = dfAll[mask]
    
    maskZ = (df.PlateLocSide>-0.254) & (df.PlateLocSide<0.254) & (df.PlateLocHeight>0.4572) & (df.PlateLocHeight<1.0668)
    dfZ = df[maskZ]
    dfO = df[~maskZ]
    
    pd = []
    for dfz in [dfZ, dfO]:
        masks = (df.PitchCall == 'StrikeSwinging') | (df.PitchCall == 'InPlay') | (df.PitchCall == 'FoulBall')
        maskc = (df.PitchCall == 'InPlay') | (df.PitchCall == 'FoulBall')
        
        dfzs = dfz[masks]
        dfzc = dfz[maskc]
        
        SR = len(dfzs.index)/len(dfz.index)
        CR = len(dfzc.index)/len(dfzs.index)
        
        pd.append(SR)
        pd.append(CR)
    
    info['ZswingRate'].loc[ID] = pd[0]
    info['ZcontRate'].loc[ID] = pd[1]
    info['OswingRate'].loc[ID] = pd[2]
    info['OcontRate'].loc[ID] = pd[3]
    
    dfBBE = df.dropna(subset=['Bearing'])
    maskPull = ((dfBBE.BatterSide=='Right')&(dfBBE.Bearing<-15)) | ((dfBBE.BatterSide=='Left')&(dfBBE.Bearing>15))
    maskOppo = ((dfBBE.BatterSide=='Right')&(dfBBE.Bearing>15)) | ((dfBBE.BatterSide=='Left')&(dfBBE.Bearing<-15))
    maskCent = (dfBBE.Bearing > -15) & (dfBBE.Bearing < 15)
    maskHard = (dfBBE.ExitSpeed > 155)
    
    dfPull = dfBBE[maskPull]
    dfOppo = dfBBE[maskOppo]
    dfCent = dfBBE[maskCent]
    dfHard = dfBBE[maskHard]
    
    pullrate = len(dfPull.index)/len(dfBBE.index)
    opporate = len(dfOppo.index)/len(dfBBE.index)
    centrate = len(dfCent.index)/len(dfBBE.index)
    hardrate = len(dfHard.index)/len(dfBBE.index)
    
    info['PullRate'].loc[ID] = pullrate
    info['CenterRate'].loc[ID] = centrate
    info['OppoRate'].loc[ID] = opporate
    info['HardHitRate'].loc[ID] = hardrate
    info['NonHardHitRate'].loc[ID] = 1 - hardrate

info.to_csv('C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\외인 영입대상 타자반응.csv', encoding='cp949')
