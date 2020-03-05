'''
Edited Feb 4, 2020

@author: mark_kwong
'''
import random

from pip._internal.utils.outdated import SELFCHECK_DATE_FMT

import card


#===========================================================================
# Description: A list of Card; used for a player's hand or a deck of cards
#
# State Attributes
#     - cards - list of card; starts out empty
# Methods
#     - shuffle() - randomly shuffle all the card in the list
#     - deal() - deal the 'top' card from the hand/deck
#     - add(card) - add Card to the list of cards
#     - remove(pos) - remove and return Card at pos number
#     - size() - size of hand
#     - getCard(pos) - returns a Card at the 'pos'
#     - __str__() - returns string of all the cards in the hand like '4♣ 10♥ A♠'
#===========================================================================
class StackOfCards(Card): # inherits from card

    def __init__(self):
        '''
        Constructor
        '''
        self.cards = []
        
    # returns a string of all the cards in the 'deck'
    def __str__(self):
        s = ''
        for card in self.cards:
            if len(s) == 1:
                s = s + str(card)
            else:
                s = s + ' ' + str(card)
        s = s
        return(s)
    
    # Add card to the 'bottom' of the deck of cards
    def add(self, card):
        self.cards.append(card)
                
    def remove(self, pos):
        card = self.cards.pop(pos)
        return card
               
    # Deal card from the 'top' of the deck of cards
    def deal(self):
        return self.cards.pop(0)
        
    def shuffle(self):
        random.shuffle(self.cards)
        
    def size(self):
        return(len(self.cards))
    
        return(self.cards[pos])
    def sort(self):
        self.cards.sort()
    def handType(self):
        
     # WINNING_HANDS = [ "Royal Flush", \
#                  "Straight Flush", \
#                  "Four of a Kind", \
#                  "Full House", \
#                  "Flush", \
#                  "Straight", \
#                  "3 of a Kind", \
#                 "Two Pairs", \
#                  "Pair (Jacks or better)" ]
def handType(self):
        if(self.cards[0].getValue()==10 and self.cards[1].getValue==11 and self.cards[2].getValue==12 and self.cards[3].getValue()==13 and self.cards[4].getValue==14):
            return WINNING_HANDS[0]
        elif(self.cards[0].getValue()==self.cards[1].getValue()-1 and self.cards[2].getValue()-1==self.cards[1].getValue() and self.cards[3].getValue()-1==self.cards[2].getValue() and self.cards[4].getValue()-1==self.cards[3].getValue()):
            if(self.cards[0].getRank()==self.cards[1].getRank()==self.cards[2].getRank()==self.cards[3].getRank()==self.cards[4].getRank()):
                return WINNING_HANDS[1]
        elif(self.cards[0].getRank()==self.cards[1].getRank()==self.cards[2].getRank()==self.cards[3].getRank()==self.cards[4].getRank()):
            return WINNING_HANDS[4]
        elif(self.cards[0].getValue()==self.cards[1].getValue()==self.cards[2].getValue()==self.cards[3].getValue()==self.cards[4].getValue()):
            return WINNING_HANDS[2]
        elif(self.cards[1].getValue()==self.cards[2].getValue()==self.cards[3].getValue()==self.cards[4].getValue()):
            return WINNING_HANDS[2]
        elif(self.cards[0].getRank()==self.cards[1].getRank()==self.cards[2].getRank()) and(  self.cards[3].getRank()==self.cards[4].getRank()):
            return WINNING_HANDS[3] #FULL HOUSE
        elif self.cards[0].getRank() == self.cards[1].getRank()+1 == self.cards[2].getRank()+2 == self.cards[3].getRank()+3 == self.cards[4].getRank()+4:
            return WINNING_HANDS[5] #straight
        elif (self.cards[0].getValue()==self.cards[1].getValue()==self.cards[2].getValue()):
            return WINNING_HANDS[6] #3 of kind 1: part 1: three of the same
        elif (self.cards[1].getValue()==self.cards[2].getValue()==self.cards[3].getValue()):
            return WINNING_HANDS[6] 
		elif (self.cards[2].getValue()==self.cards[3].getValue()==self.cards[4].getValue()):
            return WINNING_HANDS[6] 
        elif (self.cards[0].getvalue()==self.cards[1].getvalue()) and (self.cards[3].getvalue()==self.cards[4].getvalue()):
            return WINNING_HANDS[7]
   
        
        
