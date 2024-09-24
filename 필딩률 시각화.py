# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

fieldingrate = pd.read_csv('C:\\Users\\kimyj\\OneDrive\\바탕 화면\\2021 내야 구간 별 땅볼 처리율.csv', index_col=False)

#fieldingrate.columns = ['section', 'fielding rate', 'to be dropped']
#fieldingrate.drop('to be dropped', axis = 1, inplace = True)
#fieldingrate.columns = ['section', 'fielding rate']


'''SectionList = ['%d' % (i+1) for i in range(len(fieldingrate))]
PercList = [fieldingrate.iloc[i][1] for i in range(len(fieldingrate))]

fig = plt.figure(figsize=(20,10))
fig.set_facecolor('white')
ax = fig.add_subplot()

ax.bar(SectionList, PercList)
plt.title('내야 구간 별 필딩률')
plt.show()'''

#%%
fig, ax = plt.subplots(1, figsize=(10,10), constrained_layout=True)
x1 = np.linspace(-100,100,2000)
bl1 = np.abs(x1)
x2 = np.linspace(-90/np.sqrt(2), +90/np.sqrt(2), 1000)
bl2 = 90*np.sqrt(2)-np.abs(x2)
x3 = np.linspace(-90.23, 90.23, 2000)
bl3 = 60.5+np.sqrt(95**2-x3**2)
x4 = np.linspace(-80, 80, 100)
bl4 = -np.abs(x4)

ax.plot(x1, bl1, color='black', linewidth=2)
ax.plot(x2, bl2, color='black', linewidth=2)
ax.plot(x3, bl3, color='black', linewidth=2)
#ax.plot(x4, bl4, color='white', linewidth=2)

ang = []
ang_n = []

for i in range(len(fieldingrate)):
    ang.append((135-5*i)*np.pi/180)
    ang_n.append((135-5*i)*np.pi/180 - np.pi/36)

for i in range(len(fieldingrate)):
    if i < 9:
        # x**2 + (np.tan(ang[i])*x - 60.5)**2 = 95**2
        # (1+(np.tan(ang[i]))**2)*x**2 - 121*np.tan(ang[i])*x + 60.5**2 - 95**2 = 0
        th1 = (121*np.tan(ang[i])-np.sqrt((121*np.tan(ang[i]))**2-4*(1+(np.tan(ang[i]))**2)*(60.5**2-95**2)))/(2*(1+(np.tan(ang[i]))**2))
        th2 = (121*np.tan(ang_n[i])-np.sqrt((121*np.tan(ang_n[i]))**2-4*(1+(np.tan(ang_n[i]))**2)*(60.5**2-95**2)))/(2*(1+(np.tan(ang_n[i]))**2))
        x1 = np.linspace(th1, th2)
        x2 = np.linspace(th2, 0)
        # x**2 + (y-60.5)**2 = 95**2
        y01 = np.tan(ang[i])*x1
        y02 = np.tan(ang[i])*x2
        y1 = 60.5+np.sqrt(95**2-x1**2)
        y2 = np.tan(ang_n[i])*x2
        ax.plot(x1,y01, color='black', linewidth=0.5)
        ax.plot(x2,y02, color='black', linewidth=0.5)
        ax.plot(x1,y1, color='black', linewidth=0.5)
        ax.plot(x2,y2, color='black', linewidth=0.5)
        if fieldingrate['FieldingRate'][i] < 66.8:
            c = 'blue'
            a = (66.8-fieldingrate['FieldingRate'][i])/30
        else:
            c = 'red'
            a = (fieldingrate['FieldingRate'][i]-66.8)/30
        plt.fill_between(x1, y01, y1, color=c, alpha=a)
        plt.fill_between(x2, y02, y2, color=c, alpha=a)
        
        text = "%d%%" % (fieldingrate['FieldingRate'][i])
        ltang = (ang[i]+ang_n[i])/2
        ltx = (121*np.tan(ltang)-np.sqrt((121*np.tan(ltang))**2-4*(1+(np.tan(ltang))**2)*(60.5**2-95**2)))/(2*(1+(np.tan(ltang))**2))
        lty = ltx*np.tan(ltang)
        ltx -= 9 - 0.5*i
        lty += 2
        if 4<i<8:
            plt.text(ltx, lty, text, size=17, color='red')
        else:
            plt.text(ltx, lty, text, size=13)
    else:
        th1 = (121*np.tan(ang[i])+np.sqrt((121*np.tan(ang[i]))**2-4*(1+(np.tan(ang[i]))**2)*(60.5**2-95**2)))/(2*(1+(np.tan(ang[i]))**2))
        th2 = (121*np.tan(ang_n[i])+np.sqrt((121*np.tan(ang_n[i]))**2-4*(1+(np.tan(ang_n[i]))**2)*(60.5**2-95**2)))/(2*(1+(np.tan(ang_n[i]))**2))
        x1 = np.linspace(0, th1)
        x2 = np.linspace(th1, th2)
        y01 = np.tan(ang_n[i])*x1
        y02 = np.tan(ang_n[i])*x2
        y1 = np.tan(ang[i])*x1
        y2 = 60.5+np.sqrt(95**2-x2**2)
        ax.plot(x1,y01, color='black', linewidth=0.5)
        ax.plot(x2,y02, color='black', linewidth=0.5)
        ax.plot(x1,y1, color='black', linewidth=0.5)
        ax.plot(x2,y2, color='black', linewidth=0.5)
        if fieldingrate['FieldingRate'][i] < 66.8:
            c = 'blue'
            a = (66.8-fieldingrate['FieldingRate'][i])/30
        else:
            c = 'red'
            a = (fieldingrate['FieldingRate'][i]-66.8)/30
        plt.fill_between(x1, y01, y1, color=c, alpha=a)
        plt.fill_between(x2, y02, y2, color=c, alpha=a)
        
        text = "%d%%" % (fieldingrate['FieldingRate'][i])
        ltang = (ang[i]+ang_n[i])/2
        ltx = (121*np.tan(ltang)+np.sqrt((121*np.tan(ltang))**2-4*(1+(np.tan(ltang))**2)*(60.5**2-95**2)))/(2*(1+(np.tan(ltang))**2))
        lty = ltx*np.tan(ltang)
        ltx -= 9-0.5*i
        lty += 2
        plt.text(ltx, lty, text, size=13)

ax.axis('off')

#plt.title("\n리그 내야 땅볼 처리율\n2021", size=50)
plt.title("\n\n", size=50)
#plt.text(-100, 20, "이학주 처리율 : 73.2%", size=20)
#plt.text(-100, 10, "김지찬 처리율 : 79.2%", size=20)
#plt.savefig('2021 내야 구간 별 필딩률(리그 전체).jpg')