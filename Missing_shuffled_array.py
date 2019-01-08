# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 11:30:57 2019

@author: William Keilsohn
"""

'''
Consider an array of non-segative integers. 
A second array is formed by shuffeling the array and then deleting a value.
Find the missing value.
'''

### The problem it's self provided the following arrays:
test1 = [1,2,3,4,5]
test2 = [1,3,4,5]

### However, this arguably does not meet ALL conditions of the prompt, so lets make some data that does.
import numpy as np
import random

sample1 = np.random.randint(0, high = 100, size = (50))# Creates an array of 50 positive integers between 0-99
sample2 = np.copy(sample1) #Copy the array and save it sepperatly.
random.shuffle(sample2) #Shuffle the array

x = random.randint(0, 50) # pick a random index

sample2 = np.delete(sample2, x, 0) # Remove the number at that index.

# Define the function(s)
def numChecker(arr1, arr2): #Seemes like the simplist answer to me. 
    for i in arr1:
        if i not in arr2:
            return i
        
    
print(numChecker(test1, test2))
print(numChecker(sample1, sample2))

# The course provided a much more complex answer. 

