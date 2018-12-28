# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 09:32:46 2018

@author: William Keilsohn 
"""

'''
Create a standard deck of cards and then draw two cards from it at random.
'''

# Import Packages
import random

# Create deck of carsds

class Cards:
    
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

suitLis = ['Heart', 'Club', 'Spade', 'Diamond']
cards = [Cards(suit, value) for suit in suitLis for value in range(2, 15)]

# Call and print the random pair.
pair1 = random.sample(cards, 2)

for x in pair1:
    print(x.value, ' of ',  end = '')
    print(x.suit)


### Alternative Solution ###
# Create Deck of Cards
suits = ['Heart', 'Club', 'Spade', 'Diamond']
values = [i for i in range(2, 11)]
values += ['J', 'Q', 'K', 'A']

cards2 = []
for i in suits:
    for j in values:
        card = [i, j]
        cards2.append(card)

# Call and view the random Pair
pair2 = random.sample(cards2, 2)
print(pair2)