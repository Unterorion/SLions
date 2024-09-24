# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 17:38:39 2020

@author: user
"""

import pandas as pd
from sklearn import preprocessing
from sklearn.mixture import GaussianMixture as GMM

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

import glob
import os
from matplotlib import font_manager, rc
import matplotlib

matplotlib.rcParams['axes.unicode_minus'] = False

font_path = "c:/Windows/Fonts/malgun.ttf"
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)

'''input_file = r'C:\\Users\\LIONS\\Desktop\\고교야구\\고교야구 0628'
output_file = r'C:\\Users\\LIONS\\Desktop\\고교야구\\고교야구 0628\\통합.csv'

allFileList = glob.glob(os.path.join(input_file, '2021*'))
allData = []
for file in allFileList:
    df = pd.read_csv(file)
    allData.append(df)

dataCombined = pd.concat(allData, axis=0, ignore_index=False)
dataCombined.to_csv(output_file, index=False)'''



df = pd.read_csv('C:\\Users\\LIONS\\.spyder-py3\\9월 3주\\0818AAA.csv', index_col=False, encoding='cp949')

#df=pd.read_csv('D:\\trackman\\AAA\\2021\\merging\\AAA2021.csv', index_col=False)

#df=df[(df['TaggedPitchType']=='Fastball') | (df['TaggedPitchType']=='Sinker') | (df['TaggedPitchType']=='ChangeUp')]

'''idmap = pd.read_excel('C:\\Users\\LIONS\\Desktop\\고교야구\\idmap_update_아마추어.xlsx', index_col=False)
idmap.drop_duplicates(inplace=True)'''

dfcopy=df.copy()

df.dropna(subset=['PitcherId', 'BatterId'], how='any', inplace=True)

df.reset_index(inplace=True)

df['PitcherId']=df['PitcherId'].astype(int)
df['BatterId']=df['BatterId'].astype(int)


'''pitidmap=idmap[['PitcherId', 'PitName1']]
batidmap=idmap[['BatterId', 'BatName1']]'''
pitidmap = df[['Pitcher', 'PitcherId']].drop_duplicates(subset=['PitcherId'])
id_index_pitidmap=pitidmap.set_index('PitcherId')

#df = pd.merge(df, pitidmap, how='left', on='PitcherId')
#df = pd.merge(df, batidmap, how='left', on='BatterId')

pitidmap = df[['Pitcher', 'PitcherId']]
pitidmap.drop_duplicates(inplace=True)
id_index_pitidmap=pitidmap.set_index('PitcherId')

df.dropna(subset=['RelSpeed', 'SpinRate', 'HorzBreak', 'InducedVertBreak', 'BatterId', 'ZoneTime'], how='any', inplace=True)


def coloring(x):
    if x==0:
        return 'red'
    if x==1:
        return 'blue'
    if x==2:
        return 'green'
    if x==3:
        return 'black'
    if x==4:
        return 'yellow'
    if x==5:
        return 'brown'
    if x==6:
        return 'purple'
    
def coloring2(x):
    if x=='Fastball':
        return 'red'
    if x=='Slider':
        return 'darkgreen'
    if x=='Curveball':
        return 'orange'
    if x=='ChangeUp':
        return 'blue'
    if x=='Splitter':
        return 'brown'
    if x=='Cutter':
        return 'lightgreen'
    if x=='Sinker':
        return 'purple'
    if x=='Knuckleball':
        return 'gray'

def rotate(angle):
    ax.view_init(azim=angle)




#temp=df[df['kbo_pid'].isna()==True]

#print(temp.kbo_pid.unique().tolist())

#print(temp.Pitcher.unique().tolist())

#df.dropna(subset=['kbo_pid'], how='any', inplace=True)

df.reset_index(inplace=True)

#pitid=df.PitcherId.unique().tolist()

pitid = [623454,605138,621112,547176,608650,642659,656457,656725,596049,596071,592716,626929,621097,643615,605541]

yimsi=pd.DataFrame(columns=['RelSpeed', 'HorzBreak', 'InducedVertBreak', 'ZoneTime', 'Cluster', 'ClusterName', 'PitchUID'])

idList = pitidmap['PitcherId'].tolist()

for j in pitid:
    
    
    if j in idList:
        name = id_index_pitidmap.loc[j, 'Pitcher']
    else:
        continue
    print(name)
    
    tempdf=df[df['PitcherId']==j]
    
    X=tempdf[['RelSpeed', 'SpinRate', 'HorzBreak', 'InducedVertBreak', 'ZoneTime']]
    Y=tempdf[['PitcherId', 'TaggedPitchType', 'AutoPitchType','RelSpeed', 'SpinRate', 'HorzBreak', 'InducedVertBreak', 'ZoneTime', 'PitchUID']]

    X=preprocessing.MinMaxScaler().fit(X).transform(X)
    
    
    if len(tempdf)<=2:
        pass
    else:
        i=4
        while i<=6:
            gmm1=GMM(n_components=i, n_init=100).fit(X)
            bic1=gmm1.bic(X)
            gmm2=GMM(n_components=i-1, n_init=100).fit(X)
            bic2=gmm2.bic(X)
            gmm3=GMM(n_components=i+1, n_init=100).fit(X)
            bic3=gmm3.bic(X)
        
       
            if bic1<=bic2 and bic1<=bic3:
                num=i
                gmm=gmm1
                break
            else:
                i=i+1
                num=i
                gmm=gmm1
                if i>len(X):
                    break
        labels=gmm.predict(X)
        
        
        Y['Cluster']=labels
        Y['ClusterName']=Y['Cluster']
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        
        uniquecl=Y['Cluster'].unique().tolist()
        
        for k in uniquecl:
            pitchlist=Y.groupby('Cluster').get_group(k).TaggedPitchType.value_counts(1).index.tolist()
            
            pitchname=pitchlist[0]
    
                
            
            Y['ClusterName'].replace(k, pitchname, inplace=True)
            
            temp=Y[Y['Cluster']==k]
            
           
            ax.scatter(temp['RelSpeed'], temp['HorzBreak'], temp['InducedVertBreak'], c=coloring(k), label=uniquecl)
            ax.legend(uniquecl)
            
            ax.set_xlabel('구속')
            ax.set_ylabel('수평 무브먼트')
            ax.set_zlabel('수직 무브먼트')
            
            ax.set_xlim(90, 160)
            ax.set_ylim(-60, 60)
            ax.set_zlim(-60, 60)
            ax.grid('on')
            
        #plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\" + name + "_"+str(j)+"_by_Cluster.png")
        
        rot_animation = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 362, 2), interval=100)
        
        rot_animation.save("C:\\Users\\LIONS\\.spyder-py3\\9월 3주\\외인 구종분류2\\" + name + "_"+str(j)+"_by_Cluster.gif", dpi=80, writer='imagemagick')
       
    
            
        Y.to_csv('C:\\Users\\LIONS\\.spyder-py3\\9월 3주\\외인 구종분류2\\'+name+'.csv', index=False)
        
        
        uniqueclname=Y['ClusterName'].unique().tolist()
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        for k in uniqueclname:
    
            
            temp=Y[Y['ClusterName']==k]
            
            
            ax.scatter(temp['RelSpeed'], temp['HorzBreak'], temp['InducedVertBreak'], c=coloring2(k), label=uniqueclname)
            ax.legend(uniqueclname)
            
            ax.set_xlabel('구속')
            ax.set_ylabel('수평 무브먼트')
            ax.set_zlabel('수직 무브먼트')
            
            ax.set_xlim(90, 160)
            ax.set_ylim(-60, 60)
            ax.set_zlim(-60, 60)
            ax.grid('on')
            
        #plt.title("\n" + name + " 구종 분류\n", fontsize = 20)
        #plt.savefig("C:\\Users\\LIONS\\.spyder-py3\\8월 3주\\" + name + "_"+str(j)+"_by_Cluster_Name.png")
        
        rot_animation = animation.FuncAnimation(fig, rotate, frames=np.arange(0, 362, 2), interval=100)
        rot_animation.save("C:\\Users\\LIONS\\.spyder-py3\\9월 3주\\외인 구종분류2\\" + name + "_"+str(j)+"_by_Cluster_Name.gif", dpi=80, writer='imagemagick')
        
        Z=Y[['PitchUID', 'Cluster', 'ClusterName']]
        
        yimsi=pd.concat([Z, yimsi], ignore_index=True)
    
    

dfcopy=pd.merge(dfcopy, yimsi, how='outer', on=['PitchUID'])
    
    
#dfcopy.to_csv('C:\\Users\\LIONS\\.spyder-py3\\7월 2주\\Classified.csv', index=False, encoding='cp949')
    
