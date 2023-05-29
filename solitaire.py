import sys, pygame
from settings import Settings
from models import Card, Suits
from engine import GameEngine

class Solitaire:
    """Overall class to manage game assets and behavior."""
    def __init__(self):
        """Initialize the game, and create game resources."""
        GameStartUp(self)
  
    def run_game(self):
    # Start the main loop for the game.
        while True:
            self._check_events()
            self._update_screen()
           
        # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

    def retry_game(self):
        GameStartUp(self)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        # mouse_click = False

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left mouse button
                        self.leftclick_down = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:  # Left mouse button
                        self.leftclick_down = False

        # Getting the mouse position then sending it to the engine to determine game logic.
        mouse_pos = pygame.mouse.get_pos()
        self.gameEngine.detectMouse(self.leftclick_down, mouse_pos)
             
    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        mouse_pos = pygame.mouse.get_pos()

        self.screen.fill(self.settings.bg_color)
        self.gameEngine.stock.draw(self.screen)
        self.gameEngine.talon.draw(self.screen)
        self.gameEngine.foundations[0].draw(self.screen)
        self.gameEngine.foundations[1].draw(self.screen)
        self.gameEngine.foundations[2].draw(self.screen)
        self.gameEngine.foundations[3].draw(self.screen)
        self.gameEngine.tableaus[0].draw(self.screen)
        self.gameEngine.tableaus[1].draw(self.screen)
        self.gameEngine.tableaus[2].draw(self.screen)
        self.gameEngine.tableaus[3].draw(self.screen)
        self.gameEngine.tableaus[4].draw(self.screen)
        self.gameEngine.tableaus[5].draw(self.screen)
        self.gameEngine.tableaus[6].draw(self.screen)
        self.gameEngine.mouse_object.draw(self.screen, mouse_pos)

        #Drawing the retry_button image onto the screen
        if self.leftclick_down:
            # Player clicked the retry button
            if self.retry_clicked_button_rect.collidepoint(mouse_pos) or self.retry_button_rect.collidepoint(mouse_pos) or self.retry_button_hover_rect.collidepoint(mouse_pos):
                self.screen.blit(self.retry_button_clicked, self.retry_clicked_button_rect)
                self.retry_clicked = True
            # Player clicked something else, display normal button
            else:
                self.screen.blit(self.retry_button, self.retry_button_rect)
        else:
            # Player is hovering over the retry button with their mouse
            if self.retry_clicked_button_rect.collidepoint(mouse_pos) or self.retry_button_rect.collidepoint(mouse_pos) or self.retry_button_hover_rect.collidepoint(mouse_pos):
                self.screen.blit(self.retry_button_hover, self.retry_button_hover_rect)
                if self.retry_clicked == True: # The player clicked and now let go of the mouse button while still hovering over the button 
                    self.gameEngine.RetryClicked()
                    self.retry_clicked = False

            # Player isn't hovering over the button, display normal button
            else:
                self.screen.blit(self.retry_button, self.retry_button_rect)
                self.retry_clicked = False

def GameStartUp(self):
    pygame.init()
    self.settings = Settings()
    self.leftclick_down = False
    self.retry_clicked = False
    self.screen = pygame.display.set_mode(
        (self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Solitaire")

    self.clock = pygame.time.Clock()
    self.gameEngine = GameEngine(self)

    font = pygame.font.SysFont('comicsans',60, True)  # Create a Pygame font object
    self.text_surface = font.render("Hello", True, (0, 0, 0))  # Render the text to a surface

    self.rect_width = 74
    self.rect_height = 103
    self.rect_color = (128, 128, 128)  # Gray

    # Retry Button
    self.retry_button = pygame.image.load('images/Retry_button.png')
    self.button_padding = 20
    self.retry_button_rect = self.retry_button.get_rect()
    self.retry_button_rect.bottomright = (self.settings.screen_width - self.button_padding, self.settings.screen_height - self.button_padding)

    # Retry Button clicked
    self.retry_button_clicked = pygame.image.load('images/Retry_button_clicked.png')
    self.retry_clicked_button_rect = self.retry_button_clicked.get_rect()
    self.retry_clicked_button_rect.bottomright = (self.settings.screen_width - self.button_padding, self.settings.screen_height - self.button_padding)

    # Retry Button hover
    self.retry_button_hover = pygame.image.load('images/Retry_button_hover.png')
    self.retry_button_hover_rect = self.retry_button_hover.get_rect()
    self.retry_button_hover_rect.bottomright = (self.settings.screen_width - self.button_padding, self.settings.screen_height - self.button_padding)

if __name__ == '__main__':
    # Make a game instance, and run the game.
    sol = Solitaire()
    sol.run_game()