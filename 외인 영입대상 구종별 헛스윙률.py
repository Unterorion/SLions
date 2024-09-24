# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 12:16:39 2021

@author: LIONS
"""

import pandas as pd

df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\AAA2021.csv", index_col=False, encoding='cp949')
dfindi = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\외인 구종분류 2\\Wes Benjamin.csv", index_col=False, encoding='cp949')

ptypelist = dfindi.ClusterName.unique().tolist()

temp = pd.merge(df, dfindi, how='inner', on=['PitchUID'])

for ptype in ptypelist:
    dfp = temp[temp.ClusterName == ptype]
    Trate = len(dfp.index)/len(temp.index)
    
    maskS = (dfp.PitchCall=='StrikeSwinging')|(dfp.PitchCall=='InPlay')|(dfp.PitchCall=='FoulBall')
    maskW = (dfp.PitchCall=='StrikeSwinging')
    
    dfpS = dfp[maskS]
    dfpW = dfp[maskW]
    Wrate = len(dfpW.index)/len(dfpS.index)
    
    print(ptype)
    print("구사율 %.3f" % Trate)
    print("헛스윙률 %.3f" % Wrate)
    print("\n")