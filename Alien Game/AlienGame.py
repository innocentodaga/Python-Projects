# Alien Invasion Game
import sys
import pygame

from time import sleep

# Importing the game settings in our game
from settings import Settings

# importing the ship class
from ship import Ship

# importing the bullets
from bullet import Bullet

# importing the alien
from alien import Alien

#import the stats
from game_stats import GameStats

class AlienInvasion:
    # This is the overall class to manage game assets and behaviors
    
    def __init__(self):
        # Initialize the game and create game resources
        pygame.init()
        
        # include in our settings
        self.settings = Settings()

        # This specifies the screen dimensions and the game environment 
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion") # title to be displayed

        # create an instance to store game stats
        self.stats = GameStats(self)
        
        # initializing the ship attribute
        self.ship = Ship(self) 

        # bullets
        self.bullets = pygame.sprite.Group()
        
        # aliens 
        self.aliens = pygame.sprite.Group()
        
        self.create_fleet()
        
    # method that launches the game
    def run_game(self):
        # Start the game loop
        while True:
            # checking for the events
            self.check_events()
            
            # update ship movement
            self.ship.update()
            
            #update the alien
            self.update_alien()
            
            # update bullets
            self.update_bullets()
            
            # updating the screen
            self.update_screen()
            
            # updating the bullets 
            self.bullets.update()
    
    # update images on the screen and flip to the new screen
    def update_screen(self):
        # Make the most recently drawn screen visible
        self.screen.fill(self.settings.bluebg) # Setting the bg color
        
        #include the ship
        self.ship.blitme()
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        
        # making the aliens visible on the screen
        self.aliens.draw(self.screen)

        pygame.display.flip()
    
    

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
        # update the bullet position
        self.bullets.update()
            
        # Get rid of bullets that have disappeared to avoid overconsumption of memory and power
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
            print(len(self.bullets))
        self.check_bullet_alien_collision()  
        self.aliens.update()
          
        
    def check_bullet_alien_collision(self):
        # respond to bullet_alien collisions
        #remove any bullets and aliens tht have collided         
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        
        if not self.aliens:
            # destroy existing bullets and create new fleet
            self.bullets.empty()
            self.create_fleet()    
    # create a group to hold the fleet of aliens
    def create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)
        # Determine the number of rows of aliens that fit on the screen.
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height -
        (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)
        
        # Create the full fleet of aliens.
        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number) 

    def _create_alien(self, alien_number, row_number):
        """Create an alien and place it in the row."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)
        
    def update_alien(self):
        # update the alien positions
        self.aliens.update()
        self.check_fleet_edges()
        
        #looking for alien ship collisions
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self.ship_hit()
            
    def check_fleet_edges(self):
        #Respond appropiate if any aliens have reached an edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self.change_fleet_direction()
                break
            
    def change_fleet_direction(self):
        #drop the entire fleet and change the fleet's direction
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_spedd
        self.settings.fleet_direction *= -1
    
    def ship_hit(self):
        # respond to the ship being hit by an alien
        #decrements ships left
        self.stats.ships_left -= 1
        
        # get rid of any remaining aliens and bullets
        self.aliens.empty()
        self.bullets.empty()
        
        # create a new fleet and center the ship
        self.create_fleet()
        self.ship.center_ship()
        
        # pause
        sleep(0.5)
    
    def check_aliens_bottom(self):
        # check if any aliens have reached the bottom of the screen
        screen_rect = self.screen.get_rect()
        
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                # treat this the same as if the ship got hit
                self.ship_hit()
                break
            
    
if __name__ == '__main__':
    # Make a game instance and run the game
    ai = AlienInvasion()
    ai.run_game()
