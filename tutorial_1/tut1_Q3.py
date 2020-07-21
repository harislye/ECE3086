# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:36:12 2020

@author: user
"""
import random


rockstr = "Rock"
paperstr = "Paper"
scissor = " Scissor"

#%%

inputList = ["Rock", "Paper", "Scissor"]

repeat = True

while repeat == True :
    choice = input(""" Human Input your choice in number 
                   \n 1 (Rock)
                   \n 2 (Paper) or 
                   \n 3 (Scissor) 
                   ->> """)
    
    choice_num = int(choice)
    print(int(choice_num))
    if choice_num not in range(1,4):
        print(" Invalid choice")
        repeat = True
    else:
        repeat = False
        print("Correct choice")
        print(" You have chosen ", inputList[choice_num-1])
        
 # Get input from computer AI
  
n = random.randint(1,3) # num from 1 tll 3
ai_choice = inputList(n)

# winner = getWinner(human = choice_num , ai = n)
     
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
