# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 19:38:26 2020

@author: user
"""

from mhl_object_detection_module import * # wrap detection code here
import time
import matplotlib.pyplot as plt  
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'qt5')


#%% Read and display image
 
filename = './images/dog.jpg'
img = cv2.imread(filename)
imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) 
cv2.imshow("Image Before Detection", img)
# plt.imshow(imgRGB), plt.title('image')
# plt.figure(1)
# plt.show()

#%%
print("Hello")
x= 5
















