# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 18:31:53 2018

@author: William Keilsohn 
"""

'''
Check to see if a string is a palindrome.
'''

testString = input('Please enter a string: ')

newString = testString[:]

newString = newString[::-1] #Calls all values through the last one

if newString == testString:
    print('The string is a palindrome!')
else:
    print('The string is not a palindrome.')
    
### Alternative Solution ###
    
inString = input('Please enter a string: ')

cleanedList = list(filter(lambda x: x != ' ', inString))

cleanedString = ''

for i in cleanedList:
    cleanedString += i

finalString = cleanedString[::-1]

if cleanedString == finalString:
    print('The string is a palindrome!')
else:
    print('The string is not a palindrome.')


## You can make adjustments based on if spaces should be accounted for and if special characters will be involved.