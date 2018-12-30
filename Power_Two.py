# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 09:02:12 2018

@author: William Keilsohn
"""

'''
Determine if a number is a power of 2.
'''
# Import Packages
import math

# Collect data
inNum = int(input('Please enter a number: '))

# Define functions
def isTwoPower(num):
    base = math.log2(num)
    if base.is_integer():
        print('The number is a power of two.')
    else:
        print('The number is not a power of two.')
        
# Process input and return results
isTwoPower(inNum)