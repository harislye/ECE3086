# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 15:50:11 2020

@author: user
"""
import cv2
from tkinter import Label
from tkinter import *

ctr=0
#%% Call back function
def runDemo():
    global ctr
    print(" Demo running ...", ctr)
    ctr = ctr+1
    filename = filedialog.askopenfilename()
    print("Selected file = {} ".format (filename) )
    im = cv2.imread(filename)
    cv2.imshow("Image", im)

#%%
window = Tk()
window.geometry("300x300")
window.title(" My window ")

# label1 = Label(window, text="welcome", 
#                fg='blue', bg='yellow',
#                relief = "solid",
#                font=("arial",16,'bold')).pack()
label1 = Label(window, text="welcome", 
                fg='blue', bg='yellow',
                relief = "solid",
                font=("arial",16,'bold')).place(x=100,y=10)
# button1 = Button(window, text = "Demo",
#                 fg='blue', bg='yellow',
#                 relief = "solid",
#                 font=("arial",16,'bold'))
button1 = Button(window, text = "Get image file", relief = RAISED, command=runDemo)
button1.place(x=10,y=110)
window.mainloop()

































