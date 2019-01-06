# -*- coding: utf-8 -*-
"""
Created on Sun Jan  6 16:40:40 2019

@author: William Keilsohn
"""

'''
Find the factorial of a number, recursivly.
'''

#inNum = int(input('Please enter a number: ')) #This is commented out as I want to call the central function for another file.

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    

#print(factorial(inNum))

### Thid is a pretty standard answer. 