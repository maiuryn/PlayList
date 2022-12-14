import pygame
from settings import *
from song import *
from datetime import timedelta
# from tkinter import *
# from tkinter import ttk

class Display:
    
    def __init__(self):
        self.screen = pygame.display.set_mode([screen_width, screen_height], pygame.RESIZABLE)
        self.screen_width = screen_width
        self.screen_height = screen_height

        pygame.display.set_caption("playList")
        pygame.display.set_icon(pygame.image.load("./assets/icon.png"))

        self.font = pygame.font.Font('freesansbold.ttf', text_size)

        self.current_song_name = ""
        self.volume = volume
        
    def draw(self):
        # Clear the screen
        self.screen.fill(pygame.Color("black"))

        # Song volume
        pygame.draw.rect(self.screen, (25, 25, 25), pygame.Rect(0, self.screen_height - 20, self.screen_width, 20))
        pygame.draw.rect(self.screen, (175, 175, 175), pygame.Rect(0, self.screen_height - 20, (self.volume/100)*self.screen_width, 20))

        # Song length
        current_song_length = self.font.render(self.current_song_progress_text + "/" + self.current_song_length_text, False, (255, 255, 255, 255)) 
        text_rect = current_song_length.get_rect(center=(self.screen_width/2, self.screen_height*2/8))
        self.screen.blit(current_song_length, text_rect)

        # Song Progress
        pygame.draw.rect(self.screen, (50, 50, 50), pygame.Rect(0, self.screen_height - 40, self.screen_width, 20))
        pygame.draw.rect(self.screen, (200, 200, 200), pygame.Rect(0, self.screen_height - 40, (self.current_song_progress/self.current_song_length)*self.screen_width, 20))

        # Display current song name to screen
        current_song = self.font.render(self.current_song_name, False, (255, 255, 255, 255))   
        text_rect = current_song.get_rect(center=(self.screen_width/2, self.screen_height/8))
        self.screen.blit(current_song, text_rect)


    def update(self, song_progress, current_song, volume):
        self.screen_width, self.screen_height = pygame.display.get_window_size()
        self.volume = volume
        
        self.current_song_name = current_song.song_name
        self.current_song_length = current_song.song_length
        self.current_song_progress = song_progress
        self.current_song_length_text = str(timedelta(seconds=current_song.song_length))
        self.current_song_progress_text = str(timedelta(seconds=(song_progress)))

