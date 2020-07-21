# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 15:43:37 2020

@author: haris
"""

# Use PyAudio to play sound
import numpy as np
import matplotlib.pyplot as plt
import pyaudio
import wave

def getAudioParameter(filename):
    
    # set param
    chunk = 1024  
    duration = 2 # 2 secs play sound for a fixed duration

    # Open the sound file 
    wf = wave.open(filename, 'rb')

    # Create an interface to PortAudio
    p = pyaudio.PyAudio()

    # Open a .Stream object to write the WAV file to
    # 'output = True' indicates that the sound will be played rather than recorded
    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True)
    
    # Read data in chunks
    data = wf.readframes(chunk)
    rate = wf.getframerate() /chunk  # frame rate , 1 frame 1024 samples
        
    ctr=1
    while len(data) >0:
        #stream.write(data) # data send to the stream will be played
        data = wf.readframes(chunk)
        ctr +=1
    
    timeTaken = round(ctr/rate)
    d=dict()
    d['duration'] = timeTaken 
    d['samplingRate'] = wf.getframerate()
    
    # Close and terminate the stream
    stream.stop_stream()
    stream.close()
    p.terminate()
    wf.close()
    
    return d


def playAudio(filename, duration):
    
    # set param
    chunk = 1024  
   
    # Open the sound file 
    wf = wave.open(filename, 'rb')

    # Create an interface to PortAudio
    p = pyaudio.PyAudio()

    # Open a .Stream object to write the WAV file to
    # 'output = True' indicates that the sound will be played rather than recorded
    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True)
    
    # Read data in chunks
    data = wf.readframes(chunk)
    # note wf.getframerate()give frame rate
    framerate = wf.getframerate() /chunk  # frame rate , 1 frame 1024 samples
    totalChunk = framerate * duration 
    
    ctr=1
    while len(data) >0:
        # play sound
        stream.write(data) # data send to the stream will be played
        data = wf.readframes(chunk)
        ctr +=1
        if ctr > totalChunk:
            break
       
   
    # Close and terminate the stream
    wf.close()
    stream.stop_stream()
    stream.close()
    p.terminate()
    
    



