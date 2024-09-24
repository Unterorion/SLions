# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 15:33:13 2021

@author: LIONS
"""

import moviepy.editor as mp
import os

filelist = os.listdir('C:\\Users\\LIONS\\Desktop\\1008 몽고메리 수정 2')

inputroute = r'C:\\Users\\LIONS\\Desktop\\1008 몽고메리 수정 2\\'
outputroute = r'C:\\Users\\LIONS\\Desktop\\'

concat = []

for i in range(len(filelist)):
    file = filelist[i]
    clip = mp.VideoFileClip(inputroute + file)
    concat.append(clip)

video = mp.concatenate_videoclips(concat)
video.write_videofile(outputroute + "1008 몽고메리 합본.avi", codec='libx264')