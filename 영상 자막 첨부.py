# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 13:20:29 2021

@author: LIONS
"""

import pandas as pd
import moviepy.editor as mp
import os

df = pd.read_csv('C:\\Users\\LIONS\\Desktop\\20211008-NCDinosMajors-1.csv', index_col=None, encoding='cp949')
df = df[df['PitcherId'] == 543557]

filelist = os.listdir('C:\\Users\\LIONS\\Desktop\\1008 몽고메리')

inputroute = r'C:\\Users\\LIONS\\Desktop\\1008 몽고메리\\'
outputroute = r'C:\\Users\\LIONS\\Desktop\\1008 몽고메리 수정 2\\'

for i in range(len(df.index)):
    file = filelist[i]
    
    ptype = df['TaggedPitchType'].iloc[i]
    rs = df['RelSpeed'].iloc[i]/1.6
    sr = df['SpinRate'].iloc[i]
    hmov = df['HorzBreak'].iloc[i]/2.54
    vmov = df['InducedVertBreak'].iloc[i]/2.54
    '''rels = df['RelSide'].iloc[i]
    relh = df['RelHeight'].iloc[i]
    ext = df['Extension'].iloc[i]'''
    
    clip = mp.VideoFileClip(inputroute + file)
    
    txtclip = mp.TextClip("%s, %dmph\nSpin Rate %drpm\nH-mov %din\nV-mov %din"%(ptype,rs,sr,hmov,vmov), fontsize=45, color='white')
    #txtclip = mp.TextClip("%s, %dmph\nSpin Rate %drpm\nH-mov %din\nV-mov %din\nRelease S %d\nRelease H %d\nExtension %d"%(ptype,rs,sr,hmov,vmov,rels,relh,ext), fontsize=45, color='white')
    txtclip = txtclip.set_duration(clip.duration)
    video = mp.CompositeVideoClip([clip, txtclip])
    
    video.write_videofile(outputroute + file[:-4] + ".avi", codec='libx264')