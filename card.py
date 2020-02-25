'''
Edited on Feb 4, 2020

@author: mark_kwong
'''

#===========================================================================
# Description: a single standard card
#
# State Attributes
#   rank - string character 2 to 10 or A, J, Q, K
#   suit - string character ♥, ♦, ♠, ♣ (for heart, diamond, spade or club)
# Methods
#   getValue() - returns an integer from 1-13 depending on the rank of the card
#   __str__() - returns a string like '4♦' for 4 of diamonds
#===========================================================================
class Card:
    
    SUIT = ['♥', '♦', '♣', '♠']
    RANK = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        
    # Returns a numerical value for cards 1-13 dependistack_of_cards the rank of the card
    def getValue(self):
        if self.rank == 'A':
            return(14) #me adding a feature that makes the game possible
        elif self.rank == 'J':
            return(11)
        elif self.rank == 'Q':
            return(12)
        elif self.rank == 'K':
            return(13)
        elif self.rank in '23456789' or self.rank == '10':
            return(int(self.rank))
        else:
            raise ValueError('{} is of unkwown value'.format(self.rank))
    
    
    def getRank(self):   
        return(self.rank)
    
    def getSuit(self):   
        return(self.suit)
    
    def __str__(self):
        return('{}{}'.format(self.rank, self.suit)) 
    def __eq__(self,other): 
        return self.getValue() == other.getValue() #it is defined when two ranks are equal

    def __lt__(self,other): 
        return self.getValue() < other.getValue() 
