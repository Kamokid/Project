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
    """A class to manage the tablea image."""
    def __init__(self):
        self.cardBack = pygame.image.load('images/card_back.png')
        self.rect = self.cardBack.get_rect()

class Tableau(pygame.sprite.Group):
    """A class to manage the Tableau."""
    def __init__(self,x,y,z):
        super().__init__()
        self.rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        self.cards = []
        self.x = x
        self.y = y
        self.z = z
        self.rect_color = (128, 128, 128)
        self.spacing = 10
        self.imageBack =[]
        self.populateImage()

    
    def is_empty(self):
        return len(self.cards) == 0
    
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
        self.cards.append(card)
        super().add(card)

    def addBackToTableau(self,card,x,y):
        card.rect.x = x
        card.rect.y = y
        self.cards.append(card)
        super().add(card)

    def moveTop(self):
        if self.is_empty():
            return None     
        card = self.cards.pop()
        super().remove(card)
        return card
    
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
    
    # def showCard(self):
    #     if (len(self.cards) > 0):
    #         return self.cards[-1]
    #     else:
    #          return None
    
    def firstDealTableau(self, deck):
        card = deck.deal()
        card.rect.x = self.x
        # card.rect.y = self.y
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
                    for image in self.imageBack:
                        surface.blit(image.cardBack, image.rect) 

                    #Check if card has been added to the tableau
                    if len(self.cards) - len(self.imageBack) > 1:
                        n = len(self.cards) - len(self.imageBack)

                        for i in range(-n, 0):               
                            card = self.sprites()[i]
                            surface.blit(card.image, card.rect)
                    
                    elif len(self.cards) - len(self.imageBack) == 1:
                         # Get the last card sprite in the talon
                        last_card = self.sprites()[-1]

                        # Draw the last card sprite on the surface
                        surface.blit(last_card.image, last_card.rect)
                        print("Print once")

                # If imageBack has reduced from its initial length of z
                else:
                    for image in self.imageBack:
                        surface.blit(image.cardBack, image.rect) 
                    
                    # Get the difference between the cards in the tableau and imageBack i.e the cards not revelaed yet
                    n = len(self.cards) - len(self.imageBack)
                    print(n)
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
        # card.rect.y = self.y + self.spacing * i
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

class MouseObject(pygame.sprite.Group):
    """This class is used to hold the mouse card sprite data."""
    def __init__(self):
        super().__init__()
        self.rect = pygame.Rect(0, 0, CARD_WIDTH, CARD_HEIGHT)
        self.card = None

    def changeCard(self, card):
        self.card = card

    def draw(self, surface, mouse_pos):
        """Update the position of all cards in the stock."""
        if self.card != None:
            
            # Set the position of the card to the mouse position
            self.rect.center = mouse_pos
            surface.blit(self.card.image, self.rect)