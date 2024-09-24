# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 12:40:26 2021

@author: LIONS
"""

import pandas as pd

df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\AAA2021.csv", index_col=False, encoding='cp949')

ptypelist = ['Slider', 'Curveball', 'Sinker', 'Cutter', 'Changeup', 'Splitter', 'Fastball']

df['TaggedPitchType'].replace('ChangeUp', 'Changeup', inplace=True)
df['TaggedPitchType'].replace('Four-Seam', 'Fastball', inplace=True)

for ptype in ptypelist:
    dfp = df[df.TaggedPitchType == ptype]
    
    maskS = (df.PitchCall=='StrikeSwinging')|(df.PitchCall=='InPlay')|(df.PitchCall=='FoulBall')
    maskW = (df.PitchCall=='StrikeSwinging')
    dfS = dfp[maskS]
    dfW = dfp[maskW]
    
    print("%s AAA 평균 헛스윙률 = %.3f%%" % (ptype, 100*len(dfW.index)/len(dfS.index)))