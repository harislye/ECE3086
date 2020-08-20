# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 11:12:46 2020

At folder
C:\1_Code\Teaching\ECE3086\class_codes\chapterX_object_det

@author: user
"""
#%% Do import the required library

import cv2
import numpy as np
import time

#%% Revision, display video frames from webcam

# Loading camera
cap = cv2.VideoCapture(0)

starting_time = time.time()
frame_id =0
while True:
    _, frame = cap.read()
    frame_id += 1
    height, width, channels = frame.shape
    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Display the resulting frame
    cv2.imshow('colour video from webcam',frame)
    cv2.imshow('grayscale video from webcam',gray)
    
    elapsed_time = time.time() - starting_time
    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    fps = frame_id / elapsed_time
    print("Display frame {:03} at {:05.3f} frames/sec".format(frame_id, fps))    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()






#%%