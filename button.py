import pygame
from display import screen

class Button:

    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
         
    def draw(self):
        screen.blit(self.image, )

    def on_click(self):
        pass