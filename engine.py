from enum import Enum
import pygame
from models import Deck, Stock, Talon, Foundation, Tableau, MouseObject

class GameEngine:
    """ Game engine to coordinate the interactions between the models """
    def __init__(self, solitaire):
        # These will be used to keep track of the currently picked card and the pile it came from
        self.clicked_card = None
        self.previous_pile = None
        self.stock_clicked = False # This is needed because the leftclick down is ran in multiple frames
        self.solitaire = solitaire

        # Creating the deck and shuffling it.
        self.deck = Deck()
        self.deck.shuffle() 
        # Creating the stock, talon, foundation and tableaus then dealing the cards
        self.stock = Stock()
        self.talon = Talon()
        self.foundations = []
        self.tableaus = []
        self.foundations.append(Foundation(350, 50))
        self.foundations.append(Foundation(450, 50))
        self.foundations.append(Foundation(550, 50))
        self.foundations.append(Foundation(650, 50))
        self.tableaus.append(Tableau(50,200,0))
        self.tableaus.append(Tableau(150,200,1))
        self.tableaus.append(Tableau(250,200,2))
        self.tableaus.append(Tableau(350,200,3))
        self.tableaus.append(Tableau(450,200,4))
        self.tableaus.append(Tableau(550,200,5))
        self.tableaus.append(Tableau(650,200,6))
        self.mouse_object = MouseObject()
        self.deal() 

    def RetryClicked(self):      
        self.solitaire.retry_game()
    
    def deal(self):
        # Dealing all 52 cards

        # Putting 24 cards into the stock for the player to pick from during the game.
        for i in range(24):
            self.stock.firstDealStock(self.deck)

        # Putting a total of 28 cards into the tableau following the rules of solitaire
        self.tableaus[0].firstDealTableau(self.deck)
        for i in range(2):
            self.tableaus[1].firstDealTableau(self.deck)
        for i in range(3):
            self.tableaus[2].firstDealTableau(self.deck) 
        for i in range(4):
            self.tableaus[3].firstDealTableau(self.deck)
        for i in range(5):
            self.tableaus[4].firstDealTableau(self.deck)
        for i in range(6):
            self.tableaus[5].firstDealTableau(self.deck) 
        for i in range(7):
            self.tableaus[6].firstDealTableau(self.deck)  

    def returnCardsToStock(self):
        # This is called if the stock is empty, the cards will be added back to the stock from the talon
        cards = self.talon.removeAll()
        cards.reverse()
        for card in cards:
            self.stock.addToStock(card) 
            self.stock.add(card)

    def addToTalon(self):
        # Add last card in stock to talon
        card = self.stock.popTop()
        if card:
            self.talon.addToTalon(card)
            # self.talon.add(card)
        else:
            self.returnCardsToStock()

    # This the main method to initiate the logic of the game in the engine. Its called from solitaire.py in check_events()
    def detectMouse(self, click_down, mouse_pos):
        if click_down == True:
            # Detecting if player is hovering over a TABLEAU pile while the left click is pressed.
            for tableau in self.tableaus:
                if tableau.rect.collidepoint(mouse_pos):
                    if self.clicked_card == None:
                        self.clicked_card = tableau.moveTop()
                        self.x = self.clicked_card.rect.x
                        self.y = self.clicked_card.rect.y
                        self.clicked_card.rect.center = mouse_pos 
                        self.previous_pile = tableau
                        print("Pick up the tableau card.")
                        break
            for foundation in self.foundations:
                # Hovering over a foundation deck with the left click up
                if foundation.rect.collidepoint(mouse_pos):
                    if self.clicked_card == None: 
                        print("Pick up the foundation card.")
                        self.clicked_card = foundation.moveTop()
                        self.clicked_card.rect.center = mouse_pos 
                        self.previous_pile = foundation
                        break                              
            # Player is hovering over the STOCK pile while the left click is pressed.
            if self.stock.rect.collidepoint(mouse_pos):
                if self.clicked_card == None and self.stock_clicked == False:
                     self.addToTalon()
                     self.stock_clicked = True
                     print("Move stock card to talon top of pile")
                    #  print(self.stock.popTop().value)
            # Player is hovering over the TALON pile while the left click is pressed.
            if self.talon.rect.collidepoint(mouse_pos):
                if self.clicked_card == None:
                     self.clicked_card = self.talon.moveTop()
                     self.clicked_card.rect.center = mouse_pos 
                     self.previous_pile = self.talon
                     print("Picking up a card from the talon pile")                      
        elif(click_down == False): # Left click NOT pressed 
            self.stock_clicked = False
            if(self.clicked_card != None):
                for foundation in self.foundations:
                    # Hovering over a foundation deck with the left click up
                    if foundation.rect.collidepoint(mouse_pos):
                        # if self.clicked_card != None: 
                            print("Detect if the card can be placed here.")
                            if foundation.can_add_card(self.clicked_card) == True:
                                if self.previous_pile in self.tableaus:               
                                    foundation.addToFoundation(self.clicked_card)
                                    self.previous_pile.deleteImage()
                                    self.clicked_card = None
                                else:
                                    foundation.addToFoundation(self.clicked_card)
                                    self.clicked_card = None
                            break
                for tableau in self.tableaus:
                    # Hovering over a tableau deck with the left click up
                    if tableau.rect.collidepoint(mouse_pos):
                        # if self.clicked_card != None: 
                            print("Detect if the card can be placed here.")
                            if tableau.can_add_card(self.clicked_card) == True:
                                if self.previous_pile in self.tableaus:
                                    if tableau == self.previous_pile:
                                        tableau.addToTableau(self.clicked_card)
                                        self.clicked_card = None
                                        print("Card can be placed here.")
                                    else:
                                        tableau.addToTableau(self.clicked_card)
                                        self.previous_pile.deleteImage()
                                        self.clicked_card = None
                                        print("Card can be placed here.")
                                else: 
                                    tableau.addToTableau(self.clicked_card)
                                    self.clicked_card = None
                            break
                if(self.clicked_card != None):
                    # The card was let go so it will go back to the previous pile.
                    if(self.previous_pile != None):
                        print("Sending card back to its previous pile.")
                        if self.previous_pile == self.talon:
                            self.previous_pile.addToTalon(self.clicked_card)
                        elif self.previous_pile in self.tableaus:
                            self.previous_pile.addBackToTableau(self.clicked_card, self.x, self.y)
                        else:
                            self.previous_pile.addToFoundation(self.clicked_card)
                        self.clicked_card = None
                        self.previous_pile = None     
                    else:
                        print("BUG: The card has nowhere to go back to.")
                        self.clicked_card = None
                        self.previous_pile = None 

        self.mouse_object.changeCard(self.clicked_card)