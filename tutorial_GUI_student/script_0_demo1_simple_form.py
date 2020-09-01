# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 19:02:08 2020

@author: user
"""
import tkinter as tk
import sys

#%% function

def show_entry_fields():
    print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))
    if CheckVar1.get():
        print("Machine learning selected")
    if CheckVar2.get():
        print("Deep learning selected")

def exit_program():
    sys.exit()

#%% graphic part

master = tk.Tk()

# show 2 label
tk.Label(master, text="First Name").grid(row=0)
tk.Label(master, text="Last Name").grid(row=1)
e1 = tk.Entry(master)
e2 = tk.Entry(master)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

# show button
tk.Button(master, 
          text='Quit', 
          command=master.destroy).grid(row=3,column=0, 
                                    sticky=tk.W, pady=4)
tk.Button(master, 
          text='Show', command=show_entry_fields).grid(row=3, column=1, 
                                                       sticky=tk.W, pady=4)

                                                       
CheckVar1 = tk.IntVar()
CheckVar2 = tk.IntVar()
check1 = tk.Checkbutton(master, text = "Machine Learning",
                        variable = CheckVar1,onvalue = 1, offvalue=0).grid(row=5,sticky=tk.W)
check2 = tk.Checkbutton(master, text = "Deep Learning",
                        variable = CheckVar2, onvalue = 1, offvalue =0).grid(row=6,sticky=tk.W)

print(CheckVar1.get() )                                               
                                                       
master.mainloop()