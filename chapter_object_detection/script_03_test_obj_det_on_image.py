# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 10:58:41 2020

@author: user
"""

from mhl_object_detection_module import * # wrap detection code here
import time
import os
import matplotlib.pyplot as plt  
from IPython import get_ipython
# get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('matplotlib', 'qt5')

#%% Load Yolo
# weightfile = "yolov3-tiny.weights"
# cfgfile = "yolov3-tiny.cfg"
weightfile = "yolov3.weights"
cfgfile = "yolov3.cfg"

net = cv2.dnn.readNet( weightfile, cfgfile)
param = {}
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
param['classes'] = classes


#%% Read and display image
 
#filename = 'dog.jpg'
#filename = 'eagle.jpg'
filename = 'person.jpg'

path = 'images'
filename1 = os.path.join(os.getcwd(),path,filename)
img = cv2.imread(filename1)
imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) 
cv2.imshow("Image Before Detection", img)
# plt.imshow(imgRGB), plt.title('image')
# plt.figure(1)
# plt.show()

#%% run detection

height, width, channels = img.shape
param['height'] = height
param['width'] = width
(class_ids, boxes, confidences) = run_detection_yolov3(img, net, output_layers, param )

imOut = displayDetectionResult(img, boxes, class_ids, confidences, classes)

#%%
SAVE_FILE = True
if SAVE_FILE:
    filename = 'out_'+filename
    filename1 = os.path.join(os.getcwd(),path,filename)
    cv2.imwrite(filename1, imOut)    


#%%


































