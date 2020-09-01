# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 12:04:19 2020

@author: user
"""
from videoModule import clear_all
clear_all()

from videoModule import *
import numpy as np
import cv2 
import os
import time


#%% Get video info
path = r'C:\1_Code\Teaching\ECE3086\class_codes\tutorial_8_video_proccessing_python'
os.chdir(path)
filename = 'myVideo.mp4'  # 29 sec video
#filename = 'thor.mp4'  
videoInfo =  getVideoInformation(filename)



#%% Fast forward to frame x and play
cap = cv2.VideoCapture(filename)
delay = np.round(1/videoInfo.fps,3)* 1000 # in msec

#%%
i=0
speed = input('Input the frame speed 1,2, 3 or 4x option={1,2,3,4} ->> ')
delay = delay / int(speed)
delay = int(delay)

i=0
while(cap.isOpened() ):
    ret, frame = cap.read()
    if ret == False :
        break
    if cv2.waitKey(delay) & 0xFF == ord('q'):  # "Press q to clear video "
        break
    cv2.imshow('frame',frame)
    i = i + 1
    print("Display frame {}".format(i) )

cap.release()
#cv2.destroyAllWindows()
