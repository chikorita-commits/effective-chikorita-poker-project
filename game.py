'''
Created on Feb 6, 2019

@author: Charles Tao, Tyler

Description: Version 0.05: Added more features

'''
from card import Card
from player import Player
from stack_of_cards import StackOfCards


# These are the winning hands in order of strength
WINNING_HANDS = [ "Royal Flush", \
                  "Straight Flush", \
                  "Four of a Kind", \
                  "Full House", \
                  "Flush", \
                  "Straight", \
                  "3 of a Kind", \
                  "Two Pairs", \
                  "Pair (Jacks or better)" ]

# make a PokerCard Class inherit from Card
class PokerCard(Card):

class PokerHand:
  
# make a PokerGame function
def PokerGame():
    print("This Video Poker project is still in development. Please report bugs")  
    Name = input("what is your name?")
    if Name == "Chikorita":
      print("Greetings developer.")
    else:
      print("Greetings tester.")
    Age = input("HOW OLD ARE YOU? PLEASE BE HONEST.")
    if Age <= 21:
      return "We do not sell credits to players under 21."
    else:
      print("We are proceeding with the game")
      Eula = input("Warning: The game you are playing is very addictive. We are not responsible for any credit losses during your session. Understand?"
             if Eula == "Yes":
                   print("Enough talk. Let's start.")
                   print("How many credits do you have?")
                   if Credits < 1:
                     return "You ran out of credits. Please call your local credit facillity."
                   else:
                     print("Let's play!")
                     print("Credits: "+str(Credits))
                     print(PokerHand)
             else:
                   return "Error: User rejected agreement"
    
    # make the player
    #player = PokerPlayer("Player", 1)
    
    # make a deck of card
    # deck = PokerHand()  # make empty deck
    # add the 52-cards and shuffle
    
    # make rest of the game
    
    #Snapshot 1:
    # Charles and Tyler
    # This is me adding a feature to the game.
    print("You won!")
# add any other helper functions to organize your code nicely
    
def main():
    PokerGame()
    
if __name__ == "__main__":
    main()
    
        










