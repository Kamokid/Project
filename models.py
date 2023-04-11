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
        self.rect1 = pygame.Rect(self.x, self.y, CARD_WIDTH, CARD_HEIGHT)
        self.rect.x = self.x
        self.rect.y = self.y
        # self.spacing = 30
        self.rect_color = (128, 128, 128)
        self.clicked = False

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
        self.clicked = False
        self.clicked_card = None
    
    def is_empty(self):
        return len(self.cards) == 0

    def addToTalon(self, card):
        card.rect.x = self.x
        card.rect.y = self.y
        self.cards.append(card)

    def moveTop(self):
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
    
    # def showCard(self):
    #     if (len(self.cards) > 0):
    #         return self.cards[-1]
    #     else:
    #          return None
    
    def updateTalon(self):
        """Update the position of all cards in the talon."""
        for i, card in enumerate(self.cards):
            card.rect.x = self.x
            card.rect.y = self.y
            # card.rect.y = self.y + self.spacing * i

    def draw(self, surface):
        
        """Draw all the cards in the talon."""
        for card in (self.sprites()):
            surface.blit(card.image, card.rect)

            # Check if the card is clicked
            if self.clicked_card == card:
                # Move the card to the mouse position
                mouse_pos = pygame.mouse.get_pos()
                card.rect.center = mouse_pos
        
        # Check if the left mouse button is pressed
        if pygame.mouse.get_pressed()[0]:
            # Check if the mouse is over a card in the talon
            for card in reversed(self.sprites()):
                if card.rect.collidepoint(pygame.mouse.get_pos()):
                    self.clicked_card = card
                    break
        
        # Check if the left mouse button is released
        if not pygame.mouse.get_pressed()[0]:
            self.clicked_card = None
            self.updateTalon()

        return self.clicked_card
        # action = False

        # """Draw all the cards in the talon."""
        # for card in self.sprites():
        #     card.draw(surface)

        # get mouse position
        # pos = pygame.mouse.get_pos()

        # for card in self.sprites():

        #     #Check mouseover and clicked conditions
        #     if card.rect.collidepoint(pos):
        #         pressed_keys = pygame.mouse.get_pressed()
        #         if (pressed_keys[0] and self.clicked == False):
        #             self.clicked = True
        #             if self.clicked:
        #                 card.rect.x = pos[0]-(card.rect.width/2)
        #                 card.rect.y = pos[1]-(card.rect.width/2)
        #             # action = True
        #             print("clicked")

        # pressed_keys = pygame.mouse.get_pressed()
        # if (not pressed_keys[0]):
        #     self.clicked = False

        # return action

class Tableau(pygame.sprite.Group):
    """A class to manage the Tableau."""
    def __init__(self,x,y):
        super().__init__()
        self.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        self.cards = []
        self.x = x
        self.y = y
        self.rect_color = (128, 128, 128)
        self.clicked = False
        self.clicked_card = None
    
    def is_empty(self):
        return len(self.cards) == 0
    
    def addToTableau(self, card):
        card.rect.x = self.x
        card.rect.y = self.y
        self.cards.append(card)
        super().add(card)

    def moveTop(self):
        if self.is_empty():
            return None
        card = self.cards.pop()
        super().remove(card)
        return card
    
    def can_add_card(self, card):
        
        # Check if the tableau is empty
        if self.is_empty():
            if card.value == 13:
                return True
            else:
                return False      
        else:
            # Check if the cards have different colors
            if card.color != self.cards[-1].color:
               # Check if the card is lesser than the last card by 1
               if card.value - self.cards[-1].value == -1:
                    return True   
               else:
                    return False       
            else:
                return False
    
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
        super().add(card)

    def updateTableau(self):
        """Update the position of all cards in the stock."""
        for i, card in enumerate(self.cards):
            card.rect.x = self.x
            card.rect.y = self.y
            # card.rect.y = self.y + self.spacing * i

    def draw(self, surface):

         #Check if stock is empty
        if self.is_empty():
            pygame.draw.rect(surface, (0, 128, 0), self.rect)
            pygame.draw.rect(surface, self.rect_color, self.rect, 3)
        else:
            """Draw all the cards in the talon."""
            for card in self.sprites():
                surface.blit(card.image, card.rect)

            # Check if the card is clicked
            if self.clicked_card == card:
                # Move the card to the mouse position
                mouse_pos = pygame.mouse.get_pos()
                card.rect.center = mouse_pos
        
        # Check if the left mouse button is pressed
        if pygame.mouse.get_pressed()[0]:
            # Check if the mouse is over a card in the talon
            for card in reversed(self.sprites()):
                if card.rect.collidepoint(pygame.mouse.get_pos()):
                    self.clicked_card = card
                    break
        
        # Check if the left mouse button is released
        if not pygame.mouse.get_pressed()[0]:
            self.clicked_card = None
            self.updateTableau()

        return self.clicked_card
    
class Foundation(pygame.sprite.Group):
    """A class to manage the foundation."""
    def __init__(self,x,y):
        super().__init__()
        self.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        self.cards = []
        self.x = x
        self.y = y
        self.rect_color = (128, 128, 128)
        self.clicked = False
        self.clicked_card = None

    def is_empty(self):
        return len(self.cards) == 0
    
    def addToFoundation(self, card):   
        card.rect.x = self.x
        card.rect.y = self.y
        self.cards.append(card)
        super().add(card)
         
    def moveTop(self):
        # self.cards.pop(-1)
        if self.is_empty():
            return None
        card = self.cards.pop()
        super().remove(card)
        return card
    
    # def showCard(self):
    #     if (len(self.cards) > 0):
    #         return self.cards[-1]
    #     else:
    #          return None

    def can_add_card(self, card):
        
        # Check if the foundation is empty
        if self.is_empty():
            if card.value == 1:
                return True
            else:
                return False      
        else:
            # Check if the card has the same suit as the foundation
            if card.suit.name == self.cards[-1].suit.name:
               # Check if the card is greater than the last card in the foundation by 1
               if card.value - self.cards[-1].value == 1:
                    return True   
               else:
                    return False       
            else:
                return False

    def updateFoundation(self):
        """Update the position of all cards in the stock."""
        for i, card in enumerate(self.cards):
            card.rect.x = self.x
            card.rect.y = self.y
            # card.rect.y = self.y + self.spacing * i

    def draw(self, surface):

        #Check if stock is empty
        if self.is_empty():
            pygame.draw.rect(surface, (0, 128, 0), self.rect)
            pygame.draw.rect(surface, self.rect_color, self.rect, 3)
        else:
            """Draw all the cards in the talon."""
            for card in self.sprites():
                surface.blit(card.image, card.rect)

            # Check if the card is clicked
            if self.clicked_card == card:
                # Move the card to the mouse position
                mouse_pos = pygame.mouse.get_pos()
                card.rect.center = mouse_pos
        
        # Check if the left mouse button is pressed
        if pygame.mouse.get_pressed()[0]:
            # Check if the mouse is over a card in the talon
            for card in reversed(self.sprites()):
                if card.rect.collidepoint(pygame.mouse.get_pos()):
                    self.clicked_card = card
                    break
        
        # Check if the left mouse button is released
        if not pygame.mouse.get_pressed()[0]:
            self.clicked_card = None
            self.updateFoundation()

        return self.clicked_card