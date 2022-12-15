import pygame
import sys
import glob
from queue import Queue
from settings import *
from song import *
from display import *

END_SONG = pygame.USEREVENT + 1

class Player:
    playing = False
    #song_names = []
    songs = []
    song_queue = Queue()
    display = Display()

    def __init__(self):
        pygame.init()

        # Update Song List
        song_names = glob.glob(songs_folder)

        # Store names into array
        for song_name in song_names:
            self.songs.append(Song(song_name.replace(".mp3","").replace("./Songs\\",""), song_name))
            
        # Put songs into the queue in order
        for song in self.songs:
            self.song_queue.put(song)       

    def play_song(self):
        self.playing = True
        current_song = self.song_queue.get()
        current_song.load_song()
        pygame.mixer.music.play()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            
            # Keyboard Controls
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.playing == False and pygame.mixer.music.get_busy() == False:
                        self.play_song()
                    elif pygame.mixer.music.get_busy() == True:
                        self.pause_song()
                    elif pygame.mixer.music.get_busy() == False:
                        self.unpause_song()
                    
                if event.key == pygame.K_RIGHT:
                    pygame.mixer.music.unload()
                    self.play_song()
                if event.key == pygame.K_LEFT:
                    pass
            
            # Play the next song
            if event.type == END_SONG:
                self.playing = False
                self.play_song()
                

    def pause_song(self):
        pygame.mixer.music.pause()
    
    def unpause_song(self):
        pygame.mixer.music.unpause()
    

    def run(self):
        while True:
            self.check_events()
            #self.play_song()
            self.display.draw()

if __name__ == '__main__':
    player = Player()
    player.run()      
