from enum import Enum
import pygame
import copy
from models import Deck, Stock, Talon, Foundation, Tableau, MouseObject

class GameEngine:
    """ Game engine to coordinate the interactions between the models """
    def __init__(self, solitaire):
        # These will be used to keep track of the currently picked card and the pile it came from
        self.clicked_card = None
        self.clicked_cards = []
        self.cardloc = []
        self.previous_pile = None
        self.stock_clicked = False # This is needed because the leftclick down is ran in multiple frames
        self.filtered_card_list = []  # List to store the collided rect and rects following it
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
           
        else:
            self.returnCardsToStock()

    # This the main method to initiate the logic of the game in the engine. Its called from solitaire.py in check_events()
    def detectMouse(self, click_down, mouse_pos):
        if click_down == True:
            # Detecting if player is hovering over a TABLEAU pile while the left click is pressed.
            for tableau in self.tableaus:
                if tableau.rect.collidepoint(mouse_pos):

                    if not self.clicked_cards and self.clicked_card is None:
                        print(not self.clicked_cards and self.clicked_card is None)
                        # for card in tableau:
                        self.previous_pile = tableau
                        self.clicked_cards = tableau.moveAdded()
                        for card in self.clicked_cards:
                            self.cardloc.append((card.rect.x, card.rect.y))
                            print("/////////")
                            print("Before moving")
                            print("Card value:", card.value)
                            print("Card suit:", card.suit.name)
                            # Accessing the attributes of the rect object
                            x = card.rect.x
                            y = card.rect.y
                            width = card.rect.width
                            height = card.rect.height

                                        # Determine the boundaries
                            left = x
                            right = x + width
                            top = y
                            bottom = y + height

                                        # Print the boundaries
                            print("Left:", left)
                            print("Right:", right)
                            print("Top:", top)
                            print("Bottom:", bottom)
                        # self.clicked_cardsholder = copy.deepcopy(self.clicked_cards)
                        if(len(self.clicked_cards) == 1):
                            self.filtered_card_list.append(self.clicked_cards[0])                                  
                        elif(len(self.clicked_cards) > 1):
                            # collision_occurred = False  # Flag to check if collision occurred
                            # Iterate over the rects and check for collision
                            for card in self.clicked_cards:
                                # if card.rect.collidepoint(mouse_pos):
                                #     collision_occurred = True  # Collision occurred with the current rect
                                # if collision_occurred:
                                    self.filtered_card_list.append(card)                         
                            # self.clicked_card = tableau.moveTop()
                            # self.x = self.clicked_card.rect.x
                            # self.y = self.clicked_card.rect.y
                            # self.clicked_card.rect.center = mouse_pos 
                            
                            print("Pick up the tableau card.")
                    break
            for foundation in self.foundations:
                # Hovering over a foundation deck with the left click is pressed
                if foundation.rect.collidepoint(mouse_pos):
                    if not self.filtered_card_list and self.clicked_card is None:
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
                if not self.filtered_card_list and self.clicked_card is None:
                     self.clicked_card = self.talon.moveTop()
                     self.clicked_card.rect.center = mouse_pos 
                     self.previous_pile = self.talon
                     print("Picking up a card from the talon pile")                      
        elif(click_down == False): # Left click NOT pressed 
            self.stock_clicked = False
            if(self.clicked_card is not None):
                for foundation in self.foundations:
                    # Hovering over a foundation deck with the left click up
                    if foundation.rect.collidepoint(mouse_pos):
                            print("Detect if the card can be placed here.")
                            if foundation.can_add_card(self.clicked_card) == True:
                                    foundation.addToFoundation(self.clicked_card)
                                    self.mouse_object.clearAll()
                                    self.clicked_card = None
                            break
                for tableau in self.tableaus:
                    # Hovering over a tableau deck with the left click up
                    if tableau.rect.collidepoint(mouse_pos):
                            print("Detect if the card can be placed here.")
                            if tableau.can_add_card(self.clicked_card) == True:
                                    tableau.addToTableau(self.clicked_card)
                                    self.mouse_object.clearAll()
                                    self.clicked_card = None
                            break        
            elif(self.filtered_card_list):
                for foundation in self.foundations:
                    # Hovering over a foundation deck with the left click up
                    if foundation.rect.collidepoint(mouse_pos):
                        # if self.clicked_card != None: 
                            print("Detect if the card can be placed here.")
                            if foundation.can_add_card(self.filtered_card_list[-1]) == True:
                                # for card in self.filtered_card_list: 
                                self.resetXY()
                                foundation.addToFoundation(self.filtered_card_list[-1])
                                self.previous_pile.remainingCardsBackToTableau()
                                self.reset()
                                self.previous_pile.clearAllCards2()
                                self.previous_pile = None
                            break
                for tableau in self.tableaus:
                    # Hovering over a tableau deck with the left click up
                    if tableau.rect.collidepoint(mouse_pos):
                        
                            print("Detect if the card can be placed here.")
                            if tableau.can_add_card(self.filtered_card_list[0]) == True:
                                    # if tableau == self.previous_pile:
                                    #     tableau.addToTableau(self.clicked_card)
                                    #     self.mouse_object.clearAll()
                                    #     self.clicked_card = None
                                    #     print("Card can be placed here.")
                                    # else:
                                for card in self.filtered_card_list: 
                                    tableau.addToTableau(card)
                                self.reset()
                                self.previous_pile.deleteImage()
                                self.previous_pile.clearAllCards2()
                                self.previous_pile = None
                                print("Card can be placed here.")
                            break
            if(self.clicked_card is not None or self.filtered_card_list):
                    # The card was let go so it will go back to the previous pile.
                    print("card not null")
                    if(self.previous_pile is not None):
                        print("Sending card back to its previous pile.")
                        if self.previous_pile == self.talon:
                            self.previous_pile.addToTalon(self.clicked_card)
                            self.mouse_object.clearAll()
                        elif self.previous_pile in self.tableaus:
                            print("/////////")
                            print("Card Back to tableau")
                            self.resetXY()

                            for card in self.previous_pile.cards2:

                                print("Card value:", card.value)
                                print("Card suit:", card.suit.name)
                                # print()
                                # Accessing the attributes of the rect object
                                x = card.rect.x
                                y = card.rect.y
                                width = card.rect.width
                                height = card.rect.height

                                            # Determine the boundaries
                                left = x
                                right = x + width
                                top = y
                                bottom = y + height

                                            # Print the boundaries
                                print("Left:", left)
                                print("Right:", right)
                                print("Top:", top)
                                print("Bottom:", bottom)
    
                            self.previous_pile.addBackToTableau()
                            self.reset()
                            print("done")
                        else:
                            self.previous_pile.addToFoundation(self.clicked_card)
                            self.mouse_object.clearAll()
                        self.clicked_card = None
                        self.previous_pile = None     
                    else:
                        print("BUG: The card has nowhere to go back to.")
                        self.clicked_card = None
                        self.previous_pile = None 
        
        if (self.clicked_card != None):
            self.mouse_object.draggedCard(self.clicked_card)
        elif (self.filtered_card_list):
            self.mouse_object.draggedCards(self.filtered_card_list)
    
    def resetXY(self):
        for card, position in zip(self.filtered_card_list, self.cardloc):
                                 card.rect.x, card.rect.y = position
    
    def reset(self):
        print("done")
        self.mouse_object.clearAll()
        self.filtered_card_list.clear()
        self.clicked_cards.clear()
        self.cardloc.clear()

                            # for card in self.previous_pile.cards2:

                            #     print("Card value:", card.value)
                            #     print("Card suit:", card.suit.name)
                            #     # print()
                            #     # Accessing the attributes of the rect object
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
                            
                            