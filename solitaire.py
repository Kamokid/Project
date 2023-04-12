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
        self.leftclick_down = False
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Solitaire")

        self.clock = pygame.time.Clock()
        self.gameEngine = GameEngine()

        font = pygame.font.SysFont('comicsans',60, True)  # Create a Pygame font object
        self.text_surface = font.render("Hello", True, (0, 0, 0))  # Render the text to a surface

        self.rect_width = 74
        self.rect_height = 103
        self.rect_color = (128, 128, 128)  # Gray

  
    def run_game(self):
    # Start the main loop for the game.
        while True:
            self._check_events()
            self._update_screen()
           
        # Make the most recently drawn screen visible.
            pygame.display.flip()
            self.clock.tick(60)

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

if __name__ == '__main__':
    # Make a game instance, and run the game.
    sol = Solitaire()
    sol.run_game()