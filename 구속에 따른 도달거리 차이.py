# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 14:11:38 2021

@author: LIONS
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
import matplotlib

matplotlib.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', index_col=False, encoding='cp949')
df = df.dropna(subset=['RelSpeed'])

df['radVRangle'] = np.pi*df['VertRelAngle']/180
df['radHRangle'] = np.pi*df['HorzRelAngle']/180
df['Acc'] = -2*(18.44 - df['Extension'] - df['RelSpeed']*np.cos(df['radVRangle'])*np.cos(df['radHRangle'])*(5/18)*df['ZoneTime'])/df['ZoneTime']**2

X = df[['RelSpeed']]
y = df['Acc']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.01)

lr = LinearRegression()
lr.fit(X_train, y_train)
grad = float(lr.coef_)
intercept = float(lr.intercept_)

df['AbsHRelAngle'] = np.abs(df['radHRangle'])

Extlist = df.Extension.tolist()
Extmean = sum(Extlist)/len(Extlist)
VRanglist = df.radVRangle.tolist()
VRangmean = sum(VRanglist)/len(VRanglist)
HRanglist = df.radHRangle.tolist()
HRangmean = sum(HRanglist)/len(HRanglist)

stdRS = np.cos(VRangmean)*np.cos(HRangmean)*150
stdAcc = grad*stdRS + intercept

comRS = np.cos(VRangmean)*np.cos(HRangmean)*130
comAcc = grad*comRS + intercept

stdT = (np.sqrt(stdRS**2+2*stdAcc*(18.44-Extmean))-stdRS)/stdAcc

comDT = comRS*stdT + comAcc*stdT**2/2

Diff = 18.44 - Extmean - comDT
print("Difference in distance = ", Diff)