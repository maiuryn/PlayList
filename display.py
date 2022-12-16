import pygame
from settings import *
# from tkinter import *
# from tkinter import ttk

class Display:
    
    def __init__(self):
        self.screen = pygame.display.set_mode([screen_width, screen_height], pygame.RESIZABLE, pygame.SCALED)
        self.screen_width = screen_width
        self.screen_height = screen_height

        pygame.display.set_caption("playList")
        pygame.display.set_icon(pygame.image.load("./assets/icon.png"))

        self.font = pygame.font.Font('freesansbold.ttf', text_size)

        self.song_progress = 0
        self.current_song_name = ""
        
    def draw(self):
        # Clear the screen
        self.screen.fill(pygame.Color("black"))

        # Song progress
        pygame.draw.rect(self.screen, (0, 255, 0), pygame.Rect(0, 0, self.song_progress*screen_width, 20))

        # Display current song name to screen
        current_song = self.font.render(self.current_song_name, False, (255, 255, 255, 255))   
        text_rect = current_song.get_rect(center=(self.screen_width/2, self.screen_height/8))
        self.screen.blit(current_song, text_rect)


    def update(self, song_progress, current_song):
        self.screen_width, self.screen_height = pygame.display.get_window_size()

        pygame.mixer.music.set_volume(volume/100)
        
        self.current_song_name = current_song
        self.song_progress = song_progress
