# -*- coding: utf-8 -*-
"""
Created on Mon Jan  7 13:04:26 2019

@author: William Keilsohn
"""

'''
Find the first non-repeated character in a string.
'''

inString = input('Please enter a string: ')

# Define the function:
def charFinder(string): # https://stackoverflow.com/questions/15495731/best-way-to-find-first-non-repeating-character-in-a-string
    chars = {}
    for i in string:
        if i in chars:
            chars[i] += 1
        else:
            chars[i] = 1
    for j in string:
        if chars[j] == 1:
            return j
    return None

# This function is based primarily on the one present at the link. 
# The difference is that I slightly simplified it to reduce the need for a second temporary variable.
# I am aware however, that this may cause a slightly longer runtime depending on the length of the string.

if charFinder(inString) == None: #I don't particularly like it when just 'None' prints to the screen.
    print('Sorry, all letters repeat.')
else:
    print(charFinder(inString))