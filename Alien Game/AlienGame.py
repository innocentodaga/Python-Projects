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

# importing the bullets

from bullet import Bullet

class AlienInvasion:
    # This is the overall class to manage game assets and behaviors
    
    def __init__(self):
        # Initialize the game and create game resources
        pygame.init()
        
        # bullets
        self.bullets = pygame.sprite.Group()
        
        # include in our settings
        self.settings = Settings()

        # This specifies the screen dimensions and the game environment 
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion") # title to be displayed

        # initializing the ship attribute
        self.ship = Ship(self) 
        
    # method that launches the game
    def run_game(self):
        # Start the game loop
        while True:
            # checking for the events
            self.check_events()
            
            # update ship movement
            self.ship.update()
            
            # update bullets
            self.update_bullets()
            
            # Get rid of bulletst that have disappeared to avoid over consumption of memory and power
            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:
                    self.bullets.remove(bullet)
            print(len(self.bullets))
            
            # updating the screen
            self.update_screen()
            
            # updating the bullets 
            self.bullets.update()
    # update images on teh screen and flip to the new screen
    def update_screen(self):
        # Make the most recently drawn screen visible
        pygame.display.flip()
        self.screen.fill(self.settings.bluebg) # Setting the bg color
        
        #include the ship
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def check_events(self):
        # Responds to keypresses and mouse events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit() 
                elif event.type == pygame.KEYDOWN:
                    self.check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                    self.check_keyup_events(event)
                    
    def check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # move the ship to the right.
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self.fire_bullet()
            
    def check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False
            
    # create new bullet and add it to the bullets group
    def fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
     
    # updating the bullets
    def update_bullets(self):
        #update the bullet position
        self.bullets.update()
            
    
if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
