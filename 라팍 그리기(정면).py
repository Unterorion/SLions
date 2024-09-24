# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 16:44:38 2021

@author: LIONS
"""

import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, figsize=(10,10), constrained_layout=True)

ax.set_xlim(-99.5/np.sqrt(2), 99.5/np.sqrt(2))
ax.set_ylim(0, 99.5*np.sqrt(2))
ax.axis('off')

ax.plot([-99.5/np.sqrt(2),0], [99.5/np.sqrt(2),0], linewidth=2, color='black')
ax.plot([0,99.5/np.sqrt(2)], [0,99.5/np.sqrt(2)], linewidth=2, color='black')
ax.plot([-99.5/np.sqrt(2),122.5-99.5*np.sqrt(2)], [99.5/np.sqrt(2),122.5], linewidth=2, color='black')
ax.plot([99.5*np.sqrt(2)-122.5,99.5/np.sqrt(2)], [122.5,99.5/np.sqrt(2)], linewidth=2, color='black')
ax.plot([122.5-99.5*np.sqrt(2),99.5*np.sqrt(2)-122.5],[122.5,122.5], linewidth=2, color='black')

x_bd = np.linspace(-38.91/np.sqrt(2), 38.91/np.sqrt(2))
y_bd = 18.47 + np.sqrt(28.96**2 - x_bd**2)
ax.plot(x_bd, y_bd, linewidth=1, color='black')

ax.plot([-27.44/np.sqrt(2),0], [27.44/np.sqrt(2),27.44*np.sqrt(2)], linewidth=1, color='black')
ax.plot([0,27.44/np.sqrt(2)], [27.44*np.sqrt(2),27.44/np.sqrt(2)], linewidth=1, color='black')

x_l = np.linspace(-99.5/np.sqrt(2),122.5-99.5*np.sqrt(2))
y_l1 = 99.5*np.sqrt(2) - np.abs(x_l)
y_l2 = np.abs(x_l)
x_c = np.linspace(122.5-99.5*np.sqrt(2), 99.5*np.sqrt(2)-122.5)
y_c1 = 122.5 + 0*x_c
y_c2 = np.abs(x_c)
x_r = np.linspace(99.5*np.sqrt(2)-122.5, 99.5/np.sqrt(2))
y_r1 = 99.5*np.sqrt(2) - np.abs(x_r)
y_r2 = np.abs(x_r)
plt.fill_between(x_l, y_l1, y_l2, color='lightgreen')
plt.fill_between(x_c, y_c1, y_c2, color='lightgreen')
plt.fill_between(x_r, y_r1, y_r2, color='lightgreen')

y_bd2 = np.abs(x_bd)
plt.fill_between(x_bd, y_bd, y_bd2, color='red', alpha=0.5)

x_inf = np.linspace(-27.44/np.sqrt(2), 27.44/np.sqrt(2))
y_inf1 = 27.44*np.sqrt(2) - np.abs(x_inf)
y_inf2 = np.abs(x_inf)
plt.fill_between(x_inf, y_inf1, y_inf2, color='lightgreen')