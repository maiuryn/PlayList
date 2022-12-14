import pygame

class Song:

    song_name = "null"
    song_location = "null"

    def __init__(self, name):
        self.song_name = "null"
        self.song_location = "null"

    def set_song(self, song):
        self.song_name = song
    
    def set_location(self, location):
        self.song_location = location
    
    def load_song(self):
        pygame.mixer.music.unload()
        pygame.mixer.music.load(self.song_location)

    def play_song():
        pygame.mixer.music.play()

    def pause_song():
        pygame.mixer.music.pause()
    
    def unpause_song():
        pygame.mixer.music.unpause()

    

