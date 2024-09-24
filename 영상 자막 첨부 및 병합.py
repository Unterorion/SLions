# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 13:20:29 2021

@author: LIONS
"""

import pandas as pd
import moviepy.editor as mp
import os
import numpy as np

df = pd.read_csv('C:\\Users\\LIONS\\Desktop\\트랙맨 자막 영상\\20211027-Gocheok-1.csv', index_col=None, encoding='cp949')
df = df[df['PitcherId'] == 61411]

date = '1027'
name = '심창민'
lan = 'Kor'

def translate(eng):
    if eng=='Fastball':
        return '직구'
    elif eng=='Slider':
        return '슬라이더'
    elif eng=='Curveball':
        return '커브'
    elif eng=='Changeup' or eng=='ChangeUp':
        return '체인지업'
    elif eng=='Sinker':
        return '투심'
    elif eng=='Splitter':
        return '스플리터'
    elif eng=='Cutter':
        return '커터'

df['KorPitchType'] = df['TaggedPitchType'].apply(translate)

inputroute = r'C:\\Users\\LIONS\\Desktop\\트랙맨 자막 영상\\%s %s\\' % (date, name)
outputroute = r'C:\\Users\\LIONS\\Desktop\\트랙맨 자막 영상\\'
filelist = os.listdir(inputroute[:-2])

concat = []

if lan == 'Kor':
    for i in range(len(df.index)):
        file = filelist[i]
        
        ptype = df['KorPitchType'].iloc[i]
        rs = df['RelSpeed'].iloc[i]
        sr = df['SpinRate'].iloc[i]
        hmov = df['HorzBreak'].iloc[i]
        vmov = df['InducedVertBreak'].iloc[i]
        rels = df['RelSide'].iloc[i]
        relh = df['RelHeight'].iloc[i]
        ext = df['Extension'].iloc[i]
        
        clip = mp.VideoFileClip(inputroute + file)
        
        txtclip1 = mp.TextClip("%s, %dkm/h\n회전수 %d\n수평 무브먼트 %dcm\n수직 무브먼트 %dcm"%(ptype,rs,sr,hmov,vmov), fontsize=45, color='black', bg_color='white', font='Malgun-Gothic')
        txtclip1 = txtclip1.set_duration(clip.duration)
        
        txtclip2 = mp.TextClip("릴리즈 사이드 %.2fm\n릴리즈 높이 %.2fm\n익스텐션 %.2fm"%(rels,relh,ext), fontsize=45, color='black', bg_color='white', font='Malgun-Gothic')
        txtclip2 = txtclip2.set_pos(('right', 'top'))
        txtclip2 = txtclip2.set_duration(clip.duration)
        
        video = mp.CompositeVideoClip([clip, txtclip1, txtclip2])
        
        concat.append(video)
elif lan == 'Eng':
    for i in range(len(df.index)):
        file = filelist[i]
        
        ptype = df['TaggedPitchType'].iloc[i]
        rs = df['RelSpeed'].iloc[i]/1.6
        sr = df['SpinRate'].iloc[i]
        hmov = df['HorzBreak'].iloc[i]/2.54
        vmov = df['InducedVertBreak'].iloc[i]/2.54
        
        rels = np.abs(df['RelSide'].iloc[i])*100//2.54
        relh = df['RelHeight'].iloc[i]*100//2.54
        ext = df['Extension'].iloc[i]*100//2.54
        
        rels1 = rels//12
        rels2 = rels%12
        relh1 = relh//12
        relh2 = relh%12
        ext1 = ext//12
        ext2 = ext%12
        
        strrels = "%dft %din" % (rels1, rels2)
        strrelh = "%dft %din" % (relh1, relh2)
        strext = "%dft %din" % (ext1, ext2)
        
        clip = mp.VideoFileClip(inputroute + file)
        
        txtclip1 = mp.TextClip("%s, %dmph\nSpin Rate %d\nH-mov %din\nV-mov %din"%(ptype,rs,sr,hmov,vmov), fontsize=45, color='black', bg_color='white')
        txtclip1 = txtclip1.set_duration(clip.duration)
        
        txtclip2 = mp.TextClip("Release S %s\nRelease H %s\nExtension %s"%(strrels,strrelh,strext), fontsize=45, color='black', bg_color='white')
        txtclip2 = txtclip2.set_pos(('right', 'top'))
        txtclip2 = txtclip2.set_duration(clip.duration)
        
        video = mp.CompositeVideoClip([clip, txtclip1, txtclip2])
        
        concat.append(video)

final = mp.concatenate_videoclips(concat)
final.write_videofile(outputroute + "%s %s 합본.mp4"%(date,name), codec='lib264x', fps=24.00)