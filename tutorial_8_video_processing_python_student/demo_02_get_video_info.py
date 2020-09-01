# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 16:07:23 2020
https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_gui/py_video_display/py_video_display.html
@author: haris
"""
from videoModule import clear_all
clear_all()

import numpy as np
import cv2 
import os
import time
from videoModule import *
import os


   
#%%
path = r'C:\1_Code\Teaching\ECE3086\class_codes\tutorial_8_video_proccessing_python'
os.chdir(path)
filename = 'thor.mp4'

video = cv2.VideoCapture(filename)
if video.isOpened():
    fps = np.round( video.get(cv2.CAP_PROP_FPS) )
    total = int(video. get(cv2.CAP_PROP_FRAME_COUNT))
    width  = video.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
    height = video.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
    video.set(cv2.CAP_PROP_POS_AVI_RATIO,0) 
    duration = np.floor(total/fps) # in sec

delay = int( np.round( (1/fps)*1000 ) ) # in sec
videoInfo =  getVideoInformation(filename)

#%% Check to see if the info is correct

start = time.time()
for i in range(total):
    ret,frame = video.read()
    cv2.imshow(" Video frame", frame)
    if cv2.waitKey(delay) & 0xFF == ord('q'):
        break
    
endt = time.time()
timeTaken  = endt - start
print(" Total frames = ", int(i))

    
video.release()
cv2.destroyAllWindows()
    

