import sys
import pygame
from settings import Settings
from midship import MidShip

class AlienInvasion:
    def __init__(self):
        pygame.init()

        # Import our settings
        self.settings = Settings()

        # Setting our environment
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Tyson Is Trying")

        # Initialize the ship after setting up the screen
        self.ship = MidShip(self)

    def run_game(self):
        while True:
            # Capture events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Displaying of the game
            self.screen.fill(self.settings.bg_color)
            self.ship.showMe()
            pygame.display.flip()

# Creating the game instance
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
