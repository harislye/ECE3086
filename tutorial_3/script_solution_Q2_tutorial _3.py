# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 17:13:42 2020

Solution to Q2 Tutorial 3


@author: user
"""

#%%
import numpy as np
Inew = np.zeros((6,3))
subI = np.array([   [22, 77, 48 ],
                    [150, 77, 158],
                    [0, 77, 219] 
                ])

Inew = np.zeros((6,3))
mask = np.ones( (3,3) ) *1/9
product = subI *  mask
Inew[1,1] = np.sum(product) # 92

#%%
subI = np.array([   [150, 77, 158 ],
                    [0, 77, 219],
                    [22, 77, 48] 
                ])

mask = np.ones( (3,3) ) *1/9
product = subI *  mask
Inew[2,1] = np.sum(product)  # 92

#%% version 2 - Transform image I  to Inew use 3x3 mean filtering
mask = np.ones( (3,3) ) *1/9
I = np.array([   [22, 77, 48 ],
                 [150, 77, 158],
                 [0, 77, 219],
                 [22, 77, 48],
                 [150, 77, 158],
                 [0, 77, 219]
                ])

# new image initiliazed , same size as original image
Inew = np.zeros((6,3))

target = (1,1) # target pixel location
(i,j) = target
subI = I[i-1:i+2, j-1:j+2 ] # extract sub image to process
product = subI *  mask
Inew[target] = np.sum(product)

target = (2,1)
(i,j) = target
subI = I[i-1:i+2, j-1:j+2 ]
product = subI *  mask
Inew[target] = np.sum(product)

#%% Transform the whole image I to Inew
# Not required for test
# Demo code shows how to transform the whole image by mean filtering 

def padZero(Mat): # ok tested
    (r,c) = Mat.shape
    Ipad = np.zeros((r+2,c+2))
    Ipad[1:r+1, 1:c+1] = Mat
    return Ipad

I = np.array([   [22, 77, 48 ],
                 [150, 77, 158],
                 [0, 77, 219],
                 [22, 77, 48],
                 [150, 77, 158],
                 [0, 77, 219]
                ])

wid = 3 # width of mask
mask = np.ones( (3,3) ) *1/9
I_padded = padZero(I)
Inew = np.zeros(I.shape)

# Apply mean filtering over I_padded
# MOve around non zeros pixel
(nr,nc) = I_padded.shape
for i in range(1,nr-1):
    for j in range(1,nc-1):
        # print((i,j))
        # target = (i,j)
        rs = i-1 ; cs = j-1
        subI = I_padded[rs:rs+wid , cs:cs+wid ]
        product = subI *  mask
        Inew[i-1,j-1] = np.sum(product)

print(Inew)





























































































