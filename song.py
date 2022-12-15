import pygame

class Song:

    song_name = "null"
    song_location = "null"

    def __init__(self, name, location):
        self.song_name = name
        self.song_location = location

    def set_song(self, song):
        self.song_name = song
    
    def set_location(self, location):
        self.song_location = location
    
    def load_song(self):
        pygame.mixer.music.unload()
        pygame.mixer.music.load(self.song_location)

    

    

