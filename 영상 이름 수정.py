# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:48:15 2021

@author: LIONS
"""

import os

inputroute = r'C:\\Users\\LIONS\\Desktop\\트랙맨 자막 영상\\1016 이재희\\'
filelist = os.listdir(inputroute[:-2])

for name in filelist:
    if name[1] == '_':
        old = os.path.join(inputroute[:-2], name)
        newname = '00' + name
        newname = os.path.join(inputroute[:-2], newname)
        os.rename(old, newname)
    elif name[2] == '_':
        old = os.path.join(inputroute[:-2], name)
        newname = '0' + name
        newname = os.path.join(inputroute[:-2], newname)
        os.rename(old, newname)