# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:36:12 2020
C:\1_Code\Teaching\ECE3086\class_codes\tutorial_1
tut1_Q3_sfinal.py
https://www.rock-paper-scissors-game.com/
@author: user
"""
import random

def getWinner(human , ai):
    #
    combi = (human,ai)
    print(combi)
    if combi in [(1,3), (2,1), (3,2)] :
        print(" Human wins ")
        winner = 1
    elif combi in [(1,1), (2,2), (3,3)]:
        print(" Human and AI Draws ")
        winner = 0
    else:
        print(" AI wins ")
        winner = 2
        
    return winner
    # end func
        

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
    ai_choice = inputList[n-1]
    print(" Ai chooses ", ai_choice)
    winner = getWinner(human = choice_num , ai = n)
 