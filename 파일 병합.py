# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 10:39:14 2021

@author: LIONS
"""

import pandas as pd
import glob
import os

#df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\AAA2021.csv', index_col=False)
inputroute = r'C:\\Users\\kimyj\\OneDrive\\바탕 화면\\2021황사기'
outputroute = r'C:\\Users\\kimyj\\OneDrive\\바탕 화면\\2021황사기 종합.csv'

allfilelist = glob.glob(os.path.join(inputroute, '*csv'))
allData = []
for file in allfilelist:
    temp = pd.read_csv(file)
    allData.append(temp)
#%%
add = pd.concat(allData, ignore_index=True)
#add = add[['PitchUID', 'ClusterName']]
#%%
#final = pd.merge(df, add, how='outer', on=['PitchUID'])
add.to_csv(outputroute, index=False)