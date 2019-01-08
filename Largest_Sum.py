# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 09:44:23 2019

@author: William Keilsohn 
"""

'''
Given an array of itegers (positive and negative) write a program that can find the 
largest continuous sum.
'''

test = [10, -1, 11, 23, 4, -3]


# Solution based on course solution from:
# https://www.udemy.com/data-science-career-guide-interview-preparation/learn/v4/content

def findSum(arr): # This is the major function the course walks through.
    if len(arr) == 0:
        return 0
    val1 = arr[0]
    val2 = arr[0]
    for i in arr[1:]:
        val2 = max(val2 + i, i) # Checking to see if we get a larger number if we add the next in the list/array.
        val1 = max(val2, val1) # Checking to see if this new variable is larger than our current maximum
    return val1

print(findSum(test))