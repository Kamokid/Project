import sys, pygame
from settings import Settings
from models import Card, Suits

class Solitaire:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
      
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Solitaire")
        self.cardBack = pygame.image.load('images/card_back.png')
        # self.cardBack = pygame.transform.scale(self.cardBack, (int(238*0.4), int(332*0.4)))

        font = pygame.font.SysFont('comicsans',60, True)  # Create a Pygame font object
        self.text_surface = font.render("Hello", True, (0, 0, 0))  # Render the text to a surface

        # self.card = Card(self, "Club", "2")
        self.card = Card(Suits.CLUB, 2)
        self.card.image = pygame.transform.scale(self.card.image, (74, 103))

        # Define the rectangle's size and color
        self.rect_width = 74
        self.rect_height = 103
        self.rect_color = (128, 128, 128)  # Gray

        # # Create a pygame.Rect object representing the rectangle
        self.rect = pygame.Rect(0, 0, self.rect_width, self.rect_height)
        self.rect.top = 50
        self.rect.right = 420  # Adjust the x-coordinate as desired

        # # Create a pygame.Rect object representing the rectangle
        self.rect1 = pygame.Rect(0, 0, self.rect_width, self.rect_height)
        self.rect1.top = 50
        self.rect1.left = self.rect.right + 25  # Adjust the x-coordinate as desired

        # # Create a pygame.Rect object representing the rectangle
        self.rect2 = pygame.Rect(0, 0, self.rect_width, self.rect_height)
        self.rect2.top = 50
        self.rect2.left = self.rect1.right + 25  # Adjust the x-coordinate as desired

        # # Create a pygame.Rect object representing the rectangle
        self.rect3 = pygame.Rect(0, 0, self.rect_width, self.rect_height)
        self.rect3.top = 50
        self.rect3.left = self.rect2.right + 25  # Adjust the x-coordinate as desired

        # # Create a pygame.Rect object representing the rectangle
        self.rect4 = pygame.Rect(0, 0, self.rect_width, self.rect_height)
        self.rect4.top = 200
        self.rect4.left = 50  # Adjust the x-coordinate as desired

        # # Create a pygame.Rect object representing the rectangle
        self.rect5 = pygame.Rect(0, 0, self.rect_width, self.rect_height)
        self.rect5.top = 200
        self.rect5.left = self.rect4.right + 25  # Adjust the x-coordinate as desired

        # # Create a pygame.Rect object representing the rectangle
        self.rect6 = pygame.Rect(0, 0, self.rect_width, self.rect_height)
        self.rect6.top = 200
        self.rect6.left = self.rect5.right + 25  # Adjust the x-coordinate as desired

        # # Create a pygame.Rect object representing the rectangle
        self.rect7 = pygame.Rect(0, 0, self.rect_width, self.rect_height)
        self.rect7.top = 200
        self.rect7.left = self.rect6.right + 25 # Adjust the x-coordinate as desired

        # # Create a pygame.Rect object representing the rectangle
        self.rect8 = pygame.Rect(0, 0, self.rect_width, self.rect_height)
        self.rect8.top = 200
        self.rect8.left = self.rect7.right + 25  # Adjust the x-coordinate as desired

        # # Create a pygame.Rect object representing the rectangle
        self.rect9 = pygame.Rect(0, 0, self.rect_width, self.rect_height)
        self.rect9.top = 200
        self.rect9.left = self.rect8.right + 25  # Adjust the x-coordinate as desired

        # # Create a pygame.Rect object representing the rectangle
        self.rect10 = pygame.Rect(0, 0, self.rect_width, self.rect_height)
        self.rect10.top = 200
        self.rect10.left = self.rect9.right + 25  # Adjust the x-coordinate as desired

        
  
    def run_game(self):
    # Start the main loop for the game.
        while True:

            self._check_events()
            self._update_screen()

        # Make the most recently drawn screen visible.
            pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        mouse_click = False

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Check if left mouse button was clicked
                    #    mouse_click = True
                       print("clicked")
                       self.screen.blit(self.text_surface, (300, 300))  # Draw the text surface onto the screen               
    
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.cardBack, (50, 50))
        self.screen.blit(self.card.image, (146, 50))
        
        # # Draw a filled rectangle with the background color
        pygame.draw.rect(self.screen, self.settings.bg_color, self.rect)
        pygame.draw.rect(self.screen, self.settings.bg_color, self.rect1)
        pygame.draw.rect(self.screen, self.settings.bg_color, self.rect2)
        pygame.draw.rect(self.screen, self.settings.bg_color, self.rect3)
        pygame.draw.rect(self.screen, self.settings.bg_color, self.rect4)
        pygame.draw.rect(self.screen, self.settings.bg_color, self.rect5)
        pygame.draw.rect(self.screen, self.settings.bg_color, self.rect6)
        pygame.draw.rect(self.screen, self.settings.bg_color, self.rect7)
        pygame.draw.rect(self.screen, self.settings.bg_color, self.rect8)
        pygame.draw.rect(self.screen, self.settings.bg_color, self.rect9)
        pygame.draw.rect(self.screen, self.settings.bg_color, self.rect10)

        # # Draw a rectangle with a black boundary on top of the filled rectangle
        pygame.draw.rect(self.screen, self.rect_color, self.rect, 3)
        pygame.draw.rect(self.screen, self.rect_color, self.rect1, 3)
        pygame.draw.rect(self.screen, self.rect_color, self.rect2, 3)
        pygame.draw.rect(self.screen, self.rect_color, self.rect3, 3)
        pygame.draw.rect(self.screen, self.rect_color, self.rect4, 3)
        pygame.draw.rect(self.screen, self.rect_color, self.rect5, 3)
        pygame.draw.rect(self.screen, self.rect_color, self.rect6, 3)
        pygame.draw.rect(self.screen, self.rect_color, self.rect7, 3)
        pygame.draw.rect(self.screen, self.rect_color, self.rect8, 3)
        pygame.draw.rect(self.screen, self.rect_color, self.rect9, 3)
        pygame.draw.rect(self.screen, self.rect_color, self.rect10, 3)

        # self.card.blitme()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    sol = Solitaire()
    sol.run_game()