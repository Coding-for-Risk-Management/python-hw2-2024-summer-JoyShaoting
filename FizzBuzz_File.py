#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 17:21:56 2024

@author: Joy
"""

import numpy as np

def FizzBuzz(start, finish):
    fbRange=np.arange(start,finish+1)
    mod3=np.mod(fbRange,3)
    mod5=np.mod(fbRange,5)
    mod15=np.mod(fbRange,15)
    fizzbuzz=fbRange.astype(object)
    fizzbuzz[mod15 == 0] = "fizzbuzz"
    fizzbuzz[mod3 == 0] = "fizz"
    fizzbuzz[mod5 == 0] = "buzz"
   
    return(fizzbuzz)

#Tools: Create point array for objects
start = 1
finish = 15
numvec = np.arange(start,finish)
objvec = np.array(numvec,dtype = object)

# Tools: Append to a list

myEmptyList = []
for i in range(1,5):
    myEmptyList.append(i)
    
print(myEmptyList)
