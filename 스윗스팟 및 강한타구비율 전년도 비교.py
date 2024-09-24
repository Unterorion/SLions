# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 13:04:01 2021

@author: LIONS
"""

import pandas as pd

df20 = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2020_Classified_한글_4th_Edition_누락분_pitchfx.csv', encoding='cp949')
df21 = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', encoding='cp949')

def IDmask(df, ID):
    mask = (df['kbo_bid']==ID) & (df['BatterTeam'] == 'SAM_LIO') & (df['PitchCall']=='InPlay')
    return df[mask]

df20 = IDmask(df20, 79402)
df21 = IDmask(df21, 79402)

def SwSp(df):
    mask = (df['Angle']>8) & (df['Angle']<32)
    return df[mask]

def HardHit(df):
    mask = (df['ExitSpeed']>152)
    return df[mask]

SwSp20 = SwSp(df20)
SwSp21 = SwSp(df21)
HH20 = HardHit(df20)
HH21 = HardHit(df21)

print("2020 SwSp%% = %.1f, HH%% = %.1f" % (100*len(SwSp20.index)/len(df20.index), 100*len(HH20.index)/len(df20.index)))
print("2021 SwSp%% = %.1f, HH%% = %.1f" % (100*len(SwSp21.index)/len(df21.index), 100*len(HH21.index)/len(df21.index)))