import pygame
import sys
from settings import *
from song import *

class Player:
    def __init__(self):
        pygame.init()

        # Display
        pygame.display.set_mode([screen_width, screen_height])
        pygame.RESIZABLE
        pygame.SCALED
        pygame.display.set_caption("playList")

    def draw():
        pass

    def update():
        pass
    
    def check_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            # Keyboard Controls
            if event.type == pygame.K_SPACE:
                pass
            if event.type == pygame.K_RIGHT:
                pass
            if event.type == pygame.K_LEFT:
                pass
    
    def run(self):
        while True:
            self.check_events()
            self.draw()

if __name__ == '__main__':
    player = Player()
    player.run()
    
        
