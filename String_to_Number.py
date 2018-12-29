# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 21:47:45 2018

@author: William Keilsohn
"""

'''
Convert a numeric string into a number (specifically an integer).
'''

inString = input('Please enter a numeric string: ')

print(type(inString))

outString = int(inString) ### Only essential portion!

print(outString, ' : ',  type(outString))

## Python, unlike some other languages, already has a built in way of converting
## between a string and an integer. Thus the simplist solution is just to call it.