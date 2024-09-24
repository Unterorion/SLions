# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 13:13:27 2021

@author: LIONS
"""

import pandas as pd

df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv")
df = df[df['Level'] == 'KBO']
df = df[df['PitchCall']=='InPlay']

pt = df.pivot_table(index='PlayResult', values='RE24_change', aggfunc='mean')