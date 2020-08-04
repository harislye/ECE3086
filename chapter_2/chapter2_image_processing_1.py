# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 16:55:41 2020

For lecture on image processing


Take some time to display images
@author: haris
"""
#%% Display gray scale image

import cv2  
import numpy as np  
from matplotlib import pyplot as plt  
img = cv2.imread(r'C:\1_Code\Teaching\ECE3086\images\cameraman.tif',cv2.IMREAD_GRAYSCALE)  
print('Original Dimensions : ',img.shape)
plt.imshow(img, cmap='gray'), plt.title('Original gray image')
plt.figure(1)

plt.show()


#%% Apply mean filter
kernel = np.ones((10,10),np.float32)/100  
dst = cv2.filter2D(img,-1,kernel)  

plt.figure(2)
plt.subplot(121),plt.imshow(img, cmap='gray'),plt.title('Original')  
plt.xticks([]), plt.yticks([])  
plt.subplot(122),plt.imshow(dst, cmap='gray'),plt.title('Filter2D')  
plt.xticks([]), plt.yticks([])   
plt.show()  

#%% Sharpen the image

def sharpen(image):
    kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
    return cv2.filter2D(image, -1, kernel)

im2 = sharpen(img) 
plt.figure(3)
plt.subplot(121),plt.imshow(img, cmap='gray'),plt.title('Original')  
plt.subplot(122),plt.imshow(im2, cmap='gray'),plt.title('Sharpened image')  
plt.show()

#%% Edge detection

# Calcution of Sobelx 
sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5) 
      
# Calculation of Sobely 
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5) 

sobelxy = np.sqrt(sobelx**2 + sobely**2)

plt.figure(4)
plt.subplot(121),plt.imshow(sobelx, cmap='gray'),plt.title('Sobelx')  
plt.subplot(122),plt.imshow(sobely, cmap='gray'),plt.title('Sobely')  
plt.show()

plt.figure(5)
plt.imshow(sobelxy, cmap='gray'),plt.title('Sobelxy')  

plt.show()

#%% Detect edge map by thresholding

nr,nc = sobelxy.shape
edgeMap = np.zeros_like(sobelxy)
mask = sobelxy>6000 # np array boolean 256x256
edgeMap[mask]=1
numEdgePixels = sum(edgeMap.flatten()) # 

# show edge map
plt.figure(6)
plt.imshow(edgeMap, cmap='gray')














