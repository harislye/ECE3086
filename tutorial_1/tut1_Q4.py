# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:01:26 2020

Question
Write a short Python program to open the jpeg image myImage.jpg 
Display the image with your program. 
Convert the image to gray scale and save it as myImage_gray.jpg . Use the opencv cv2 module for image processing. Other modules can be used too.


@author: user
"""

#%%

import cv2
import matplotlib.pyplot as plt
import os

#%% Display image with matplotlib

#path = 'C:\\1_Code\\Teaching\\ECE3086\\class_codes\\tutorial_1'
filename = 'myImage.jpg'
filename = os.path.join('media_files',filename)
img = cv2.imread(filename)
print(img.shape)

img2=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(img2)
plt.show()
 
#%% Convert to grayscale

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(img_gray.shape)
plt.figure()
plt.imshow(img_gray,  cmap='gray') , plt.title(" Gray scale image converted from color image")
plt.show()