import sys, pygame
from settings import Settings
from models import Card, Suits
from engine import GameEngine

class Solitaire:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
      
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Solitaire")

        self.clock = pygame.time.Clock()
        self.gameEngine = GameEngine()

        font = pygame.font.SysFont('comicsans',60, True)  # Create a Pygame font object
        self.text_surface = font.render("Hello", True, (0, 0, 0))  # Render the text to a surface

        # self.card = Card(self, "Club", "2")
        # self.card = Card(Suits.CLUB, 2)
        # self.card.image = pygame.transform.scale(self.card.image, (74, 103))

        # Define the rectangle's size and color
        self.rect_width = 74
        self.rect_height = 103
        self.rect_color = (128, 128, 128)  # Gray

        # # # Create a pygame.Rect object representing the rectangle
        # self.rect = pygame.Rect(0, 0, self.rect_width, self.rect_height)
        # self.rect.top = 50
        # self.rect.right = 420  # Adjust the x-coordinate as desired

        # # # Create a pygame.Rect object representing the rectangle
        # self.rect1 = pygame.Rect(0, 0, self.rect_width, self.rect_height)
        # self.rect1.top = 50
        # self.rect1.left = self.rect.right + 25  # Adjust the x-coordinate as desired

        # # # Create a pygame.Rect object representing the rectangle
        # self.rect2 = pygame.Rect(0, 0, self.rect_width, self.rect_height)
        # self.rect2.top = 50
        # self.rect2.left = self.rect1.right + 25  # Adjust the x-coordinate as desired

        # # # Create a pygame.Rect object representing the rectangle
        # self.rect3 = pygame.Rect(0, 0, self.rect_width, self.rect_height)
        # self.rect3.top = 50
        # self.rect3.left = self.rect2.right + 25  # Adjust the x-coordinate as desired

  
    def run_game(self):
    # Start the main loop for the game.
        while True:

            self._check_events()
            self._update_screen()
           
        # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(222)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # mouse_click = False

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                # if event.type == pygame.MOUSEBUTTONDOWN:
                #     pressed_keys = pygame.mouse.get_pressed()
                #     if (pressed_keys[0]):
                #         print("Left key is being pressed")
                #     if (pressed_keys[2]):
                #         print("Right key is being pressed")

             
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        # self.screen.blit(self.cardBack, (50, 50))
        # self.screen.blit(self.card.image, (146, 50))

        if self.gameEngine.stock.draw(self.screen):
            self.gameEngine.addToTalon()
        self.gameEngine.foundation1.draw(self.screen)
        self.gameEngine.foundation2.draw(self.screen)
        self.gameEngine.foundation3.draw(self.screen)
        self.gameEngine.foundation4.draw(self.screen)
        if self.gameEngine.talon.draw(self.screen):
            card = self.gameEngine.talon.draw(self.screen)
            self._add_foundation(card)
            
        # self.gameEngine.talon.updateTalon()

        
        # # Draw a filled rectangle with the background color
        # pygame.draw.rect(self.screen, self.settings.bg_color, self.rect)
        # pygame.draw.rect(self.screen, self.settings.bg_color, self.rect1)
        # pygame.draw.rect(self.screen, self.settings.bg_color, self.rect2)
        # pygame.draw.rect(self.screen, self.settings.bg_color, self.rect3)


        # # Draw a rectangle with a black boundary on top of the filled rectangle
        # pygame.draw.rect(self.screen, self.rect_color, self.rect, 3)
        # pygame.draw.rect(self.screen, self.rect_color, self.rect1, 3)
        # pygame.draw.rect(self.screen, self.rect_color, self.rect2, 3)
        # pygame.draw.rect(self.screen, self.rect_color, self.rect3, 3)




        tableauCard1 = self.gameEngine.tableau1.showCard()
        self.screen.blit(pygame.transform.scale(tableauCard1.image, (74, 103)), (50,200))

        tableauCard2 = self.gameEngine.tableau2.showCard()
        self.screen.blit(pygame.transform.scale(tableauCard2.image, (74, 103)), (150,200))

        tableauCard3 = self.gameEngine.tableau3.showCard()
        self.screen.blit(pygame.transform.scale(tableauCard3.image, (74, 103)), (250,200))

        tableauCard4 = self.gameEngine.tableau4.showCard()
        self.screen.blit(pygame.transform.scale(tableauCard4.image, (74, 103)), (350,200))

        tableauCard5 = self.gameEngine.tableau5.showCard()
        self.screen.blit(pygame.transform.scale(tableauCard5.image, (74, 103)), (450,200))

        tableauCard6 = self.gameEngine.tableau6.showCard()
        self.screen.blit(pygame.transform.scale(tableauCard6.image, (74, 103)), (550,200))

        tableauCard7 = self.gameEngine.tableau7.showCard()
        self.screen.blit(pygame.transform.scale(tableauCard7.image, (74, 103)), (650,200))

    def _add_foundation(self, card):
        if card.rect.colliderect(self.gameEngine.foundation1):
                 if self.gameEngine.foundation1.can_add_card(card):
                    cardf=self.gameEngine.talon.moveTop()
                    if cardf:
                        self.gameEngine.foundation1.addToFoundation(cardf)
        if card.rect.colliderect(self.gameEngine.foundation2):
                 if self.gameEngine.foundation2.can_add_card(card):
                    cardf=self.gameEngine.talon.moveTop()
                    if cardf:
                        self.gameEngine.foundation2.addToFoundation(cardf)
        if card.rect.colliderect(self.gameEngine.foundation3):
                 if self.gameEngine.foundation3.can_add_card(card):
                    cardf=self.gameEngine.talon.moveTop()
                    if cardf:
                        self.gameEngine.foundation3.addToFoundation(cardf)
        if card.rect.colliderect(self.gameEngine.foundation4):
                 if self.gameEngine.foundation4.can_add_card(card):
                    cardf=self.gameEngine.talon.moveTop()
                    if cardf:
                        self.gameEngine.foundation4.addToFoundation(cardf)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    sol = Solitaire()
    sol.run_game()