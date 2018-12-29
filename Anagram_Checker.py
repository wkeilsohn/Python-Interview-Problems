# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 14:02:35 2018

@author: William Keilsohn
"""

'''
Determine if two strings are anagrams of eachother.
'''

St1 = input('Please enter the first string: ')
St2 = input('Please enter the second string: ')

def areAnagrams(string1, string2):
    Lis1, Lis2 = sorted(list(string1)), sorted(list(string2))
    if Lis1 == Lis2:
        print('The strings are anagrams.')
    else:
        print('The strings are not anagrams.')
        
areAnagrams(St1, St2)