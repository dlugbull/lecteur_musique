import os
import pygame

class Song():
    def __init__(self, path:str):
        self.path = path
        self.name = path.split("/")[-1]
        self.depth = len(path.split("/"))-4

class Folder():
    def __init__(self, path:str, parent):
        self.path = path
        self.parent = parent
        self.name = path.split("/")[-2]
        self.depth = len(path.split("/"))-5
        self.children = list(self.generate_children())
    
    def generate_children(self):
        for child in os.listdir(self.path):
            if os.path.isdir(self.path+child):
                yield Folder(self.path+child+"/", self)
            
            elif child.split(".")[-1] == "mp3" and len(child)>3:
                yield Song(self.path+child)