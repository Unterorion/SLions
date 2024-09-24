# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 18:24:07 2021

@author: LIONS
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

fig, ax = plt.subplots(1, figsize=(10,10), constrained_layout=True)

aIn = 28.96
cIn = 18.44/np.sqrt(2)
bIn = np.sqrt(aIn**2-cIn**2)
ref_angIn = np.arccos((aIn**2+bIn**2-cIn**2)/(2*aIn*bIn))
angIn = np.linspace(-ref_angIn, ref_angIn+np.pi/2)
ax.plot(cIn+aIn*np.cos(angIn), cIn+aIn*np.sin(angIn), color='black', linewidth=1)

# 쿠키커터형 구장
lrfence = 95 # 좌우펜스
cenfence = 118 # 중앙펜스

a = (cenfence**2-lrfence**2)/(2*np.sqrt(2)*cenfence-2*lrfence) # 외야펜스(원형) 중심 a,a
r = cenfence - np.sqrt(2)*a # 외야펜스(원형) 반경 r
ref_ang = np.arccos((r**2+(lrfence-a)**2-a**2)/(2*r*(lrfence-a)))

ang = np.linspace(-ref_ang, ref_ang+np.pi/2)# 외야펜스 중심에서 좌우까지 각범위

ax.plot([0, 0], [0, lrfence], color='black', linewidth=2)
ax.plot([0, lrfence], [0, 0], color='black', linewidth=2)
ax.plot(a+r*np.cos(ang), a+r*np.sin(ang), color='black', linewidth=2)
ax.plot([27.43, 27.43], [0, 27.43], color='black', linewidth=1)
ax.plot([0, 27.43], [27.43, 27.43], color='black', linewidth=1)
ax.set_xlim(0, 120)
ax.set_ylim(0, 120)

#%% 라팍

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

fig, ax = plt.subplots(1, figsize=(10,10), constrained_layout=True)

aIn = 28.96
cIn = 18.44/np.sqrt(2)
bIn = np.sqrt(aIn**2-cIn**2)
ref_angIn = np.arccos((aIn**2+bIn**2-cIn**2)/(2*aIn*bIn))
angIn = np.linspace(-ref_angIn, ref_angIn+np.pi/2)
ax.plot(cIn+aIn*np.cos(angIn), cIn+aIn*np.sin(angIn), color='black', linewidth=1)

ax.plot([0, 0], [0, 99.5], color='black', linewidth=2)
ax.plot([0, 99.5], [0, 0], color='black', linewidth=2)
ax.plot([99.5, 99.5], [0, 122*np.sqrt(2)-99.5], color='black', linewidth=2)
ax.plot([0, 122*np.sqrt(2)-99.5], [99.5, 99.5], color='black', linewidth=2)
ax.plot([122*np.sqrt(2)-99.5, 99.5], [99.5, 122*np.sqrt(2)-99.5], color='black', linewidth=2)
ax.plot([27.43, 27.43], [0, 27.43], color='black', linewidth=1)
ax.plot([0, 27.43], [27.43, 27.43], color='black', linewidth=1)
ax.set_xlim(0, 120)
ax.set_ylim(0, 120)

#%% 타 구장/라팍 비교

fig, ax = plt.subplots(1, figsize=(10,10), constrained_layout=True)

ax.plot([0, 0], [0, 99.5], color='red', linewidth=2)
ax.plot([0, 99.5], [0, 0], color='red', linewidth=2)
ax.plot([99.5, 99.5], [0, 122*np.sqrt(2)-99.5], color='red', linewidth=2)
ax.plot([0, 122*np.sqrt(2)-99.5], [99.5, 99.5], color='red', linewidth=2)
ax.plot([122*np.sqrt(2)-99.5, 99.5], [99.5, 122*np.sqrt(2)-99.5], color='red', linewidth=2)

ax.plot([0, 0], [0, lrfence], color='black', linewidth=2)
ax.plot([0, lrfence], [0, 0], color='black', linewidth=2)
ax.plot(a+r*np.cos(ang), a+r*np.sin(ang), color='black', linewidth=2)
ax.plot([27.43, 27.43], [0, 27.43], color='black', linewidth=1)
ax.plot([0, 27.43], [27.43, 27.43], color='black', linewidth=1)
ax.set_xlim(0, 120)
ax.set_ylim(0, 120)
