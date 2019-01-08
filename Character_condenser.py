# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 09:57:37 2019

@author: William Keilsohn
"""

'''
Given a string with several repeating characters. Produce a string with counts of each character.
'''

test = 'AAAABBBBCCCCCDDEEEE'
test2 = 'ABACCDBFAACBBBDFAAAC'

# Define Function:
### My personal attempt below.

def charCounter(string): ### This works!
    stringDic = {}
    newString = ''
    if len(string) == 0:
        return '' # Deal with the one exception case where the string is empty.
    for i in string:
        if i in stringDic:
            stringDic[i] += 1 # Count the number of letters in a string
        else:
            stringDic[i] = 1 # Start a new letter
    for j in stringDic:
        newString = newString + j # Add the letter
        newString = newString + str(stringDic[j]) # Add the counts
    return newString

print(charCounter(test))
print(charCounter(test2))

### The course did provide a soultion to this. It was noticably longer and arguably 
### not as dry as the one above. I'm sure it can be easily found online however. 
    