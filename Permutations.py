# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 08:34:26 2018

@author: William Keilsohn
"""

'''
Print all permutations of a string via iteration and recursion.
'''


inString = input('Please enter a string: ')

# Iteration 
def itPerm(string):
    length = len(string)
    if length <= 1: # We shouldn't waste time with single character/empty stings
        return string
    else:
        for i in range(0, (length ** length)): #https://stackoverflow.com/questions/33312532/generate-all-permutations-of-a-string-in-python-without-using-itertools
            yield ''.join(string[i // length ** (length - j - 1) % length] for j in range(0, length))

# I will admit that this is a tricky problem to deal with. Most similar soultions use recursion.
# Thus I barrowed heavily from the following in this one:
# https://stackoverflow.com/questions/33312532/generate-all-permutations-of-a-string-in-python-without-using-itertools               

# Recursion
def recPerm(string):
    length = len(string)
    if length <= 1: #Once again it is useless to try and find permutations of tiny below a certain size.
        return string
    else:
        vals = []
        for i, j in enumerate(string):
            for a in recPerm(string[:i] + string[i + 1:]):
                vals += [j + a]
    return vals

# Many locations recomend some combiantion of enumerate(i,j) and using a set of 
# substrings with [:i] and [i+1:]. 
# Above and beyond this, there is some room to make changes.             
            
            


# Output Results
print('\n')
print('Iteration results: ', end = '\n')
for x in itPerm(inString):
    print(x)
print('\n')
print('Recursion results: ', end = '\n')
print(recPerm(inString))
        
### Alternative Solution ###
#Import a package
from itertools import permutations

# Find all permutations
results = permutations(inString)

# Output results
print('\n', 'Additional answer results: ', '\n')
for i in results:
    j = ''.join(i) # The package creates tuples
    print(j)

