# -*- coding: utf-8 -*-
"""
Created on Fri Dec 28 21:30:40 2018

@author: William Keilsohn
"""

'''
Determine if a number is a pallandrome.
'''

numIn = input('Please enter a number: ')

def pallNum(num):
    numLis = list(num)
    if numLis == numLis[::-1]:
        print('The number is a palindrome.')
    else:
        print('The number is not a palindrome.')

pallNum(numIn)