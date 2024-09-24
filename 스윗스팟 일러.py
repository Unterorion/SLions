# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 14:15:29 2021

@author: LIONS
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

fig, ax = plt.subplots(1, figsize=(6.3,10), constrained_layout=True)
ax.set_xlim(0,1.2)
ax.set_ylim(-1,1)

y1 = np.linspace(0, np.sin(8*np.pi/180))
x11 = y1/np.tan(32*np.pi/180)
x12 = y1/np.tan(8*np.pi/180)

y2 = np.linspace(np.sin(8*np.pi/180), np.sin(32*np.pi/180))
x21 = y2/np.tan(32*np.pi/180)
x22 = np.sqrt(1-y2**2)

plt.fill_betweenx(y1, x11, x12, alpha=0.3, facecolor='red', edgecolor='face')
plt.fill_betweenx(y2, x21, x22, alpha=0.3, facecolor='red', edgecolor='face')

plt.annotate('', xy=(np.cos(8*np.pi/180),np.sin(8*np.pi/180)), xytext=(0,0), arrowprops=dict(arrowstyle='->', color='black', lw=5))
plt.annotate('', xy=(np.cos(32*np.pi/180),np.sin(32*np.pi/180)), xytext=(0,0), arrowprops=dict(arrowstyle='->', color='black', lw=5))
plt.annotate('8도', xy=(1.1*np.cos(8*np.pi/180), 1.1*np.sin(8*np.pi/180)), rotation=8, va='center', ha='center', fontsize=30)
plt.annotate('32도', xy=(1.12*np.cos(32*np.pi/180), 1.12*np.sin(32*np.pi/180)), rotation=32, va='center', ha='center', fontsize=30)
plt.annotate('Sweet Spot', xy=(0.65*np.cos(20*np.pi/180), 0.65*np.sin(20*np.pi/180)), rotation=20, va='center', ha='center', fontsize=40)

xunder = np.linspace(0, np.cos(32*np.pi/180))
yunder1 = np.sqrt(1-xunder**2)
yunder2 = np.tan(32*np.pi/180)*xunder
plt.fill_between(xunder, yunder1, yunder2, alpha=0.3, color='blue')

'''ytop1 = np.linspace(-1, 0)
xtop11 = np.sqrt(1-ytop1**2)
xtop12 = 0*ytop1
ytop2 = np.linspace(0, np.sin(8*np.pi/180))
xtop21 = np.sqrt(1-ytop2**2)
xtop22 = ytop2/np.tan(8*np.pi/180)
plt.fill_betweenx(ytop1, xtop11, xtop12, alpha=0.3, color='blue')
plt.fill_betweenx(ytop2, xtop21, xtop22, alpha=0.3, color='blue')'''

ytop3 = np.linspace(-1, np.sin(8*np.pi/180))
xtop31 = np.sqrt(1-ytop3**2)
xtop32 = ytop3/np.tan(8*np.pi/180)
plt.fill_betweenx(ytop3, xtop31, xtop32, alpha=0.3, color='blue')

ax.axis('off')
ax.grid('off')