# -*- coding: utf-8 -*-
"""
Created on Sun Dec 30 16:58:43 2018

@author: William Keilsohn
"""

'''
Find all prime numbers up to a given number.
'''

# Collect input
inNum = int(input('Please enter the maximum number you would like to go up to: '))

# Define functions
def isPrime(num):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
            break
    return prime

def primeFinder(num): # Technically 1 is not prime... 
    vals = [x for x in range(2, (num + 1))]# Just incase the number you enter is prime, it should be included.
    for j in vals:
        if isPrime(j):
            print(j)
    
# Accept input and output results
primeFinder(inNum)
        