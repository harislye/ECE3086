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

#%% Downsample a video and display at 1 fps 
cap = cv2.VideoCapture(filename)

# Your code here




    

cap.release()
#cv2.destroyAllWindows()






















