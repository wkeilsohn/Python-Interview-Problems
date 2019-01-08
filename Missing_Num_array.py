# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 09:42:56 2019

@author: William Keilsohn
"""

'''
In an array 1-100 numbers are stored. One number is missing. How do you find it?
'''

'''
This could be worded better. So I'm going to make some assumptions:
    1 - The array is the numbers 1 -100 inclusive
    2 - The array, like many in these questions/examples, is 1-d
    3 - A random number has been taken from the array.
    4 - The array is in random order.
'''

# Given these assumptions, packages are inorder:
import random

test = [i for i in range(1, 101)] # Remember, python is exclusive on the last digit.
random.shuffle(test)

x = random.randint(1, 100) # Pick a random number

del test[x] # Delete the number with that index value from the list. 

for i in range(1, 101): # Easy and simple.
    if i not in test:
        print(i)
        break
    
# It wouldn't be hard to delete the number itself from the list, but then that number would be stored as a variable, and thus not unknown.