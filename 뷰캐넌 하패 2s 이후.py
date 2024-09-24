# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 14:40:43 2021

@author: LIONS
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc
import matplotlib

matplotlib.rcParams['axes.unicode_minus'] = False

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df = pd.read_csv("C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv", index_col=None, encoding='cp949')
df = df[df['Level'] == 'KBO']
df.dropna(subset=['RelSpeed'], inplace=True)
df = df[df['kbo_pid'] == 50404]

indlist = []

for i in range(len(df.index)-1):
    if df['TaggedPitchType'].iloc[i]=='Fastball' and df['PlateLocHeight'].iloc[i]>0.9652 and df['PlateLocHeight'].iloc[i]<1.1684 and df['PlateLocSide'].iloc[i]>-0.3387 and df['PlateLocSide'].iloc[i]<0.3387:
        if df['Strikes'].iloc[i+1]==2:
            indlist.append(i)
            indlist.append(i+1)

result = df.iloc[indlist, :]

result = result[['BatName1', 'TaggedPitchType', 'PlateLocSide', 'PlateLocHeight', 'PitchCall', 'PlayResult', 'ExitSpeed', 'Angle']]

def color(p):
    if p == 'Cutter':
        return 'lightgreen'
    elif p == 'Curveball':
        return 'orange'
    elif p == 'ChangeUp' or p == 'Changeup':
        return 'blue'
    else:
        return 'red'

def translate(p):
    if p == 'Cutter':
        return '커터'
    elif p == 'Curveball':
        return '커브'
    elif p == 'ChangeUp' or p == 'Changeup':
        return '체인지업'
    else:
        return '직구'

result['KorPitchType'] = result['TaggedPitchType'].apply(translate)

for j in range(int(len(result.index)/2)):
    temp = result.iloc[[2*j, 2*j+1], :]
    
    fig, ax = plt.subplots(1, figsize=(10, 12), constrained_layout=True)
    ax.plot([-0.254, 0.254], [1.0668, 1.0668], color='black', linewidth=2)
    ax.plot([-0.254, 0.254], [0.4572, 0.4572], color='black', linewidth=2)
    ax.plot([-0.254, -0.254], [0.4572, 1.0668], color='black', linewidth=2)
    ax.plot([0.254, 0.254], [0.4572, 1.0668], color='black', linewidth=2)
    
    ax.plot([-0.3387, 0.3387], [0.9652, 0.9652], color='darkgreen', linewidth=1, ls='--')
    ax.plot([-0.3387, 0.3387], [1.1684, 1.1684], color='darkgreen', linewidth=1, ls='--')
    ax.plot([-0.3387, -0.3387], [0.9652, 1.1684], color='darkgreen', linewidth=1, ls='--')
    ax.plot([0.3387, 0.3387], [0.9652, 1.1684], color='darkgreen', linewidth=1, ls='--')
    
    ax.plot([-0.5,-0.43], [1.37, 1.37], color='darkgreen', linewidth=1, ls='--')
    ax.plot([-0.5,-0.43], [1.31, 1.31], color='darkgreen', linewidth=1, ls='--')
    ax.plot([-0.5,-0.5], [1.31, 1.37], color='darkgreen', linewidth=1, ls='--')
    ax.plot([-0.43,-0.43], [1.31, 1.37], color='darkgreen', linewidth=1, ls='--')
    ax.annotate("하이존", xy=(-0.42,1.34), va='center', ha='left', fontsize=20)
    
    ax.plot([-0.5,-0.43], [1.29, 1.29], color='black', linewidth=2)
    ax.plot([-0.5,-0.43], [1.23, 1.23], color='black', linewidth=2)
    ax.plot([-0.5,-0.5], [1.23, 1.29], color='black', linewidth=2)
    ax.plot([-0.43,-0.43], [1.23, 1.29], color='black', linewidth=2)
    ax.annotate("스트라이크존", xy=(-0.42,1.26), va='center', ha='left', fontsize=20)
        
    ax.set_xlim(-0.508, 0.508)
    ax.set_ylim(0.1524, 1.3716)
    ax.axis('off')
    
    for k in range(len(temp.index)):
        x = temp['PlateLocSide'].iloc[k]
        y = temp['PlateLocHeight'].iloc[k]
        if y<0.1524:
            y=0.1724
        elif y>1.3716:
            y=1.3516
        ptype = temp['TaggedPitchType'].iloc[k]
        ax.scatter(x, y, s=2000, alpha=0.5, c=color(ptype))
        ax.annotate(str(k+1), xy=(x,y), va='center', ha='center', fontsize=30)
        
        if k == 1:
            if x<0:
                ha='left'
                x += 0.02
            else:
                ha='right'
                x -= 0.02
            if y<0.762:
                va='bottom'
                y += 0.02
            else:
                va='top'
                y -= 0.02
            
            bat = temp['BatName1'].iloc[k]
            pt = temp['KorPitchType'].iloc[k]
            pc = temp['PitchCall'].iloc[k]
            pr = temp['PlayResult'].iloc[k]
            es = temp['ExitSpeed'].iloc[k]
            ang = temp['Angle'].iloc[k]
            
            if pc == 'StrikeCalled':
                res = '스트라이크'
            elif pc == 'BallCalled':
                res = '볼'
            elif pc == 'FoulBall':
                res = '파울'
            elif pc == 'InPlay':
                if pr == 'Single':
                    res = '단타'
                elif pr == 'Out':
                    if ang<8:
                        res = '땅볼 아웃'
                    elif ang>8:
                        res = '뜬공 아웃'
                    else:
                        res = '라이너 아웃'
            if pc != 'InPlay':
                ax.annotate("타자 : %s\n구종 : %s\n결과 : %s" % (bat, pt, res), xy=(x,y), va=va, ha=ha, fontsize=25)
            else:
                ax.annotate("타자 : %s\n구종 : %s\n결과 : %s\n타구속도 : %d\n발사각 : %d" % (bat, pt, res, es, ang), xy=(x,y), va=va, ha=ha, fontsize=25)
        
    ind = str(j)
    if len(ind) == 1:
        ind = '0'+ind
    plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\9월 4주\\뷰캐넌 결정구 2\\%s.png" % ind)