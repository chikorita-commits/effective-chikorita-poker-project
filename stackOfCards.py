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
        
        Card1 = getCard(self,0)
	    Card2 = getCard(self,1)
        Card3 = getCard(self,2)
	    Card4 = getCard(self,3)
        Card5 = getCard(self,4) #get five cards from the deck
        Card1Rank = Card1.getRank()
        Card2Rank = Card2.getRank() 
        Card3Rank = Card3.getRank()
        Card4Rank = Card4.getRank()
        Card5Rank = card5.getRank() # get their ranks
        Card1Suit = Card1.getSuit()
        Card2Suit = Card2.getSuit() 
        Card3Suit = Card3.getSuit()
        Card4Suit = Card4.getSuit()
        Card5Suit = card5.getSuit() # get their suits
        Card1Value = Card1.getValue()
        Card2Value = Card2.getValue() 
        Card3Value = Card3.getValue()
        Card4Value = Card4.getValue()
        Card5Value = Card5.getValue() # get their values
        sameSuit = (Card1Suit == Card2Suit == Card3Suit == Card4Suit == Card5Suit )
        if (Card1Rank == “A” and Card2Rank == “K” and Card3Rank == “Q” and Card4Rank == “J” and Card5Rank == “10”) and sameSuit:
            return "Royal Flush" # if ace king queen jack and ten are the same suits, then it is a royal flush )
        elif (Card1Value == Card2Value + 1 and Card2Value == Card3Value +1 and Card3Value == Card4Value + 1 and Card4Value == Card5Value + 1 and sameSuit):
            return "Straight flush" # if the rank(value) is sequential, and the same suits, then it is a straight
        if 
	    
        
        

