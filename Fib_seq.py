# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 11:32:05 2018

@author: William Keilsohn
"""

'''
Find the Nth fibinachi number iterativly and recursivly.
'''

inNum = int(input('Please enter a number: '))

# Iterativly
def itFibFinder(num):
    i, j = 0, 1
    for x in range(0, num):
        i, j = j, i + j
    return i

# Recursivly
def fibFinder(num):
    if num <= 1:
        return num
    else:
        return fibFinder(num - 1) + fibFinder(num - 2)

print(itFibFinder(inNum))    
print(fibFinder(inNum))

# Honestly, this has been done a million times.
# The answer is pretty standard everywhere. 