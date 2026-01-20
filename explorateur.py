import pygame
import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
import time

class Song():
    def __init__(self, path:str):
        self.path = path
        self.name = path.split("/")[-1]
        self.depth = len(path.split("/"))-4

    def play_song(self):
        audio = MP3(self.path, ID3=ID3) # Supprimer les commentaires invalides
        if "COMM" in audio.tags: 
            del audio.tags["COMM"]
        audio.save()


        pygame.mixer.init()
        pygame.mixer.music.load(self.path)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            time.sleep(0.1)

class Folder():
    def __init__(self, path:str, parent):
        self.path = path
        self.parent = parent
        self.name = path.split("/")[-2]
        self.depth = len(path.split("/"))-5
        self.children = list(self.generate_children())
        self.expanded = False
    
    def generate_children(self):
        for child in os.listdir(self.path):
            if os.path.isdir(self.path+child):
                yield Folder(self.path+child+"/", self)
            
            elif child.split(".")[-1] == "mp3" and len(child)>3:
                yield Song(self.path+child)