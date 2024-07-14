import sys, pygame
from settings import Settings

class AlienInvasion:
    
    def __init__(self):
        
        pygame.init()
        
        # import our settings
        self.settings = Settings()
        
        # seting our env't
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Tyson Is Trying")
        
    def runGame(self):
        while True:
            # Capture events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # displaying of the game
            pygame.display.flip()
            self.screen.fill(self.settings.bg_color)
            
# creating the game instance
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.runGame()
            