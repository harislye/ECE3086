# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 10:11:14 2020

@author: user
"""
from mhl_object_detection_module import * # wrap detection code here
import time

#%% Load Yolo
# weightfile = "yolov3-tiny.weights"
# cfgfile = "yolov3-tiny.cfg"
weightfile = "yolov3.weights"
cfgfile = "yolov3.cfg"

net = cv2.dnn.readNet( weightfile, cfgfile)

classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]

param = {}
param['classes'] = classes
#%%

# Loading camera
cap = cv2.VideoCapture(0)

starting_time = time.time()
frame_id = 0
while True:
    _, frame = cap.read()
    frame_id += 1
    height, width, channels = frame.shape
    param['height'] = height
    param['width'] = width
    (class_ids, boxes, confidences) = run_detection_yolov3(frame, net, output_layers, param )
    displayDetectionResult(frame, boxes, class_ids, confidences, classes)
    elapsed_time = time.time() - starting_time
    
    fps = frame_id / elapsed_time
    print("Frame {} detection rate at {:03.2f} frames/sec".format(frame_id, fps) )
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    