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
        # if self.deck:
        #     for card in self.deck.cards:
        #         print(card.value)
        # else:
        #     print("No more cards in deck!")
        self.deck.shuffle()

        self.stock = Stock()
        self.talon = Talon()
        self.foundation1 = Foundation(350,50)
        self.foundation2 = Foundation(450, 50)
        self.foundation3 = Foundation(550, 50)
        self.foundation4 = Foundation(650, 50)
        self.tableau1 = Tableau(50,200)
        self.tableau2 = Tableau(150,200)
        self.tableau3 = Tableau(250,200)
        self.tableau4 = Tableau(350,200)
        self.tableau5 = Tableau(450,200)
        self.tableau6 = Tableau(550,200)
        self.tableau7 = Tableau(650,200)
        self.deal()
    
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
