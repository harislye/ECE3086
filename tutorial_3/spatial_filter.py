# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:56:28 2020

@author: user
"""
import numpy as np
def meanFilter(I,mask):
        
    def padZero(Mat): # ok tested
        (r,c) = Mat.shape
        Ipad = np.zeros((r+2,c+2))
        Ipad[1:r+1, 1:c+1] = Mat
        return Ipad
        # end func
    
    I_padded = padZero(I)
    wid = mask.shape[0] # width of mask
    I_padded = padZero(I)
    Inew = np.zeros(I.shape)

    # Apply mean filtering over I_padded
    # Move around non zeros pixel
    (nr,nc) = I_padded.shape
    for i in range(1,nr-1):
        for j in range(1,nc-1):
            # print((i,j))
            # target = (i,j)
            rs = i-1 ; cs = j-1
            subI = I_padded[rs:rs+wid , cs:cs+wid ]
            product = subI *  mask
            Inew[i-1,j-1] = np.sum(product)
    # end for loop
    return Inew
    
# Test case 1 - pass on 29/7/2020
# I2 = np.array([   [22, 77, 48 ],
#                  [150, 77, 158],
#                  [0, 77, 219],
#                  [22, 77, 48],
#                  [150, 77, 158],
#                  [0, 77, 219]
#                 ])

# mask = np.ones( (3,3) ) *1/9 # mask
# I_filtered = meanFilter(I2, mask)

