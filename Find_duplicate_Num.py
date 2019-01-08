# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 12:29:48 2019

@author: kingw
"""

'''
In an array 1-100 exactly one number is duplicate how do you find it?
'''

'''
Once again there is some poor wording in this question so here are some assumptions:
    1 - The numbers are 1 to 100 inclusive
    2 - The numbers are shuffled
    3 - The duplicated number is mixed in with the others (not just at the end)
    4 - The array is 1-d
'''

# Import some packages!
import random

test = [i for i in range(1, 101)]

# Now a i don't want to know what the extra number is, I'm going to write a function to add it.
def addNum(lis):
    x = random.randint(0, 99)
    y = random.randint(1, 100)
    lis.insert(x, y)
    random.shuffle(lis)
    return lis

addNum(test)

def dupFinder(lis):
    dic = {}
    for i in lis:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    for j in dic:
        if dic[j] == 2: # This could also just be < 1, but eh, lets keep it simple.
            dup = j
    return dup
        
print(dupFinder(test))
    
## Generally it seems to be understood that if you want to count something you 
## create a hash table or dictionay and use it to keep track of the number of times the item appears.
    