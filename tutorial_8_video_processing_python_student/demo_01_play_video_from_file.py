# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 10:14:22 2020

@author: haris
"""

# Read a video file

import numpy as np
import cv2
import os

path = r'C:\1_Code\Teaching\ECE3086\class_codes\tutorial_8_video_proccessing_python'
os.chdir(path)
#%%
#filename = 'myVideo.mp4'
filename = 'thor.mp4'
#filename=0 # use webcam

delay = 20 # Display a frame for delay miliseconds 

cap = cv2.VideoCapture(filename)
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

