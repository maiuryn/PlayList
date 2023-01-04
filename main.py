import pygame
import sys
import glob
from mutagen.mp3 import MP3
from queue import Queue
from settings import *
from song import *
from display import *

END_SONG = pygame.USEREVENT + 1

class Player:
    def __init__(self):
        pygame.init()

        self.playing = False
        self.songs = []
        self.display = Display()
        self.index = 0
        self.current_song = Song("Press Space to Play", "./", -1)
        self.volume = volume
        pygame.mixer.music.set_volume(self.volume)

        pygame.mixer.music.set_endevent(END_SONG)

        # Update Song List
        song_directories = glob.glob(songs_folder)

        # Store names into array
        for song_directory in song_directories:
            self.songs.append(Song(song_directory.replace(".mp3","").replace("./songs\\",""), song_directory, int(MP3(song_directory).info.length)))          
            
        # Put songs into the queue in order
        # for song in self.songs:
        #     self.song_queue.put(song)    
    
    # def load_songs(self, directory):
    #     self.songs.clear()
    #     song_directories = glob.glob(directory)
    #     for song_directory in song_directories:
    #         self.songs.append(Song(song_directory.replace(".mp3","").replace(f"{directory}",""), song_directory, int(MP3(song_directory).info.length)))

    def play_song(self):
        self.playing = True
        # current_song = self.song_queue.get()
        self.current_song = self.songs[self.index]
        self.current_song.load_song()
        pygame.mixer.music.play()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            if event.type == pygame.VIDEORESIZE:
                width, height = event.size
                if width < 426:
                    width = 426
                if height < 240:
                    height = 240
                self.display.screen = pygame.display.set_mode((width,height), pygame.RESIZABLE)
            
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
                    self.index = (self.index + 1) % (len(self.songs))
                    self.play_song()
                if event.key == pygame.K_LEFT:
                    self.index = (self.index - 1) % (len(self.songs))
                    self.play_song()
                
                if event.key == pygame.K_UP:
                    self.volume = self.volume + 5
                    if self.volume > 100:
                        self.volume = 100
                if event.key == pygame.K_DOWN:
                    self.volume = self.volume - 5
                    if self.volume < 0:
                        self.volume = 0
            
            # Play the next song
            if event.type == END_SONG:
                self.playing = False
                self.index = (self.index + 1) % (len(self.songs))
                self.play_song()              

    def pause_song(self):
        pygame.mixer.music.pause()
    
    def unpause_song(self):
        pygame.mixer.music.unpause()
    

    def run(self):
        while True:
            pygame.mixer.music.set_volume(self.volume/100)
            self.check_events()
            self.display.update(pygame.mixer.music.get_pos()//1000, self.current_song, self.volume)  
            self.display.draw()
            pygame.display.update()

if __name__ == '__main__':
    player = Player()
    player.run()      
