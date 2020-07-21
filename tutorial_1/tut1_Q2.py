# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:20:48 2020

@author: user
"""

if __name__ == '__main__':
    n = int(input())
    
    # get a list of int num < n
    
    if n>=0:
        nlist = range(n)
        nlistSq = [ i**2  for i in nlist]
        #print(nlistSq, sep='\n')
        
        for i in nlistSq:
            #print(i)
            print(i, end ='\n')