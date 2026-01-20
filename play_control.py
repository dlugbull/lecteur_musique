import pygame
from mutagen.mp3 import MP3
from mutagen.id3 import ID3
from explorateur import*

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()

def next(song, waiting_list):
    index=waiting_list.index(song)

    if index==len(waiting_list)-1:
        waiting_list[0].play_song()
    else:
        waiting_list[index+1].play_song()



def previous(song, waiting_list):
    index=waiting_list.index(song)

    if index==0:
        waiting_list[-1].play_song()
    else:
        waiting_list[index-1].play_song()


def lower_volume():
    current_volume = pygame.mixer.music.get_volume()
    if current_volume < 0.05:
        return
    pygame.mixer.music.set_volume(current_volume - 0.05)

def higher_volume():
    current_volume = pygame.mixer.music.get_volume()
    if current_volume > 0.95:
        return
    pygame.mixer.music.set_volume(current_volume + 0.05)