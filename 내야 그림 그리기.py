# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 10:31:19 2021

@author: LIONS
"""

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, figsize=(10,10), constrained_layout=True)

ax.plot([27.44, 27.44], [0, 27.44], linewidth=2, color='black')
ax.plot([0, 27.44], [27.44, 27.44], linewidth=2, color='black')

lin = np.sqrt(28.96**2-18.47**2/2)
ang = np.arccos((28.96**2+lin**2-18.47**2/2)/(2*28.96*lin))
theta = np.linspace(-ang, np.pi/2+ang)
arcx = 18.47/np.sqrt(2)+28.96*np.cos(theta)
arcy = 18.47/np.sqrt(2)+28.96*np.sin(theta)
ax.plot(arcx, arcy, linewidth=2, color='black')

th = 18.47/np.sqrt(2)+lin
ax.plot([0, th], [0, 0], linewidth=2, color='black')
ax.plot([0, 0], [0, th], linewidth=2, color='black')

ax.axis('off')
plt.savefig("C:\\Users\\LIONS\\Desktop\\참고용\\내야.png")