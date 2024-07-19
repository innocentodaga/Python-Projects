# This will be the settings file containing all the Game settings

class Settings:
    
    def __init__(self):
        # Initialize the game settings
        self.screen_width = 500
        self.screen_height = 500
        self.bg_color = (230, 230, 230)
        self.bluebg = (65, 105, 225)

        # bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 14
        self.bullet_color = (60, 60, 60)
        
        
        # ship speed 
        self.ship_speed = 1.0
        self.ship_limit = 3
        
        # limiting the number of bullets
        self.bullets_allowed = 4
        
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_spedd = 1.0
        
        #fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1
        



        
        