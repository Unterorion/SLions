# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 17:21:30 2021

@author: LIONS
"""

import pandas as pd

df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', index_col=False, encoding='cp949')
df = df.dropna(subset=['Angle'])
maskKBO = (df['BatterTeam']=='SAM_LIO')|(df['BatterTeam']=='KIW_HER')|(df['BatterTeam']=='HAN_EAG')|(df['BatterTeam']=='KT_WIZ')|(df['BatterTeam']=='LOT_GIA')|(df['BatterTeam']=='KIA_TIG')|(df['BatterTeam']=='DOO_BEA')|(df['BatterTeam']=='NC_DIN')|(df['BatterTeam']=='LG_TWI')|(df['BatterTeam']=='SSG_LAN')
df_KBO = df[maskKBO]
maskInPlay = (df_KBO['PitchCall']=='InPlay') & (df_KBO['Bearing']>-45) & (df_KBO['Bearing']<45)
df_inPlay = df_KBO[maskInPlay] # 인플레이 타구 전체

maskAllHit = (df_inPlay['PlayResult']!='Out')
df_allHit = df_inPlay[maskAllHit]

BA_All = len(df_allHit.index)/len(df_inPlay.index)

# 스윗스팟
maskSwSp = (df_inPlay['Angle']>8) & (df_inPlay['Angle']<32)
df_SwSp = df_inPlay[maskSwSp]

maskSwSpHit = (df_SwSp['PlayResult']!='Out')
df_SwSpHit = df_SwSp[maskSwSpHit]

BA_SwSp = len(df_SwSpHit.index)/len(df_SwSp.index)

print("BA for all batted ball = %f" % BA_All)
print("BA at sweet spot = %f" % BA_SwSp)

df_inPlay['TB'] = 0
df_SwSp['TB'] = 0

for i in range(len(df_inPlay.index)):
    if df_inPlay["PlayResult"].iloc[i] == 'Single':
        df_inPlay["TB"].iloc[i] = 1
    elif df_inPlay["PlayResult"].iloc[i] == 'Double':
        df_inPlay["TB"].iloc[i] = 2
    elif df_inPlay["PlayResult"].iloc[i] == 'Triple':
        df_inPlay["TB"].iloc[i] = 3
    elif df_inPlay["PlayResult"].iloc[i] == 'HomeRun':
        df_inPlay["TB"].iloc[i] = 4

for i in range(len(df_SwSp.index)):
    if df_SwSp["PlayResult"].iloc[i] == 'Single':
        df_SwSp["TB"].iloc[i] = 1
    elif df_SwSp["PlayResult"].iloc[i] == 'Double':
        df_SwSp["TB"].iloc[i] = 2
    elif df_SwSp["PlayResult"].iloc[i] == 'Triple':
        df_SwSp["TB"].iloc[i] = 3
    elif df_SwSp["PlayResult"].iloc[i] == 'HomeRun':
        df_SwSp["TB"].iloc[i] = 4

SLG_inPlay = sum(df_inPlay["TB"])/len(df_inPlay.index)
SLG_SwSp = sum(df_SwSp["TB"])/len(df_SwSp.index)

print("SLG for all batted ball = %f" % SLG_inPlay)
print("SLG at sweet spot = %f" % SLG_SwSp)

#%% 배럴타구

maskBarrel = ((df_inPlay['ExitSpeed']>185.6) & (df_inPlay['Angle']>8) & (df_inPlay['Angle']<50)) | ((df_inPlay['ExitSpeed']>156.8) & (df_inPlay['ExitSpeed']<185.6) & (df_inPlay['Angle']>26-0.625*(df_inPlay['ExitSpeed']-156.8)) & (df_inPlay['Angle']<30+0.694*(df_inPlay['ExitSpeed']-156.8)))
df_Barrel = df_inPlay[maskBarrel]

#mask_BarrelHit = (df_Barrel['TB'] != 0)
#df_BarrelHit = df_Barrel[mask_BarrelHit]
df_BarrelHit = df_Barrel[df_Barrel['TB'] != 0]

BA_Barrel = len(df_BarrelHit.index)/len(df_Barrel.index)
SLG_Barrel = sum(df_Barrel['TB'])/len(df_Barrel.index)

print("BA for barrels = %f" % BA_Barrel)
print("SLG for barrels = %f" % SLG_Barrel)

#%% 강한 타구

df_hardhit = df_inPlay[df_inPlay['ExitSpeed']>155]
df_hardhithit = df_hardhit[df_hardhit['PlayResult'] != 'Out']

BA_HH = len(df_hardhithit.index)/len(df_hardhit.index)
SLG_HH = sum(df_hardhit['TB'])/len(df_hardhit.index)

print("BA for hard-hit balls = %f" % BA_HH)
print("SLG for hard-hit balls = %f" % SLG_HH)