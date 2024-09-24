# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 14:13:01 2021

@author: LIONS
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc
from sklearn.linear_model import LinearRegression

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', encoding='cp949')

graphind = list(range(5))

ID = 79402
name = '김상수'
career = 0.308

mask = (df['kbo_bid'] == ID) & (df['BatterTeam'] == 'SAM_LIO')
df_indi = df[mask]

df_indi['NewTime'] = None

for i in range(len(df_indi.index)):
    time = str(df_indi['Time'].iloc[i])
    if time[0] != '0':
        if time[0:2] != '10' and time[0:2] != '11':
            df_indi['NewTime'].iloc[i] = '0' + time
        else:
            df_indi['NewTime'].iloc[i] = time
    else:
        df_indi['NewTime'].iloc[i] = time

df_indi['Datetime'] = None

for i in range(len(df_indi.index)):
    date = str(df_indi['Date'].iloc[i])
    time = str(df_indi['Time'].iloc[i])
    df_indi['Datetime'].iloc[i] = date + " " + time

df_indi = df_indi.sort_values(by='Datetime')
df_indi = df_indi.drop_duplicates(['Datetime'])

datedf = df_indi['Date'].drop_duplicates()
datesList = datedf.tolist()

InpNum = 0
HitNum = 0
BABIPlist = []

for date in datesList:
    mask_Inp = (df_indi['Date'] == date) & (df_indi['PitchCall'] == 'InPlay') & (df_indi['PlayResult'] != 'HomeRun') & (df_indi['PlayResult'] != 'Sacrifice')
    df_Inp = df_indi[mask_Inp]
    InpNum += len(df_Inp.index)
    
    maskHit = (df_Inp['PlayResult'] != 'Out') & (df_Inp['PlayResult'] != 'Error') & (df_indi['PlayResult'] != 'FieldersChoice')
    df_Hit = df_Inp[maskHit]
    HitNum += len(df_Hit.index)
    BABIPlist.append(HitNum/InpNum)

now = HitNum/InpNum
graphlim = len(datesList)

dateind = []
for ind in graphind:
    dateind.append(datesList[ind*len(datesList)//5])
dateind.append(datesList[len(datesList)-1])

fig, ax = plt.subplots(1, figsize=(6,5), constrained_layout=True)
ax.set_xlim(0, graphlim)
ax.set_ylim(0, 0.5)
ax.plot([0,graphlim], [career, career], color='green', linewidth=2, linestyle='--', label='통산 BABIP')
ax.plot(datesList, BABIPlist, color='blue', label='올해 BABIP 변화')
ax.set_title("%s 21시즌 날짜 별 BABIP\n" % name, fontsize = 20)
ax.set_xticks(dateind)
plt.xticks(rotation=45, ha='center')
ax.grid('off')

DateInd = list(range(graphlim))
recentDict = {'Dates':DateInd, 'BABIP':BABIPlist}
recentDF = pd.DataFrame(recentDict)

X = recentDF['Dates']
y = recentDF['BABIP']

line_fitter = LinearRegression()
line_fitter.fit(X.values.reshape(-1,1), y)

ax.plot(X,line_fitter.predict(X.values.reshape(-1,1)), color='orange', linestyle='--', label='올해 BABIP 변화 경향')
ax.legend(loc='lower right')
plt.text(graphlim+1, now, '현재 %.3f' % now, color='blue', fontsize=10)
plt.text(graphlim+1, career, '통산 %.3f' % career, color='green', fontsize=10)
plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\7월 4주\\%s 바빕.png" % name, dpi=100)