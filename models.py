from enum import Enum
import pygame
import copy
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
        # self.rect1 = pygame.Rect(self.x, self.y, CARD_WIDTH, CARD_HEIGHT)
        self.rect.x = self.x
        self.rect.y = self.y
        # self.spacing = 30
        self.rect_color = (128, 128, 128)

    def is_empty(self):
        return len(self.cards) == 0
    
    def addToStock(self, card):
        """Add a card to the stock and set its position."""
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
        #Check if stock is empty
        if self.is_empty():
            pygame.draw.rect(surface, (0, 128, 0), self.rect)
            pygame.draw.rect(surface, self.rect_color, self.rect, 3)
        else:
            surface.blit(self.cardBack, (self.rect.x, self.rect.y))

class Talon(pygame.sprite.Group):
    """A class to manage the talon."""
    def __init__(self):
        super().__init__() 
        self.cards = []
        self.x = 146
        self.y = 50
        self.rect = pygame.Rect(self.x, self.y, CARD_WIDTH, CARD_HEIGHT)
    
    def is_empty(self):
        return len(self.cards) == 0

    def addToTalon(self, card):
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
    
    def removeAll(self):
        new_stock = self.cards.copy()
        self.cards.clear()
        super().empty()
        return new_stock
    
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

class Image:
    """A class to manage the tableau image."""
    def __init__(self):
        self.cardBack = pygame.image.load('images/card_back.png')
        self.rect = self.cardBack.get_rect()

class Tableau(pygame.sprite.Group):
    """A class to manage the Tableau."""
    def __init__(self,x,y,z):
        super().__init__()
        self.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        self.cards = []
        self.cards2 =[]
        self.cards2Count = 0 
        self.rect.height = 103 + (12*z)
        self.x = x
        self.y = y
        self.z = z
        self.rect_color = (128, 128, 128)
        self.spacing = 15
        self.imageBack =[]
        self.populateImage()
    
    def is_empty(self):
        return len(self.cards) == 0
    
    def is_cards2empty(self):
        return len(self.cards2) == 0
    
    def populateImage(self):
        # Populates the images for a tableau using z
        if self.z > 0:
            for i in range(self.z):
                image = Image()
                image.rect.x = self.x
                image.rect.y = self.y + self.spacing * i
                self.imageBack.append(image)
    
    def addToTableau(self, card):
        if self.is_empty():
            card.rect.x = self.x
            card.rect.y = self.y
        else:
            card.rect.x = self.x
            card.rect.y = self.y + self.spacing * len(self.cards)
            self.rect.height += 12

        self.cards.append(card)
        super().add(card)

    def addBackToTableau(self,card):

        self.cards.append(card)
        self.rect.height += 12
        super().add(card)

    # def remainingCardsBackToTableau(self):

    #     if self.cards2Count == 1:
    #         self.deleteImage()
    #         self.clearAllCards2()

    #     elif len(self.cards2Count) > 1:
    #         for card in self.cards2[:-1]:
    #             self.cards.append(card)
    #             super().add(card)
    #             self.rect.height += 12
    #             print("/////////")
    #             print("Adding Remaining Cards Back")
    #             print("Card value:", card.value)
    #             print("Card suit:", card.suit.name)
    #             # print()

    #             x = card.rect.x
    #             y = card.rect.y
    #             width = card.rect.width
    #             height = card.rect.height

    #                             # Determine the boundaries
    #             left = x
    #             right = x + width
    #             top = y
    #             bottom = y + height

    #                             # Print the boundaries
    #             print("Left:", left)
    #             print("Right:", right)
    #             print("Top:", top)
    #             print("Bottom:", bottom)   
    #         self.clearAllCards2()

    # def addBackToTableauX(self):
    #     for card in self.cards2:
    #         self.cards.append(card)
    #         super().add(card)
    #         self.rect.height += 12
    #         print("/////////")
    #         print("Adding Back")
    #         print("Card value:", card.value)
    #         print("Card suit:", card.suit.name)
    #         # print()

    #         x = card.rect.x
    #         y = card.rect.y
    #         width = card.rect.width
    #         height = card.rect.height

    #                         # Determine the boundaries
    #         left = x
    #         right = x + width
    #         top = y
    #         bottom = y + height

    #                         # Print the boundaries
    #         print("Left:", left)
    #         print("Right:", right)
    #         print("Top:", top)
    #         print("Bottom:", bottom)   
    #     self.clearAllCards2()
    
    def moveAdded(self):
        if self.is_empty():
            return [] 
        else:
            #Check if imageBack is empty
            if self.imageBack:
                #Check if imageBack has reduced from its initial length of z
                if len(self.imageBack) == self.z:
                    
                    #Check if card has been added to the tableau
                    if len(self.sprites()) - len(self.imageBack) > 1:

                        n = len(self.sprites()) - len(self.imageBack)

                        for i in range(-n, 0):               
                            self.cards2.append(self.cards[i])
                            super().remove(self.cards[i])
                            self.cards.pop(i)
                            self.rect.height -= 12

                    elif len(self.cards) - len(self.imageBack) == 1:

                         # Get the last card sprite in the tableau
                        self.cards2.append(self.cards[-1])
                        super().remove(self.cards[-1])
                        self.cards.pop(-1)
                        self.rect.height -= 12
         
                # If imageBack has reduced from its initial length of z
                else:
                    # Get the difference between the cards in the tableau and imageBack i.e the cards not revealed yet
                    n = len(self.cards) - len(self.imageBack)
                    for i in range(-n, 0):
                        self.cards2.append(self.cards[i])
                        super().remove(self.cards[i])
                        self.cards.pop(i)
                        self.rect.height -= 12        
  
            else:
                """Draw all the cards in the talon."""

                while  self.cards:
                    super().remove(self.cards[0])
                    self.cards2.append(self.cards.pop(0))
                self.rect.height = 103

            # print("/////////")
            # print("move added")
            # for card in self.cards2:
            #     print("Card value:", card.value)
            #     print("Card suit:", card.suit.name)
            #     # print()
            #        # Accessing the attributes of the rect object
            #     x = card.rect.x
            #     y = card.rect.y
            #     width = card.rect.width
            #     height = card.rect.height

            #                 # Determine the boundaries
            #     left = x
            #     right = x + width
            #     top = y
            #     bottom = y + height

            #                 # Print the boundaries
            #     print("Left:", left)
            #     print("Right:", right)
            #     print("Top:", top)
            #     print("Bottom:", bottom)

            self.cards2Count = len(self.cards2)         
            return  self.cards2
    
    def clearAllCards2(self):
        if self.is_cards2empty():
            return None
        self.cards2.clear()
    
    def deleteImage(self):
        if self.imageBack:
            del self.imageBack[-1]
    
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
    
    def firstDealTableau(self, deck):
        card = deck.deal()
        card.rect.x = self.x
        card.rect.y = self.y + self.spacing * len(self.cards)
        self.cards.append(card)
        super().add(card)

    def updateTableau(self):
        """Update the position of all cards in the stock."""
        for i, card in enumerate(self.cards):
            card.rect.x = self.x
            card.rect.y = self.y
            # card.rect.y = self.y + self.spacing * i

    def draw(self, surface):

        #Check if the tableau is empty
        if self.is_empty():
            pygame.draw.rect(surface, (0, 128, 0), self.rect)
            pygame.draw.rect(surface, self.rect_color, self.rect, 3)
        else:
            #Check if imageBack is empty
            if self.imageBack:
                #Check if imageBack has reduced from its initial length of z
                if len(self.imageBack) == self.z:
                    
                    #Check if card has been added to the tableau
                    if len(self.sprites()) - len(self.imageBack) > 1:
                        for image in self.imageBack:
                            surface.blit(image.cardBack, image.rect) 

                        n = len(self.sprites()) - len(self.imageBack)

                        for i in range(-n, 0):               
                            card = self.sprites()[i]
                            surface.blit(card.image, card.rect)
                    
                    elif len(self.cards) - len(self.imageBack) == 1:
                        for image in self.imageBack:
                            surface.blit(image.cardBack, image.rect) 
                         # Get the last card sprite in the tableau
                        last_card = self.sprites()[-1]

                        # Draw the last card sprite on the surface
                        surface.blit(last_card.image, last_card.rect)          
                    else:
                        for image in self.imageBack:
                            surface.blit(image.cardBack, image.rect) 

                # If imageBack has reduced from its initial length of z
                else:
                    for image in self.imageBack:
                        surface.blit(image.cardBack, image.rect) 
                    
                    # Get the difference between the cards in the tableau and imageBack i.e the cards not revealed yet
                    n = len(self.cards) - len(self.imageBack)
                    for i in range(-n, 0):               
                        card = self.sprites()[i]
                        surface.blit(card.image, card.rect)
            else:
                """Draw all the cards in the talon."""
                for card in self.sprites():
                    surface.blit(card.image, card.rect)           
    
class Foundation(pygame.sprite.Group):
    """A class to manage the foundation."""
    def __init__(self,x,y):
        super().__init__()
        self.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        self.cards = []
        self.x = x
        self.y = y
        self.rect_color = (128, 128, 128)

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

class MouseObject(pygame.sprite.Group):
    """This class is used to hold the mouse card sprite data."""
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(50, 65, CARD_WIDTH, CARD_HEIGHT)
        self.cards = []
        self.offset = 10
        self.spacing = 10

    def draggedCards(self, cards2):
        for card in cards2:
            card.rect.y = card.rect.y + self.spacing * len(self.cards)
            self.cards.append(card)

    def draggedCard(self, card):
        self.cards.append(card)

    def is_empty(self):
        return len(self.cards) == 0
    
    def clearAll(self):
        if self.is_empty():
            return None
        self.cards.clear()

    def draw(self, surface, mouse_pos):
        # """Update the position of all cards in the stock."""
        # if self.card != None:
            
        #     # Set the position of the card to the mouse position
        #     self.rect.center = mouse_pos
        #     surface.blit(self.card.image, self.rect)
        
        if not self.is_empty():
        # Code for drawing the cards at the mouse position
            for i, card in enumerate(self.cards):
                    card.rect.center = mouse_pos
                    surface.blit(card.image, card.rect)