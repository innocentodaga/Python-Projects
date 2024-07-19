import pygame

class Ship:
    def __init__(self, ai_game):
        # Initialize the ship and set its starting position
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect
        self.image = pygame.image.load('Alien Game/images/ship.bmp')

        # Scale the image
        self.image = pygame.transform.scale(self.image, (55, 75))  # Change (50, 75) to your desired size

        # Update the rect attribute to match the new size
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom
        
        #sotre a decimal value for the ships horizontal position
        self.x = float(self.rect.x)
        
        # movement flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        # update the ship's position based on the movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        
        
        # update rect object from self.x
        self.rect.x = self.x
        
    def blitme(self):
        # Draw the ship at its current location
        self.screen.blit(self.image, self.rect)
    
    def center_ship(self):
        #center the ship on the screen
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
    
    
