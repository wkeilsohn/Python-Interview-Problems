# -*- coding: utf-8 -*-
"""
Created on Tue Jan  8 10:36:50 2019

@author: William Keilsohn
"""

'''
You are provided an array of stock prices per day. Write an algorithum that figures out
what days (index of the array) you could buy and sell the stock for max profit.

Note: You should only have to go through the array once.
'''

import numpy as np

prices = [6, 13, 2, 10, 3, 5] # Once again the 'array' provided is given as a list. 

# Thus if we want an actual 'array' in python:
parray = np.array(prices)

# Define Function(s)

### The solution as provided by the course:
def profitFinder(arr): #This is fine, and 'works', but it doesn't answer the question.
    minPrice = arr[0] #Start with the first price
    maxProfit = 0 # Assume no profit
    for i in arr: #Iterate through list
        minPrice = min(minPrice, i) # Determine lowest price
        comProfit = i - minPrice # Find store current profit
        maxProfit = max(maxProfit, comProfit) #Compare to the maximum profit.
    return maxProfit

### Let's try to answer the question

def profitMargin(arr):
    minPrice = arr[0] #Keep this from the example
    maxProfit = 0 # Keep from example
    buyDay = 0 # Going to need a day to actually but
    sellDay = 0 # Going to need a day to sell
    newArray = [] # The question specifically wants a list/array returned.
    for i in arr:
        minPrice = min(minPrice, i) #This is still worth keeping
        comProfit = i - minPrice
        maxProfit = max(maxProfit, comProfit)
        if maxProfit == comProfit: # Checking to see that this is the largest price possible.
            sellDay = arr.index(i)        
    buyDay = arr.index(minPrice) # The question wanted the actual day that the stock could be bought.
    newArray.append(buyDay)#Add the final days to the list
    newArray.append(sellDay) # Remember indexing starts at 0, so day '0' is day 1
    return newArray # Give back the new list

print(profitFinder(prices))
print(profitMargin(prices))