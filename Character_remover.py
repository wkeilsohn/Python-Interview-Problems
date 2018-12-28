# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 19:59:29 2018

@author: William Keilsohn
"""

'''
Remove a given character from a string.
'''

inString = input('Please enter a string: ')
inChar = input('Please enter a character you would like to remove: ')

cleanedLis = list(filter(lambda x: x != inChar, inString))

outString = ''
for i in cleanedLis:
    outString += i
    
print(outString)

### Alternative Solution ###

newLis = list(inString)

outPut = ''

for i in newLis:
    if i != inChar:
        outPut += i

print(outPut)
    
## Additional rules can be added if you want to deal with capital vs. lowercase letters.