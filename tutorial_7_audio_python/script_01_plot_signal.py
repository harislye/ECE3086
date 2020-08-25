# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 19:30:14 2020

@author: user
"""
import numpy as np
import matplotlib.pyplot as plt
plt.close('all')

#%% Create a sin wave to model continuous time signal
# Parameter : 
numCycles = 5     
fsig = 100 # Hz

period =  1/fsig
t_stop = numCycles * period  # sec , ending time
t = np.linspace(0, t_stop, 10000)
x_t = 325 * np.sin(2*np.pi*fsig*t)
print(" Number of cycles = {}".format(numCycles))
print(" CT Signal start time = {} secs, ending time = {} secs".format(0,t_stop))

fig = plt.figure(1)
plt.plot(t, x_t, label="sine wave");
plt.xlabel('t');
plt.ylabel('x(t)');
plt.title(r'Plot of CT signal $x(t)=325 \sin(2\pi 50 t)$');
plt.xlim([0, t_stop]);
plt.legend(loc='upper left', frameon=False)
plt.show()

#%% Do sampling on the signal
# parameter
t_end = t_stop  # Sample a signal from time 0 till t_stop sec
numPoints = 100 # NUmber of points to cover the signal from [0,t_end]

n = np.arange(numPoints) #  points on the plot
T = t_end/numPoints # spacing between points in time
xs = np.sin(2 * np.pi * fsig * n * T)


fig = plt.figure(2)
plt.xlabel('n');
plt.ylabel('x[n]');
plt.title(r'Plot of DT signal $x[n] = 325 \sin(2\pi 50 nT)$');
plt.stem(n, xs);


fig = plt.figure(3)
plt.xlabel('n');
plt.ylabel('x[n]');
plt.title(r'Plot of Sampled signal $x[n] = 325 \sin(2\pi 50 nT)$');
plt.plot(n, xs, 'r.');
plt.show()








