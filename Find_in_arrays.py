# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 09:21:59 2019

@author: William Keilsohn
"""

'''
Given two arrays, find which number from the first is not present in the second.
'''

# Import Packages
import numpy as np

# Create arrays
data1 = [1, 2, 3, 4, 5] # These are the 'arrays' provided by the original online prompt.
data2 = [2 ,3, 1, 0, 5]

#  'Arrays' as lists:
## If the arrays are one dimentional, and thus, in python act as lists, then...

for i in data1:
    if i not in data2:
        print(i)
        break #Easy answer and we can stop here.

# 'Arrays' as actual arrays
## If we actually wish to treat the array as an actual array then...
darray1 = np.array(data1)
darray2 = np.array(data2)

## Of course, this still being a 1-d array the same solution still applies
for j in darray1:
    if j not in darray2:
        print(i)
        break

# Just to confirm both are working:
if i == j:
    print(True)
else:
    print(False)