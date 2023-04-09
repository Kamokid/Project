from enum import Enum
import pygame
from models import *

class GameEngine:
    """ Game engine to coordinate the interactions between the models """
    def __init__(self):
        # """ Initialize GameEngine settings """
        # self.all_sprites = pygame.sprite.Group()
        # self.deck_sprites = pygame.sprite.Group()
        # self.stock_sprites = pygame.sprite.Group()
        # self.talon_sprites = pygame.sprite.Group()
        # self.foundation_sprites = pygame.sprite.Group()
        # self.tableau_sprites = pygame.sprite.Group()

        """ Initialize GameEngine settings """
        self.deck = Deck()
        if self.deck:
            for card in self.deck.cards:
                print(card.value)
        else:
            print("No more cards in deck!")
        self.deck.shuffle()

        # for card in self.deck.cards:
        #     card_sprite = Card(card.suit, card.value)
        #     self.all_sprites.add(card_sprite)
        #     self.deck_sprites.add(card_sprite)

        self.stock = Stock()
        self.talon = Talon()
        self.foundation1 = Foundation(420,50)
        self.foundation2 = Foundation(494, 50)
        self.foundation3 = Foundation(568, 50)
        self.foundation4 = Foundation(642, 50)
        self.tableau1 = Tableau(50,200)
        self.tableau2 = Tableau(150,200)
        self.tableau3 = Tableau(250,200)
        self.tableau4 = Tableau(350,200)
        self.tableau5 = Tableau(450,200)
        self.tableau6 = Tableau(550,200)
        self.tableau7 = Tableau(650,200)
        self.deal()
        
        # self.all_sprites.add(self.stock, self.talon, self.foundation1, self.foundation2, 
        #                      self.foundation3, self.foundation4, self.tableau1, self.tableau2, 
        #                      self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7)
        
        # self.stock_sprites.add(self.stock)
        # self.talon_sprites.add(self.talon)
        # self.foundation_sprites.add(self.foundation1, self.foundation2, self.foundation3, self.foundation4)
        # self.tableau_sprites.add(self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, 
        #                          self.tableau6, self.tableau7)

        
    
    def deal(self):
        # initial = self.deck.length()
        for i in range(24):
            self.stock.firstDealStock(self.deck)
        
        self.tableau1.firstDealTableau(self.deck)
        
        for i in range(2):
            self.tableau2.firstDealTableau(self.deck)
        for i in range(3):
            self.tableau3.firstDealTableau(self.deck) 
        for i in range(4):
            self.tableau4.firstDealTableau(self.deck)
        for i in range(5):
            self.tableau5.firstDealTableau(self.deck)
        for i in range(6):
            self.tableau6.firstDealTableau(self.deck) 
        for i in range(7):
            self.tableau7.firstDealTableau(self.deck)  

    # def update(self):
    #     self.all_sprites.update()
    #     self.stock_sprites.update()
    #     self.talon_sprites.update()
    #     self.foundation_sprites.update()
    #     self.tableau_sprites.update()
    
    def addToTableau(self, click):
        # Check if the top card of the talon can be added to tableau1
        if self.talon[-1].color != self.tableau1[-1].color:
            if self.talon[-1].value - self.tableau1[-1].value == -1:
                self.tableau1.add(self.talon.moveTop())
    
        # Check if the top card of any tableau pile can be added to tableau1
        for tableau in [self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
            if tableau[-1].color != self.tableau1[-1].color:
                if tableau[-1].value - self.tableau1[-1].value == -1:
                    self.tableau1.add(tableau.moveTop())
    
        # Check if the top card of any foundation pile can be added to tableau1
        for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
            if foundation[-1].color != self.tableau1[-1].color:
              if foundation[-1].value - self.tableau1[-1].value == -1:
                    self.tableau1.add(foundation.moveTop())

        # Check if the top card of the talon can be added to tableau2
        if self.talon[-1].color != self.tableau2[-1].color:
            if self.talon[-1].value - self.tableau2[-1].value == -1:
                self.tableau2.add(self.talon.moveTop())
    
        # Check if the top card of any tableau pile can be added to tableau2
        for tableau in [self.tableau1, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
            if tableau[-1].color != self.tableau2[-1].color:
                if tableau[-1].value - self.tableau2[-1].value == -1:
                    self.tableau2.add(tableau.moveTop())
    
         # Check if the top card of any foundation pile can be added to tableau2
        for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
            if foundation[-1].color != self.tableau2[-1].color:
                if foundation[-1].value - self.tableau2[-1].value == -1:
                    self.tableau2.add(foundation.moveTop())
        
        # Check if the top card of the talon can be added to tableau3
        if self.talon[-1].color != self.tableau3[-1].color:
            if self.talon[-1].value - self.tableau3[-1].value == -1:
                self.tableau3.add(self.talon.moveTop())
    
        # Check if the top card of any tableau pile can be added to tableau3
        for tableau in [self.tableau1, self.tableau2, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
            if tableau[-1].color != self.tableau3[-1].color:
                if tableau[-1].value - self.tableau3[-1].value == -1:
                    self.tableau3.add(tableau.moveTop())
    
         # Check if the top card of any foundation pile can be added to tableau3
        for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
            if foundation[-1].color != self.tableau3[-1].color:
                if foundation[-1].value - self.tableau3[-1].value == -1:
                    self.tableau3.add(foundation.moveTop())
        
        # Check if the top card of the talon can be added to tableau4
        if self.talon[-1].color != self.tableau4[-1].color:
            if self.talon[-1].value - self.tableau4[-1].value == -1:
                self.tableau4.add(self.talon.moveTop())
    
        # Check if the top card of any tableau pile can be added to tableau4
        for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau5, self.tableau6, self.tableau7]:
            if tableau[-1].color != self.tableau4[-1].color:
                if tableau[-1].value - self.tableau4[-1].value == -1:
                    self.tableau4.add(tableau.moveTop())
    
         # Check if the top card of any foundation pile can be added to tableau4
        for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
            if foundation[-1].color != self.tableau4[-1].color:
                if foundation[-1].value - self.tableau4[-1].value == -1:
                     self.tableau4.add(foundation.moveTop())

        # Check if the top card of the talon can be added to tableau5
        if self.talon[-1].color != self.tableau5[-1].color:
            if self.talon[-1].value - self.tableau5[-1].value == -1:
                self.tableau5.add(self.talon.moveTop())
    
        # Check if the top card of any tableau pile can be added to tableau5
        for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau6, self.tableau7]:
            if tableau[-1].color != self.tableau5[-1].color:
                if tableau[-1].value - self.tableau5[-1].value == -1:
                    self.tableau5.add(tableau.moveTop())
    
         # Check if the top card of any foundation pile can be added to tableau5
        for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
            if foundation[-1].color != self.tableau5[-1].color:
                if foundation[-1].value - self.tableau5[-1].value == -1:
                    self.tableau5.add(foundation.moveTop())

        # Check if the top card of the talon can be added to tableau6
        if self.talon[-1].color != self.tableau6[-1].color:
            if self.talon[-1].value - self.tableau6[-1].value == -1:
                self.tableau6.add(self.talon.moveTop())
    
        # Check if the top card of any tableau pile can be added to tableau6
        for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau7]:
            if tableau[-1].color != self.tableau6[-1].color:
                if tableau[-1].value - self.tableau6[-1].value == -1:
                     self.tableau6.add(tableau.moveTop())
    
         # Check if the top card of any foundation pile can be added to tableau6
        for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
            if foundation[-1].color != self.tableau6[-1].color:
                if foundation[-1].value - self.tableau6[-1].value == -1:
                    self.tableau6.add(foundation.moveTop())
          
        # Check if the top card of the talon can be added to tableau7
        if self.talon[-1].color != self.tableau7[-1].color:
            if self.talon[-1].value - self.tableau7[-1].value == -1:
                self.tableau7.add(self.talon.moveTop())
    
        # Check if the top card of any tableau pile can be added to tableau7
        for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6]:
            if tableau[-1].color != self.tableau7[-1].color:
                if tableau[-1].value - self.tableau7[-1].value == -1:
                    self.tableau7.add(tableau.moveTop())
    
         # Check if the top card of any foundation pile can be added to tableau7
        for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
            if foundation[-1].color != self.tableau7[-1].color:
                if foundation[-1].value - self.tableau7[-1].value == -1:
                    self.tableau7.add(foundation.moveTop())

    def addToEmptyTableau(self, click):
        
        # Check if the tableau1 is empty
        if not self.tableau1:
            # Check if the top card of the talon is a King and can be added to tableau1
            if self.talon[-1].value == 13:
               self.tableau1.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is a King and can be added to tableau1
            for tableau in [self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                if tableau[-1].value == 13:
                  self.tableau1.add(tableau.moveTop())

            # Check if the top card of any foundation pile is a king and can be added to tableau1
            for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
              if foundation[-1].value == 13:
                 self.tableau1.add(foundation.moveTop())
      
        # Check if the tableau2 is empty
        if not self.tableau2:
            # Check if the top card of the talon is a King and can be added to tableau2
            if self.talon[-1].value == 13:
               self.tableau2.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is a King and can be added to tableau2
            for tableau in [self.tableau1, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                if tableau[-1].value == 13:
                  self.tableau2.add(tableau.moveTop())

            # Check if the top card of any foundation pile is a king and can be added to tableau2
            for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
              if foundation[-1].value == 13:
                 self.tableau2.add(foundation.moveTop())

        # Check if the tableau3 is empty
        if not self.tableau3:
            # Check if the top card of the talon is a King and can be added to tableau3
            if self.talon[-1].value == 13:
               self.tableau3.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is a King and can be added to tableau3
            for tableau in [self.tableau1, self.tableau2, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                if tableau[-1].value == 13:
                  self.tableau3.add(tableau.moveTop())

            # Check if the top card of any foundation pile is a king and can be added to tableau3
            for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
              if foundation[-1].value == 13:
                 self.tableau3.add(foundation.moveTop())
          
        # Check if the tableau4 is empty
        if not self.tableau4:
            # Check if the top card of the talon is a King and can be added to tableau4
            if self.talon[-1].value == 13:
               self.tableau4.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is a King and can be added to tableau4
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau5, self.tableau6, self.tableau7]:
                if tableau[-1].value == 13:
                  self.tableau4.add(tableau.moveTop())

            # Check if the top card of any foundation pile is a king and can be added to tableau4
            for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
              if foundation[-1].value == 13:
                 self.tableau4.add(foundation.moveTop())

        # Check if the tableau5 is empty
        if not self.tableau5:
            # Check if the top card of the talon is a King and can be added to tableau5
            if self.talon[-1].value == 13:
               self.tableau5.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is a King and can be added to tableau5
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau6, self.tableau7]:
                if tableau[-1].value == 13:
                  self.tableau5.add(tableau.moveTop())

            # Check if the top card of any foundation pile is a king and can be added to tableau5
            for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
              if foundation[-1].value == 13:
                 self.tableau5.add(foundation.moveTop())

        # Check if the tableau6 is empty
        if not self.tableau6:
            # Check if the top card of the talon is a King and can be added to tableau6
            if self.talon[-1].value == 13:
               self.tableau6.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is a King and can be added to tableau6
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau7]:
                if tableau[-1].value == 13:
                  self.tableau6.add(tableau.moveTop())

            # Check if the top card of any foundation pile is a king and can be added to tableau6
            for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
              if foundation[-1].value == 13:
                 self.tableau6.add(foundation.moveTop())

        # Check if the tableau1 is empty
        if not self.tableau7:
            # Check if the top card of the talon is a King and can be added to tableau7
            if self.talon[-1].value == 13:
               self.tableau7.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is a King and can be added to tableau7
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6]:
                if tableau[-1].value == 13:
                  self.tableau7.add(tableau.moveTop())

            # Check if the top card of any foundation pile is a king and can be added to tableau7
            for foundation in [self.foundation1, self.foundation2, self. foundation3, self.foundation4]:
              if foundation[-1].value == 13:
                 self.tableau7.add(foundation.moveTop())

    def addToEmptyFoundation(self, click):
        
        # Check if the foundation1 is empty
        if not self.foundation1:
            # Check if the top card of the talon is an Ace and can be added to foundation1
            if self.talon[-1].value == 1:
               self.foundation1.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is an Ace and can be added to foundation1
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                if tableau[-1].value == 1:
                  self.foundation1.add(tableau.moveTop())

            # Check if the top card of any foundation pile is an Ace and and can be added to foundation1
            for foundation in [self.foundation2, self. foundation3, self.foundation4]:
              if foundation[-1].value == 1:
                 self.foundation1.add(foundation.moveTop())

        # Check if the foundation2 is empty
        if not self.foundation2:
            # Check if the top card of the talon is an Ace
            if self.talon[-1].value == 1:
               self.foundation2.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is an Ace
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                if tableau[-1].value == 1:
                  self.foundation2.add(tableau.moveTop())

            # Check if the top card of any foundation pile is an Ace
            for foundation in [self.foundation1, self. foundation3, self.foundation4]:
              if foundation[-1].value == 1:
                 self.foundation2.add(foundation.moveTop())

        # Check if the foundation3 is empty
        if not self.foundation3:
            # Check if the top card of the talon is an Ace
            if self.talon[-1].value == 1:
               self.foundation3.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is an Ace
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                if tableau[-1].value == 1:
                  self.foundation3.add(tableau.moveTop())

            # Check if the top card of any foundation pile is an Ace
            for foundation in [self.foundation1, self.foundation2, self.foundation4]:
              if foundation[-1].value == 1:
                 self.foundation3.add(foundation.moveTop())
        
        # Check if the foundation4 is empty
        if not self.foundation4:
            # Check if the top card of the talon is an Ace
            if self.talon[-1].value == 1:
               self.foundation4.add(self.talon.moveTop())
              
            # Check if the top card of any tableau pile is an Ace
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                if tableau[-1].value == 1:
                  self.foundation4.add(tableau.moveTop())

            # Check if the top card of any foundation pile is an Ace
            for foundation in [self.foundation1, self.foundation2, self. foundation3]:
              if foundation[-1].value == 1:
                 self.foundation4.add(foundation.moveTop())

    def addToFoundation(self, click):

        # Check if the foundation1 is empty
        if self.foundation1:
            # Check if the top card of the talon has the same suit as foundation
            if self.talon[-1].suit.name == self.foundation1[-1].suit.name:
               # Check if the top card of the talon is greater than the last card in the foundation by 1
               if self.talon[-1].value - self.foundation1[-1].value == 1:
                    self.foundation1.add(self.talon.moveTop())
              
            
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                # Check if the top card of the tableau has the same suit as a foundation
                if tableau[-1].suit.name == self.foundation1[-1].suit.name:
                    # Check if the tableau card is greater than the last card in the foundation by 1
                    if tableau[-1].value - self.foundation1[-1].value == 1:  
                        self.foundation1.add(tableau.moveTop())

        # Check if the foundation2 is empty
        if self.foundation2:
            # Check if the top card of the talon has the same suit as foundation
            if self.talon[-1].suit.name == self.foundation2[-1].suit.name:
               # Check if the top card of the talon is greater than the last card in the foundation by 1
               if self.talon[-1].value - self.foundation2[-1].value == 1:
                    self.foundation2.add(self.talon.moveTop())
              
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                # Check if the top card of the tableau has the same suit as a foundation
                if tableau[-1].suit.name == self.foundation2[-1].suit.name:
                    # Check if the tableau card is greater than the last card in the foundation by 1
                    if tableau[-1].value - self.foundation2[-1].value == 1:  
                        self.foundation2.add(tableau.moveTop())

            # Check if the top card of any foundation pile is an Ace
            for foundation in [self.foundation1, self. foundation3, self.foundation4]:
              if foundation[-1].value == 1:
                 self.foundation2.add(foundation.moveTop())

        # Check if the foundation3 is empty
        if self.foundation3:
            # Check if the top card of the talon has the same suit as foundation
            if self.talon[-1].suit.name == self.foundation3[-1].suit.name:
               # Check if the top card of the talon is greater than the last card in the foundation by 1
               if self.talon[-1].value - self.foundation3[-1].value == 1:
                    self.foundation3.add(self.talon.moveTop())
              
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                # Check if the top card of the tableau has the same suit as a foundation
                if tableau[-1].suit.name == self.foundation3[-1].suit.name:
                    # Check if the tableau card is greater than the last card in the foundation by 1
                    if tableau[-1].value - self.foundation3[-1].value == 1:  
                        self.foundation3.add(tableau.moveTop())
        
        # Check if the foundation4 is empty
        if self.foundation4:
            # Check if the top card of the talon has the same suit as foundation
            if self.talon[-1].suit.name == self.foundation4[-1].suit.name:
               # Check if the top card of the talon is greater than the last card in the foundation by 1
               if self.talon[-1].value - self.foundation4[-1].value == 1:
                    self.foundation4.add(self.talon.moveTop())
              
            for tableau in [self.tableau1, self.tableau2, self.tableau3, self.tableau4, self.tableau5, self.tableau6, self.tableau7]:
                # Check if the top card of the tableau has the same suit as a foundation
                if tableau[-1].suit.name == self.foundation4[-1].suit.name:
                    # Check if the tableau card is greater than the last card in the foundation by 1
                    if tableau[-1].value - self.foundation4[-1].value == 1:  
                        self.foundation4.add(tableau.moveTop())

    def returnCardsToStock(self):
        # Check if the stock is empty
        cards = self.talon.removeAll()
        # if cards:
        #     for card in cards:
        #         print(card.value)
        # else:
        #     print("No more cards in deck!")
        cards.reverse()
        for card in cards:
            self.stock.addToStock(card) 
            self.stock.add(card)

    def addToTalon(self):
        # Add last card in stock to talon
        card = self.stock.popTop()
        if card:
            self.talon.addToTalon(card)
            self.talon.add(card)
        else:
            self.returnCardsToStock()
