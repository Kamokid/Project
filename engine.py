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
                    
                    #Check if the mouse is holding a card
                    if not self.filtered_card_list and self.clicked_card is None:
                        
                        self.previous_pile = tableau

                        #Return a list of the cards that are visible in a particular array
                        self.clicked_cards = tableau.moveAdded()
                        
                        #Check if only one card was returned from the tableau
                        if(len(self.clicked_cards) == 1):

                            #Append that card to the local list that will then be passed on to the cursor
                            self.filtered_card_list.append(self.clicked_cards[0])
                        #Check if more than one card was returned from the tableau                                      
                        elif(len(self.clicked_cards) > 1):
                            for i, card in enumerate(self.clicked_cards):
                                if i == 0:
                                    #Capture the Y position of the first card
                                    first_rect_y = card.rect.y
                                #Check if the Y position of this card collides with the  mouse    
                                if mouse_pos[1] >= first_rect_y and mouse_pos[1] < (first_rect_y + 15):

                                    #Add the card that collides with the mouse as well as all cards after it to the local list of cards
                                    self.filtered_card_list.extend(self.clicked_cards[i:])

                                    #Clear the array that was holding all the cards returned from the tableau
                                    self.clicked_cards.clear()
                                    break
                                
                                #Check if this is the last card and it was clicked without onlya lower bound for the y-position
                                if self.clicked_cards[i] == self.clicked_cards[-1] and  mouse_pos[1] >= first_rect_y:

                                    #Append only the last card in the tableau tp the local list of cards
                                    self.filtered_card_list.append(self.clicked_cards[i])

                                    #Clear the array that was holding all the cards returned from the tableau
                                    self.clicked_cards.clear()
                                    break

                                #Return the card that didnt collide with the mouse point to its previous tableau
                                tableau.addBackToTableau(self.clicked_cards[i])

                                #Increment the y-position to be used in the collide condition
                                first_rect_y += 15

                        # for card in self.filtered_card_list:
                        #     self.cardloc.append((card.rect.x, card.rect.y))
                        #     print("/////////")
                        #     print("Before moving")
                        #     print("Card value:", card.value)
                        #     print("Card suit:", card.suit.name)
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

            # Player is hovering over the TALON pile while the left click is pressed.
            if self.talon.rect.collidepoint(mouse_pos):
                if not self.filtered_card_list and self.clicked_card is None:
                     self.clicked_card = self.talon.moveTop()
                     self.clicked_card.rect.center = mouse_pos 
                     self.previous_pile = self.talon
                     print("Picking up a card from the talon pile")    

        elif(click_down == False): # Left click no longer being pressed 
            self.stock_clicked = False

            #Check if the mouse is holding a card. The card is either from a talon or a foundation
            if(self.clicked_card is not None):
                for foundation in self.foundations:
                    # Hovering over a foundation deck with the left click up
                    if foundation.rect.collidepoint(mouse_pos):
                            print("Detect if the card can be placed in foundation.")
                            if foundation.can_add_card(self.clicked_card) == True:
                                    foundation.addToFoundation(self.clicked_card)
                                    self.reset()
                            break
                    
                for tableau in self.tableaus:
                    # Hovering over a tableau deck with the left click up
                    if tableau.rect.collidepoint(mouse_pos):
                            print("Detect if the card can be placed in tableau.")
                            if tableau.can_add_card(self.clicked_card) == True:
                                    tableau.addToTableau(self.clicked_card)
                                    self.reset()
                            break        
            
            #Check if the mouse is holding a card or cards. The card(s) is/are from a tableau
            elif(self.filtered_card_list):
                for foundation in self.foundations:
                    # Hovering over a foundation deck with the left click up
                    if foundation.rect.collidepoint(mouse_pos):
                        # if self.clicked_card != None: 
                            print("Detect if the card can be placed here.")
                            if len(self.filtered_card_list) == 1:  
                                if foundation.can_add_card(self.filtered_card_list[0]) == True:
                                    foundation.addToFoundation(self.filtered_card_list[0])
                                # self.previous_pile.remainingCardsBackToTableau()
                                    self.reset()
                                    self.previous_pile.deleteImage()
                                    self.previous_pile.clearAllCards2()
                                    self.previous_pile = None
                            break
                for tableau in self.tableaus:
                    # Hovering over a tableau deck with the left click up
                    if tableau.rect.collidepoint(mouse_pos):
                            print("Detect if the card can be placed here.")
                            if not tableau == self.previous_pile:                       
                                if tableau.can_add_card(self.filtered_card_list[0]) == True:
                                    for card in self.filtered_card_list: 
                                        tableau.addToTableau(card)
                                    self.reset()
                                    
                                    #Delete an image in the tableau
                                    self.previous_pile.deleteImage()

                                    #Clear the list in tableau that holds the cards returned from tableau
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
                            
                            self.resetXY()

                            # print("/////////")
                            # print("Card Back to tableau")
                            # for card in self.filtered_card_list:

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
    
                            for card in self.filtered_card_list: 
                                self.previous_pile.addBackToTableau(card)
                            self.previous_pile.clearAllCards2()
                            self.reset()

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
        self.clicked_card = None
        self.cardloc.clear()