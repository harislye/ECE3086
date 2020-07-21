# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:44:06 2020

@author: user
"""

import math
import os
import random
import re
import sys

# Wait for you to type something
if __name__ == '__main__':
    n = int(input().strip())
    
    if n in range(1,101):
        # is odd ?
        if (n%2)!=0 :
            print("Weird")
            
        elif n in range(2,6): # till 5
            print("Not Weird")
        elif n in range(6,21): # till 20
            print("Weird")
        elif n > 20: 
            print("Not Weird")    
    # end if
    