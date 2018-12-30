# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 21:56:51 2018

@author: William Keilsohn
"""

'''
Check if a given number is binary.
'''

inNum = int(input('Please enter a number: '))

def binChecker(num):
    Num = str(num) # This could be removed by accepting the string input. However, that wouldn't allow the program to take a number. 
    numLis = list(Num)
    total = 0
    for i in numLis:
        if i == '0' or i == '1':
            total += 0
        else:
            total += 1
    if total == 0:
        print('The number is binary')
    else:
        print('The number is not binary')

binChecker(inNum)
        
### Alternative Solution ###
def isBinary(num):
    Num = str(num)
    numLis = list(Num)
    Looper = True
    for i in numLis:
        if i not in ['1', '0']:
            Looper = False
            return "The number is not binary."
    if Looper:
        return "The number is binary."
            
print(isBinary(inNum))
            
### As you can see there is a lot of room for variation between the two programs. The choice is really a matter of how one wants to check for the 0's and 1's.