# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 17:12:30 2020
https://realpython.com/playing-and-recording-sound-python/
@author: user
"""
import sounddevice as sd
import soundfile as sf
from scipy.io.wavfile import write
import matplotlib.pyplot as plt
import numpy as np
plt.close('all')

#%% Do audio recording
# Parameter
filename = 'output2.wav'
fs = 44100  # Sample rate
seconds = 3  # Duration of recording


myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write(filename, fs, myrecording)  # Save as WAV file

#%% Playback the recorded sound

filename = 'output2.wav'
# Extract data and sampling rate from file
data, fs = sf.read(filename, dtype='float32')  
sd.play(data, fs)
status = sd.wait()  # Wait until file is done playing

#%% Try play flac audio , fail on mp3 (you can try librosa for mp3)

# Extract data and sampling rate from file
# from https://helpguide.sony.net/high-res/sample1/v1/en/index.html
filemp3= r'.\audio\bee_96kHz24bit.flac'
data, fs = sf.read(filemp3, dtype='float32')  
sd.play(data, fs)
status = sd.wait()  # Wait until file is done playing



#%% Display the recorded sound waveform (plot signal in time domain)
plt.figure(1)
sig1 = myrecording[:,1] # pick channel 1 of stereo audio stream
plt.plot(sig1)

print(" Total samples for {} secs recorded sound = {} ".format(seconds,len(sig1)))

# Show time in secs for x axis
T = 1/fs # sampling period
tvec = T * np.arange(len(sig1))
plt.figure(2)
plt.plot(tvec,sig1)
stringt = "Recorded sound of {} secs".format(seconds)
plt.title(stringt)
plt.show()

#%% Plot only selected sound segment
t_start = 1.0
t_end = 3 # sec

n1 = int( np.floor(t_start/T) )
n2 = int( np.floor(t_end/T) )

sig1_sel = sig1[n1:n2+1] # include n2
numPt = len(sig1_sel)
tvec = T * np.arange(n1,n1+numPt)

plt.figure(3)
plt.plot(tvec,sig1_sel)
stringt = "Recorded sound of {} secs to {} secs".format(t_start, t_end)
plt.title(stringt)
plt.show()

# Play only selected segment
sd.play(sig1_sel, fs)
status = sd.wait()  # Wait until file is done playing

#%%

