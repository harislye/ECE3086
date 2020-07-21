# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:41:44 2020

Question 6
Write a short Python program to open the video file myVideo.mp4 . 
Use the program to play the video. 
Convert the video to grayscale and save it as myVideo_gray.mp4. 
Repeat the same problem using video from your webcam.
 Use the opencv cv2 module for video processing.

---------
Convert to grayscale and save it

@author: user
"""

#%% Import

import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

#%% Read Video File

filename = './media_files/myVideo.mp4'  # ok
filenameOut = './media_files/myVideo_gray.mp4'

# Create a video reader 
cap = cv2.VideoCapture(filename) # video object

# get video parameter
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fourcc = cv2.VideoWriter_fourcc(*'MP4V') # use mpeg4 encoder
fps = round( cap.get(cv2.CAP_PROP_FPS) ) # frame rate

out = cv2.VideoWriter(filenameOut, fourcc, fps, (frame_width,frame_height) , isColor=False )

# check for error in opening the video
if (cap.isOpened()== False): 
  print("Error opening video stream or file")
  
#%% Write to another video
frameIdx=0
while (cap.isOpened()):
    

print(" Total frames = {}".format(frameIdx))  

#%%
cap.release() 
out.release()
   
# Closes all the frames 
cv2.destroyAllWindows()   
























