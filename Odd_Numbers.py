# -*- coding: utf-8 -*-
"""
Spyder Editor

Author: William Keilsohn
"""

'''
Prompt: Find all the odd numbers between 0 - 100?
'''

for i in range(0, 100):
    if i % 2 == 1:
        print(i)

# This is a simple answer which will only print it. 
# To obtain a list...

lis = []
for i in range(1, 100, 2):
    lis.append(i)


### Solutions can be altered to account for larger sample sizes. 
### Stepping through by 2 prevents checking for odd numbers.
### Range is exclusive on the last increment.
