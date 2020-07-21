# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:54:45 2020
Question 5 Write a short Python program to read the audio file myAudio.wav .
 Play the sound with your program. 
 Find the sampling rate.
 Modify the program to read sound from the microphone. # not yet



Pyaudio install works for win10
> pip install pipwin
> pipwin install pyaudio

@author: user
"""

#%% Import

import numpy as np
import matplotlib.pyplot as plt
import pyaudio
import wave

#%% Read audio file
filename = './media_files/myAudio.wav'  # ok
# Open the sound file 
wf = wave.open(filename, 'rb')

# Create an interface to PortAudio
p = pyaudio.PyAudio()

#%% Check audio parameter
print(wf.getsampwidth()) 
print(" Sampling rate = " , wf.getframerate() )  # 44100 samples/sec
print(" Num channel = ", wf.getnchannels()) # 2 -> stereo

#%% Play one chunk of sound samples

# 1 chunk = 1024 samples
chunk = 1024

# Open a .Stream object to write the WAV file to
# 'output = True' indicates that the sound will be played rather than recorded
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

#%% Specify how long audio to play
fsamp = wf.getframerate()
duration = 4 # sec
numChunks = np.ceil( (fsamp /chunk) * duration )
print(" Total chunks = " , numChunks)

#%%
 
# Read data in chunk 
total = 0
while total < numChunks :
    data = wf.readframes(chunk)
    stream.write(data) # data send to the stream will be played
    total +=1


# Close and terminate the stream
wf.close()
stream.stop_stream()
stream.close()
p.terminate() # end pyAudio object




























