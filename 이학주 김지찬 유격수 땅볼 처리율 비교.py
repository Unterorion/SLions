# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 15:01:09 2021

@author: LIONS
"""

import pandas as pd

df = pd.read_csv('2021KBOwithFutures.csv', encoding='cp949')

maskLee = (df.Bearing > -20) & (df.Bearing < -5) & (df.PlayResult != 'Sacrifice') & (df.Angle < 8) & (df.HitType != 'FlyBall') & (df.PitchCall != 'FoulBall') & (df.pos_5 == '이학주')
dfLee = df[maskLee]
maskLee_out = (dfLee.PlayResult == 'Out')
dfLee_out = dfLee[maskLee_out]

maskKim = (df.Bearing > -20) & (df.Bearing < -5) & (df.PlayResult != 'Sacrifice') & (df.Angle < 8) & (df.HitType != 'FlyBall') & (df.PitchCall != 'FoulBall') & ((df.pos_5 != '이학주') & ((df.PitcherTeam == 'SAM_LIO') & (df.Date != ('06/05/2021')) & (df.Date != ('06/12/2021')) & (df.Date != ('06/13/2021')) & (df.Date != ('06/22/2021'))))
dfKim = df[maskKim]
maskKim_out = (dfKim.PlayResult == 'Out')
dfKim_out = dfKim[maskKim_out]

Lee_rate = 100*len(dfLee_out.index)/len(dfLee.index)
Kim_rate = 100*len(dfKim_out.index)/len(dfKim.index)

print("Lee rate = %.1f%%" % Lee_rate)
print("Kim rate = %.1f%%" % Kim_rate)