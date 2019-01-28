#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 07:42:18 2019

@author: William Keilsohn
"""
# Find all prime numbers between 0 and a given number, n:

# First, a prime number is a number who's only two factors are 1 and itself.
# Additionally, 1 is not typically considered a prime number, but 2 is. 

# Collect user input:
inNum = int(input('Please enter a number:' ))

# Define the function:
def primeFinder(num):
    num +=1 # Just incase the number itself is prime, I want to make sure it gets checked.
    if num  < 2: # Remember, 2 is the smallest prime number.
        print('Number too small.')
        return
    for i in range(num): # https://hackernoon.com/prime-numbers-using-python-824ff4b3ea19
        prime = True 
        for j in range(2, i):
            if i % j == 0: # Checks if any factors for a number exist. 
                prime = False
                break # If one exists, we can stop checking as the number is not prime. 
        if prime == True:
            print(str(i)) # Print out all the primes.
        
# Return user requested output:        
print('\n') # I like a little formatting/spacing for my output
primeFinder(inNum)