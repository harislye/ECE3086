# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 18:44:19 2020

@author: user
"""
import numpy as np
from numpy import pi
from numpy import cos
from numpy import zeros
from numpy import r_
from scipy import signal

import matplotlib.pylab as pylab
from scipy.fftpack import dct, idct
import matplotlib.pyplot as plt
plt.close('all')

#%% Use DCT transform from the scipy library

np.set_printoptions(formatter={'float': '{: 0.3f}'.format})

# numpy array
f = np.array([1,1,1,1,2,2,2,2], dtype='float32')
print("f = ",f)
 
# apply dct function on array
F = dct(f, norm = 'ortho')
print("Fu = ",F) # 

f_recon = idct(F, norm = 'ortho') 
print("f_recon = ",f_recon)
 
status = np.allclose(f,f_recon) 
print(" f equal f_recon ? ->", status)

#%% Try find the coefficient for F[0], u=0  frequency 0
u=0

cosv = np.zeros(8)
F = np.zeros(8)

for i in range(8):
    if u==0: 
        Cu = 1/np.sqrt(2)
    else: Cu=1
    cosv[i] = (Cu/2) *cos( (2*i+1)*u*pi/16)

# F[0] represent similarity between the signal in vec f with ref signal cosv(with u=0)
F[u] =  np.dot(f,cosv)    # F[0]=4.24

#%% Do for u = 0,1,2 ...7
for u in range(8):
    # compute ref signal for frequency u
    for i in range(8):
        i = int(i)
        if u==0: 
            Cu = 1/np.sqrt(2)
        else: Cu=1
        cosv[i] = (Cu/2) *cos( (2*i+1)*u*pi/16)
    
    F[u] = np.dot(f,cosv)  
    
#%% Exercise try reconstruct back the signal from the DCT coefficients

#%% Plot the reference signal
# matrix to store all ref signal
cosvv = np.zeros((8,8))
for u in range(8):
    # compute ref signal for frequency u
    for i in range(8):
        i = int(i)
        if u==0: 
            Cu = 1/np.sqrt(2)
        else: Cu=1
        cosvv[u,i] = (Cu/2) *cos( (2*i+1)*u*pi/16)

#%% Bar chart plot
import matplotlib.pyplot as plt
plt.close('all')
pylab.rcParams['figure.figsize'] = (3, 2)
index= np.arange(8)

for uu in range(8):
    plt.figure()
    string = " Reference cos signal with u = {}".format(uu)
    val = list(cosvv[uu,:])
    plt.bar(index,val)
    plt.xticks(index)
    plt.title(string)
    
plt.figure()
string = " test signal  "
val = list(f)
plt.bar(index,val)
plt.xticks(index)
plt.title(string)



#%%


























 
 