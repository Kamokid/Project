from enum import Enum
import pygame
import random

CARD_WIDTH = 74
CARD_HEIGHT = 103

class Suits(Enum):
  CLUB = 0
  SPADE = 1
  HEART = 2
  DIAMOND = 3

class Card(pygame.sprite.Sprite):
    """A class to manage a card."""


    def __init__(self, suit, value):
        """Initialize the card and set its starting position."""
        super().__init__()
        self.suit = suit
        self.value = value
        self.image = pygame.image.load('images/'+ self.suit.name +'-'+ str(self.value)+'.svg')
        self.image = pygame.transform.scale(self.image, (CARD_WIDTH , CARD_HEIGHT))
        self.rect = self.image.get_rect()
        self.color = None
        self.set_color()

    def set_color(self):
        color_map = {
            "CLUB": lambda: "BLACK",
            "DIAMOND": lambda: "RED",
            "SPADE": lambda: "BLACK",
            "HEART": lambda: "RED"
        }
        self.color = color_map.get(self.suit.name, lambda: None)()

    def draw(self, surface):
        """Draw the card onto a surface."""
        surface.blit(self.image, self.rect)

    def update(self):
        pass

class Deck():
    """A class to manage the deck of cards."""
   
    def __init__(self):
        super().__init__()
        # self.rect = pygame.Rect(0, 0, CARD_WIDTH, CARD_HEIGHT)
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
    
    def update(self):
        pass
    

class Stock(pygame.sprite.Group):
    """A class to manage the stock."""
    def __init__(self):
        super().__init__()
        self.cardBack = pygame.image.load('images/card_back.png')
        self.rect = self.cardBack.get_rect()
        self.cards = []
        self.x = 50
        self.y = 50
        self.clicked = False
        self.rect1 = pygame.Rect(self.x, self.y, CARD_WIDTH, CARD_HEIGHT)
        self.rect.x = self.x
        self.rect.y = self.y
        # self.spacing = 30
        self.rect_color = (128, 128, 128)

    def is_empty(self):
        return len(self.cards) == 0
    
    def addToStock(self, card):
        """Add a card to the tableau and set its position."""
        card.rect.x = self.x
        card.rect.y = self.y 
        # + self.spacing * len(self.cards)
        self.cards.append(card)
        # super().add(card)
    
    def popTop(self):
        if self.is_empty():
            return None
        card = self.cards.pop()
        super().remove(card)
        return card

    def firstDealStock(self, deck):
        card = deck.deal()
        card.rect.x = self.x
        card.rect.y = self.y
        # card.rect.y = self.y + self.spacing * len(self.cards)
        self.cards.append(card)
        super().add(card)

    def updateStock(self):
        """Update the position of all cards in the stock."""
        for i, card in enumerate(self.cards):
            card.rect.x = self.x
            card.rect.y = self.y
            # card.rect.y = self.y + self.spacing * i

    def draw(self, surface):
        action = False

        # """Draw all the cards in the stock."""
        # for card in self.sprites():
        #     card.draw(surface)

        #Check if stock is empty
        if self.is_empty():
            pygame.draw.rect(surface, (0, 128, 0), self.rect)
            pygame.draw.rect(surface, self.rect_color, self.rect, 3)
        else:
            surface.blit(self.cardBack, (self.rect.x, self.rect.y))

        # get mouse position
        pos = pygame.mouse.get_pos()

        #Check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            pressed_keys = pygame.mouse.get_pressed()
            if (pressed_keys[0] and self.clicked == False):
                self.clicked = True
                action = True
                print("clicked")

        pressed_keys = pygame.mouse.get_pressed()
        if (not pressed_keys[0]):
            self.clicked = False

        return action

class Talon(pygame.sprite.Group):
    """A class to manage the talon."""
    def __init__(self):
        super().__init__() 
        self.cards = []
        self.x = 146
        self.y = 50
        self.rect = pygame.Rect(self.x, self.y, CARD_WIDTH, CARD_HEIGHT)
    
    def addToTalon(self, card):
        card.rect.x = self.x
        card.rect.y = self.y
        self.cards.append(card)

    def moveTop(self):
        # self.cards.pop(-1)
        if self.is_empty():
            return None
        card = self.cards.pop()
        super().remove(card)
        return card
    
    def removeAll(self):
        new_stock = self.cards.copy()
        self.cards.clear()
        super().empty()
        return new_stock
    
    def showCard(self):
        if (len(self.cards) > 0):
            return self.cards[-1]
        else:
             return None
    
    def updateTalon(self):
        """Update the position of all cards in the talon."""
        for i, card in enumerate(self.cards):
            card.rect.x = self.x
            card.rect.y = self.y
            # card.rect.y = self.y + self.spacing * i

    def draw(self, surface):
        """Draw all the cards in the stock."""
        for card in self.sprites():
            card.draw(surface)

    
class Foundation(pygame.sprite.Sprite):
    """A class to manage the foundation."""
    def __init__(self,x,y):
        super().__init__()
        self.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        self.cards = []
        self.x = x
        self.y = y
    
    def add(self, card):
        card.rect.x = self.x
        card.rect.y = self.y
        self.cards.append(card)
    
    def moveTop(self):
        self.cards.pop(-1)
    
    def showCard(self):
        if (len(self.cards) > 0):
            return self.cards[-1]
        else:
             return None
        
    def update(self):
        pass

class Tableau(pygame.sprite.Sprite):
    """A class to manage the Tableau."""
    def __init__(self,x,y):
        super().__init__()
        self.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        self.cards = []
        self.x = x
        self.y = y
    
    def add(self, card):
        card.rect.x = self.x
        card.rect.y = self.y
        self.cards.append(card)

    def moveTop(self):
        self.cards.pop(-1)
    
    def showCard(self):
        if (len(self.cards) > 0):
            return self.cards[-1]
        else:
             return None
    
    def firstDealTableau(self, deck):
        card = deck.deal()
        card.rect.x = self.x
        card.rect.y = self.y
        self.cards.append(card)

    def update(self):
        pass