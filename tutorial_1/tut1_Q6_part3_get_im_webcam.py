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
# Test opencv code to capture video from handphone configured as webcamera >>ok
# Possible to use DroidCam app to use your handphone as webcam

import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while(True):
    ret, frame = cap.read()

    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
















