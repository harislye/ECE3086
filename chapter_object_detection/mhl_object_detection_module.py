# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 15:44:52 2020
Ref https://pysource.com/2019/07/08/yolo-real-time-detection-on-cpu/
@author: user
"""
import cv2
import numpy as np


def run_detection_yolov3(frame, net, output_layers, param ):
# return frame # with bounding box predicted

    #Parameter used
    confidence_threshold = 0.5
    nms_overlap_threhold = 0.4


    
    height = param['height'] 
    width = param['width']
    
    classes = param['classes'] 
        
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    
    # Get prediction
    outs = net.forward(output_layers)
    
        # Showing informations on the screen
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > confidence_threshold:
                # Object detected
                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)
    
                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
    
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
    # end for loop
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, nms_overlap_threhold)
    
    # do filtering
    class_ids_f=[]; boxes_f=[];confidences_f=[]
    for  i in indexes:
        i =int(i)
        class_ids_f.append(class_ids[i])
        boxes_f.append(boxes[i])
        confidences_f.append(confidences[i])
        
    return (class_ids_f, boxes_f, confidences_f)
        
def displayDetectionResult(image, boxes, class_ids, confidences, classes):
    colors = np.random.uniform(0, 255, size=(len(classes), 3))
    font = cv2.FONT_HERSHEY_PLAIN
    numObjectsPredicted = len(boxes)
    for i in range(numObjectsPredicted):
        x, y, w, h = boxes[i]
        label = str(classes[class_ids[i]])
        confidence = round(confidences[i],3)
        color = colors[class_ids[i]]
        cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
        cv2.rectangle(image, (x, y), (x + w, y + 30), color, -1)
        text = str(i) + ": " + label + " " + str(round(confidence, 3))
        cv2.putText(image, text , (x, y + 30), font, 2, (55,55,55), 3)
        print("Predict {}/{} ,class:{} confidence ={}".format(i+1,
                                                                numObjectsPredicted,
                                                                label,confidence))
        
    cv2.imshow("Detection Result", image)
    return image
    

   
    # end func        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        