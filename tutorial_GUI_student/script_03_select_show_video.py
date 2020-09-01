# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:50:11 2020

@author: user
"""
import cv2
from tkinter import Label
from tkinter import *
import os
os.chdir(r'C:\1_Code\Teaching\ECE3086\class_codes\tutorial_GUI_student')

ctr=0
#%% Call back function
def runDemo():
    global ctr
    print(" Demo running ...", ctr)
    ctr = ctr+1
    filename = filedialog.askopenfilename()
    print("Selected video file = {} ".format (filename) )
    status = showVideo(filename)


def showVideo(filename):
    i=0
    cap = cv2.VideoCapture(filename)
    while(cap.isOpened() ):
        ret, frame = cap.read()
        i = i + 1
        if ret == False :
            break
       
        cv2.imshow('frame',frame)
        print("Display frame {}".format(i) )
        
        if cv2.waitKey(40) & 0xFF == ord('q'):  # "Press q to clear video "
            break
        
    cap.release()
    return 1


#%%
window = Tk()
window.geometry("300x300")
window.title(" My Video Player ")

# label1 = Label(window, text="welcome", 
#                fg='blue', bg='yellow',
#                relief = "solid",
#                font=("arial",16,'bold')).pack()
label1 = Label(window, text=" My Video Player ", 
                fg='blue', bg='yellow',
                relief = "solid",
                font=("arial",16,'bold')).place(x=10,y=10)
# button1 = Button(window, text = "Demo",
#                 fg='blue', bg='yellow',
#                 relief = "solid",
#                 font=("arial",16,'bold'))
button1 = Button(window, text = "Get video file", relief = RAISED, command=runDemo)
button1.place(x=10,y=110)
window.mainloop()

































