from enum import Enum
import pygame
import random

# # Define card suits and values
# # C for Clubs, D for Diamonds, H for Hearts, S for Spades
# suits = ['C', 'D', 'H', 'S']
# values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# # Define card class and sets the ranks for each card.
# ranks = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

class Suits(Enum):
  CLUB = 0
  SPADE = 1
  HEART = 2
  DIAMOND = 3

class Card:
    """A class to manage a card."""

    # def __init__(self, sol_game, suit, value):
    def __init__(self, suit, value):
        """Initialize the card and set its starting position."""
        self.suit = suit
        self.value = value
        self.image = pygame.image.load('images/'+ self.suit.name +'-'+ str(self.value)+'.svg')
        # self.image = pygame.image.load('images/CLUB-1.svg')

        # """Initialize the card and set its starting position."""
        # self.screen = sol_game.screen
        # self.screen_rect = sol_game.screen.get_rect()

        # Load the ship image and get its rect.
        
        # self.rect = self.image.get_rect()

        # # Start each new ship at the bottom center of the screen.
        # SHIP_OFFSET = 50  # adjust this value to position the ship as desired
        # self.rect.topleft = (
        # self.screen_rect.left + SHIP_OFFSET,
        # self.screen_rect.top + SHIP_OFFSET,
        #   )

class Deck:
    """A class to manage the deck of card."""
   
    def __init__(self):
        self.cards = []
        for suit in Suits:
            for value in range(1,14):
                self.cards.append(Card(suit, value))
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()
    
    def length(self):
        return len(self.cards)
    

class Stock:
    """A class to manage the stock."""
    def __init__(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)
    
    def popTop(self):
        self.cards.pop(-1)

class Talon:
    """A class to manage the talon."""
    def __init__(self):
        self.cards = []
    
    def add(self, card):
        self.cards.append(card)
    
    def removeAll(self):
        return self.cards
    
class Foundation:
    """A class to manage the foundation."""
    def __init__(self):
        self.cards = []
    
    def add(self, card):
        self.cards.append(card)
    
    def moveTop(self):
        self.cards.pop(-1)

class Tableau:
    """A class to manage the Tableau."""
    def __init__(self):
        self.cards = []
    
    def add(self, card):
        self.cards.append(card)

    def moveTop(self):
        self.cards.pop(-1)
    