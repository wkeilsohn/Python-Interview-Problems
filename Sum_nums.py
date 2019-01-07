# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 21:16:00 2018

@author: William Keilsohn
"""

'''
Find the sum of digits of a number using recursion.
'''

inNum = int(input('Please enter a number: '))

def sumDigits(num):    
    numLis = list(str(num))
    if len(numLis) == 1: # If it is a single digit, there is no reason to progress further.
        return num
    elif num % 10 == 0: # Multiples of ten can be left as is. 
        return num
    else:
        for i in numLis:
            return sumDigits(num // 10) + (num % 10) # Add the tens to the remainders
            
    
print(sumDigits(inNum))