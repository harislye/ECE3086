# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 16:41:44 2020

Question 6
Write a short Python program to open the video file myVideo.mp4 . 
Use the program to play the video. 
Convert the video to grayscale and save it as myVideo_gray.mp4. 
Repeat the same problem using video from your webcam.
 Use the opencv cv2 module for video processing.

@author: user
"""

#%% Import

import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

#%% Read Video File

filename = './media_files/myVideo.mp4'  # ok
# Create a video reader 
cap = cv2.VideoCapture(filename) # video object

# check for error in opening the video
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

#%% Count how many frames

frameIdx=0
while (cap.isOpened()):
    ret,frame = cap.read()

    if (ret == True):
      frameIdx += 1
      cv2.imshow(' Video Frame', frame)

    if (ret == False):
        break
    
     # Press Q on keyboard to  exit 
    if cv2.waitKey(25) & 0xFF == ord('q'): 
      break

print(" Total frames = {}".format(frameIdx ))
totalFrames = frameIdx

#%% Display one frame - todo



#%%
cap.release() 
# Closes all the frames 
cv2.destroyAllWindows()


























