# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager, rc
import seaborn as sns

matplotlib.rcParams['axes.unicode_minus'] = False

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

df_init = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\2021KBOwithFutures.csv', index_col=False, encoding='cp949')

mask = (df_init.PitcherTeam == 'SAM_LIO') & (df_init.Inning > 6)
df = df_init[mask]
df.loc[df.Pitcher == '원태인', 'Pitcher'] = 'Won, Tae In'
df.loc[df.Pitcher == '임현준', 'Pitcher'] = 'Lim, Hyun Jun'
df.loc[df.Pitcher == '김대우', 'Pitcher'] = 'Kim, Dae Woo'
df.loc[df.Pitcher == '양창섭', 'Pitcher'] = 'Yang, Chang Seop'
df.loc[df.Pitcher == '최지광', 'Pitcher'] = 'Choi, Ji Guang'
df.loc[df.Pitcher == '우규민', 'Pitcher'] = 'Woo, Kyu Min'
df.loc[df.Pitcher == '장필준', 'Pitcher'] = 'Jang, Pill Joon'
df.loc[df.Pitcher == '오승환', 'Pitcher'] = 'Oh, Seung Hwan'
df.loc[df.Pitcher == '백정현', 'Pitcher'] = 'Baek, Jung Hyun'

mask_2outs = (df.Outs == 2)
df_2outs = df[mask_2outs]

#%% 전체/2아웃 구속 분포 비교
sns.distplot(df['RelSpeed'], color="blue", label="전체")
sns.distplot(df_2outs['RelSpeed'], color="red", label="2아웃")
plt.ylabel('구속 비율')
plt.xlabel('구속')
plt.legend(loc='upper left')
plt.title('전체/2아웃 구속 분포 비교')
plt.show()

#%% 전체/2아웃 로케이션 비교

fig, ax = plt.subplots(2, 1, figsize=(7,10), constrained_layout=True)


ax[0].plot('PlateLocSide', 'PlateLocHeight', data=df, marker='o', alpha=0.1, color='blue', linestyle='none')
ax[0].set_title('전체 투구 로케이션')
ax[0].set_ylabel('수직 로케이션')
ax[0].set_xlabel('수평 로케이션')
ax[0].grid(True)

ax[1].plot('PlateLocSide', 'PlateLocHeight', data=df_2outs, marker='o', alpha=0.1, color='red', linestyle='none')
ax[1].set_title('\n2아웃 이후 투구 로케이션')
ax[1].set_ylabel('수직 로케이션')
ax[1].set_xlabel('수평 로케이션')
ax[1].grid(True)

HorMean = np.mean(df.PlateLocSide)
VerMean = np.mean(df.PlateLocHeight)
HorSD = np.std(df.PlateLocSide)
VerSD = np.std(df.PlateLocHeight)

HorMean_2outs = np.mean(df_2outs.PlateLocSide)
VerMean_2outs = np.mean(df_2outs.PlateLocHeight)
HorSD_2outs = np.std(df_2outs.PlateLocSide)
VerSD_2outs = np.std(df_2outs.PlateLocHeight)

print("Overall: Mean = (%.1f, %.1f), SD = (%.1f, %.1f)" % (HorMean, VerMean, HorSD, VerSD))
print("After 2 outs: Mean = (%.1f, %.1f), SD = (%.1f, %.1f)" % (HorMean_2outs, VerMean_2outs, HorSD_2outs, VerSD_2outs))

#%%
fig1 = plt.figure(figsize = (7,10))
ax1 = plt.subplot(2,1,1)
ax1 = sns.kdeplot(df['PlateLocSide'], label='전체', color='blue')
ax1 = sns.kdeplot(df_2outs['PlateLocSide'], label='2아웃', color='red')

ax2 = plt.subplot(2,1,2)
ax2 = sns.kdeplot(df['PlateLocHeight'], label='전체', color='blue')
ax2 = sns.kdeplot(df_2outs['PlateLocHeight'], label='2아웃', color='red')
plt.show()

#%% 전체/2아웃 zone percentage
maskZone = (df.PlateLocHeight > 0.4572) & (df.PlateLocHeight < 1.0668) & (df.PlateLocSide > -0.254) & (df.PlateLocSide < 0.254)
dfZone = df[maskZone]

maskZone_2outs = (df_2outs.PlateLocHeight > 0.4572) & (df_2outs.PlateLocHeight < 1.0668) & (df_2outs.PlateLocSide > -0.254) & (df_2outs.PlateLocSide < 0.254)
dfZone_2outs = df_2outs[maskZone_2outs]

print("Overall zone percentage = %.1f%%" % (100*len(dfZone.index)/len(df.index)))
print("Zone percentage after 2 outs = %.1f%%" % (100*len(dfZone_2outs.index)/len(df_2outs.index)))

#%% 전체/2아웃 무브먼트 비교

fig, ax = plt.subplots(2, 1, figsize=(7,10), constrained_layout=True)


ax[0].plot('HorzBreak', 'InducedVertBreak', data=df, marker='o', alpha=0.1, color='blue', linestyle='none')
ax[0].set_title('전체 투구 무브먼트')
ax[0].set_ylabel('수직 무브먼트')
ax[0].set_xlabel('수평 무브먼트')
ax[0].grid(True)

ax[1].plot('HorzBreak', 'InducedVertBreak', data=df_2outs, marker='o', alpha=0.1, color='red', linestyle='none')
ax[1].set_title('\n2아웃 이후 투구 무브먼트')
ax[1].set_ylabel('수직 무브먼트')
ax[1].set_xlabel('수평 무브먼트')
ax[1].grid(True)
