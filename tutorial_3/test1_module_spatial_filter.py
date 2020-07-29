# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 09:54:23 2020

@author: user
"""
from spatial_filter import *  # import all

I = np.array([   [22, 77, 48 ],
                 [150, 77, 158],
                 [0, 77, 219],
                 [22, 77, 48],
                 [150, 77, 158],
                 [0, 77, 219]
                ])

mask = np.ones( (3,3) ) *1/9 # mask
I_filtered = meanFilter(I, mask)
