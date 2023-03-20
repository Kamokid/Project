import random
import pygame

# Define card suits and values
# C for Clubs, D for Diamonds, H for Hearts, S for Spades
suits = ['C', 'D', 'H', 'S']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']

# Initialize pygame
pygame.init()

# Define card class and sets the ranks for each card.
ranks = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

# Currently selected card
selected_card = None

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.rank = ranks[value]  # used to set the rank for each card based on its value
        self.face_up = False
        self.back = pygame.image.load('card_back.jpg')
        self.image = pygame.image.load(f'{suit}{value}.png')

    def flip(self):
        self.face_up = not self.face_up

    def draw(self, screen, pos):
        if self.face_up:
            screen.blit(self.image, pos)
        else:
            screen.blit(self.back, pos)

# Define deck class
class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for value in values:
                card = Card(suit, value)
                self.cards.append(card)
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

# Define main game loop
def play_game():
    # Initialize game
    deck = Deck()
    tableau = [[] for _ in range(7)]  # create an empty list for each tableau pile
    for i in range(7):
        for j in range(i+1):
            card = deck.draw_card()
            if j == i:
                card.flip() # flip the last card of the tableau in each pile face up
            tableau[i].append(card) # adding the card to the tableau pile
    foundation = {suit: [] for suit in suits} # create an empty dictionary for the foundation piles, one for each suit
    discard = []

    # Initialize pygame screen
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Solitaire')

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            #Mouse button was clicked
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                pos = pygame.mouse.get_pos() # Get the position of the mouse cursor
                for i in range(7):
                    # Check if the mouse click is within the tableau region of the selected column
                    if pos[0] >= i*100 + 50 and pos[0] < i*100 + 150:
                        if pos[1] >= 200 and pos[1] < 200 + len(tableau[i])*30:
                            # Select the top card from the tableau of the selected column
                            if selected_card == None:
                                selected_card = tableau[i][-1] # Setting the selected_card if one isn't already selected
                                if not selected_card.face_up:
                                    selected_card.flip() # If card is not flipped, it will flip the card upright
                                    selected_card = None # The selected_card is set to none because the user flipped the card upright and isn't moving the card.
                                break # Breaking out of the loop because either the card is flipped or the player clicked on an upright card to select for a move in the next click
                            elif selected_card != tableau[i][-1] and selected_card.rank == tableau[i][-1].rank - 1: 
                                # The new card clicked is not the same as the card saved in the selected_card from before AND the selected_card rank is lower by 1 (Adding the selected card to the other tableau pile)
                                tableau[i][-1].append(selected_card)
                                tableau[i].pop()
                                if tableau[i]:
                                    tableau[i][-1].flip()
                                selected_card = None # The selected card is set to none because it was added to the other tableau deck
                                break
                            else:
                                #Either the user clicked on the same card again or the rank of the card wasn't 1 lower. 
                                selected_card = None 
                        elif pos[1] >= 300 and pos[1] < 330:
                            # Check if the mouse click is within the foundation region
                            if selected_card != None: # Checking if the selected_card was picked before
                                if selected_card.face_up:
                                    # Check if the selected card can be placed on any foundation pile
                                    for suit in suits:
                                        if foundation[suit] and selected_card.suit == suit and selected_card.rank == foundation[suit][-1].rank + 1:
                                            foundation[suit].append(selected_card)
                                            tableau[i].pop()
                                            if tableau[i]:
                                                tableau[i][-1].flip()
                                            break
                                    else:
                                        # If the selected card is an Ace, move it to the empty foundation pile
                                        for suit in suits:
                                            if not foundation[suit] and selected_card.rank == 1:
                                                foundation[suit].append(selected_card)
                                                tableau[i].pop()
                                                if tableau[i]:
                                                    tableau[i][-1].flip()
                                                break
                                selected_card = None # No matter what the selected car is set to none at the end because the user clicked off of the tableau deck
                            else:
                            # The user clicked within the foundation region but has no cards selected so it's breaking out of the for loop.
                                break
                # Check if the mouse click is within the discard pile region
                else:
                    if pos[0] >= 0 and pos[0] < 100:
                        if pos[1] >= 400 and pos[1] < 430:
                            if discard:
                                discard[-1].flip()
             # Draw background
                screen.fill((0, 128, 0))

                # Draw tableau
                for i in range(7):
                    for j, card in enumerate(tableau[i]):
                        card.draw(screen, (i*100 + 50, 200 + j*30))

                # Draw foundation
                for i, suit in enumerate(suits):
                    if foundation[suit]:
                        foundation[suit][-1].draw(screen, (i*100 + 50, 50))

                # Draw discard
                if discard:
                    discard[-1].draw(screen, (0, 400))

                # Update screen
                pygame.display.flip()

# Run game
play_game()

