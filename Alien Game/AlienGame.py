# Alien Invasion Game
# In Alien Invasion, the player controls a rocket ship that appears 
# at the bottom center of the screen. The player can move the ship 
# right and left using the arrow keys and shoot bullets using the 
# spacebar. When the game begins, a fleet of aliens fills the sky 
# and moves across and down the screen. The player shoots and 
# destroys the aliens. If the player shoots all the aliens, a new fleet 
# appears that moves faster than the previous fleet. If any alien hits 
# the player’s ship or reaches the bottom of the screen, the player 
# loses a ship. If the player loses three ships, the game ends

import sys
import pygame

# Importing the game settings in our game
from settings import Settings

# importing the ship class
from ship import Ship

class AlienInvasion:
    # This is the overall class to manage game assets and behaviors
    
    def __init__(self):
        # Initialize the game and create game resources
        pygame.init()
        
        # include in our settings
        self.settings = Settings()

        # This specifies the screen dimensions and the game environment 
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion") # title to be displayed

        # initializing the ship attribute
        self.ship = Ship(self) 
        
    # method that launches the game
    def run_game(self):
        # Start the game loop
        while True:
            # checking for the events
            self.check_events()
            
            # updating the screen
            self.update_screen()
                                    
    def check_events(self):
        # Responds to keypresses and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 
                            
    # update images on teh screen and flip to the new screen
    def update_screen(self):
        # Make the most recently drawn screen visible
        pygame.display.flip()
        self.screen.fill(self.settings.bluebg) # Setting the bg color

        
        #include the ship
        self.ship.blitme()

if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
