# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 13:47:08 2021

@author: LIONS
"""

import pandas as pd
import numpy as np

df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', index_col=False, encoding='cp949')
df = df.dropna(subset = ['RelSpeed'])

pID = 50411
cID = 60768

for ID in [pID, cID]:
    dfi = df[df.PitcherId == ID]
    RHlist = dfi.RelHeight.tolist()
    RSlist = dfi.RelSide.tolist()
    
    RHmean = np.mean(RHlist)
    RSmean = np.mean(RSlist)
    
    RHstd = np.std(RHlist)
    RSstd = np.std(RSlist)
    
    RelLen = np.sqrt(RHmean**2 + RSmean**2)
    RelAng = np.arctan(RSmean/RHmean)*180/np.pi
    
    name = dfi.PitName1.iloc[0]
    
    print("%s 릴리즈 길이 = %f, 릴리즈 각도 = %f, 표준편차 = 수직 %f, 수평 %f" % (name, RelLen, RelAng, RHstd/RHmean, RSstd/RSmean))