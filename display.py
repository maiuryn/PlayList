import pygame
from settings import *


class Display:

    def __init__(self):
        pygame.display.set_mode([screen_width, screen_height], pygame.RESIZABLE, pygame.SCALED)    
        pygame.display.set_caption("playList")
        
    def draw(self):
        pass