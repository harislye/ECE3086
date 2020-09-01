# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 17:54:35 2020

@author: haris
"""

import numpy as np
import cv2 

class VideoData :
    pass
        

def getVideoInformation(filename):
    v = VideoData()
    video = cv2.VideoCapture(filename)
    if video.isOpened():
        v.fps = np.round( video.get(cv2.CAP_PROP_FPS) )
        v.total = int(video. get(cv2.CAP_PROP_FRAME_COUNT))
        v.width  = video.get(cv2.CAP_PROP_FRAME_WIDTH)  # float
        v.height = video.get(cv2.CAP_PROP_FRAME_HEIGHT) # float
        v.duration = np.floor(v.total/v.fps)
    
        
    print(" Video information for {} ".format(filename))
    print(" Total frames = {} ".format(v.total))
    print(" Frame rate = {} frames/sec ".format(v.fps))
    print(" Video duration = {} secs ".format(v.duration))
    return v

def clear_all():
    from IPython import get_ipython
    get_ipython().magic('reset -sf')