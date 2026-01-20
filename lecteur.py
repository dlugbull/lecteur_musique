import pygame
import os
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
import time
from explorateur import*
chemin_base = input("Entrez le chemin d'accès de votre dossier de musiques : ")
if chemin_base[-1] != "/":
    chemin_base += "/"
base = Folder(chemin_base, None)

def affiche(folder):
    print("    "*folder.depth + folder.name)
    if os.path.isdir(folder.path):
        for i in folder.children:
            affiche(i)



def play_song(song):
    audio = MP3(song.path, ID3=ID3) # Supprimer les commentaires invalides
    if "COMM" in audio.tags: 
        del audio.tags["COMM"]
    audio.save()


    pygame.mixer.init()                 # Initialise le module audio
    pygame.mixer.music.load(song.path)  # Charge ton fichier MP3
    pygame.mixer.music.play()           # Lance la lecture

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

line=Song("/home/dlugbull/Musique/twenty one pilots/Arcane/The Line.mp3")
play_song(line)