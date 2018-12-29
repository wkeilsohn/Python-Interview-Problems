# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 21:37:43 2018

@author: William Keilsohn
"""

'''
Count the accurance of a given character in a string.
'''

# Import packages
import re

inString = input('Please enter a string: ')
inChar = input('Please enter a single character to search for: ')

def charFinder(string, char):
    outList = re.findall(char, string)
    outLength = len(outList)
    print(outLength)

charFinder(inString, inChar)

## Print is used to display to the console.
## Return is also a viable option here 