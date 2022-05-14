# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 15:32:21 2018

@author: yzj
"""

file=open("D:/test.fq","r").readlines()
left=open("D:/left.fq","w")
right=open("D:/right.fq","w")
for i in range(0,len(file),4):
    if (file[i].startswith("@")) & (file[i].endswith("/1\n")):
        left.write(file[i]+file[i+1]+file[i+2]+file[i+3])
    if (file[i].startswith("@")) & (file[i].endswith("/2\n")):
        right.write(file[i]+file[i+1]+file[i+2]+file[i+3])

left.close()
right.close()

        