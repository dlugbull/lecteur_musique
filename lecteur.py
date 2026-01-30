import pygame
import time
import eyed3
from play_control import *

chemin_base = input("Entrez le chemin d'accès de votre dossier de musiques : ")
if chemin_base[-1] != "/":
    chemin_base += "/"
base = Folder(chemin_base, None)

def get_img_from_music(song=None):
    if song==None:
        return
    audio_file = eyed3.load(song.path)
    for image in audio_file.tag.images:
        image_file = open("temp.jpg", "wb")
        image_file.write(image.image_data)
        image_file.close()
    


def draw_explorer(folder, start_y=10):
    click_zones.clear()
    y=start_y

    def draw_item(item, y):
        indent = item.depth * 20

        if isinstance(item, Folder):
            if item.expanded:
                prefixe = "[-]"
            else:
                prefixe="[+]"
        else:
            prefixe="   "

        text = font.render(prefixe+" "+item.name, True, (230, 230, 230))
        rect = text.get_rect(topleft=(10+indent, y))
        screen.blit(text, rect)

        click_zones.append((rect, item))
        return y + 20

    def walk(folder, y):
        y = draw_item(folder, y)

        if folder.expanded:
            for child in folder.children:
                if isinstance(child, Folder):
                    y = walk(child, y)
                else:
                    y = draw_item(child, y)
        return y

    walk(folder, y)

pygame.init()
screen = pygame.display.set_mode((0, 0))
font = pygame.font.Font(None, 24)

click_zones = []

def run():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = event.pos

                for rect, item in click_zones:
                    if rect.collidepoint(mx, my):

                        if isinstance(item, Folder):
                            item.expanded = not item.expanded
                        elif isinstance(item, Song):
                            get_img_from_music(item)
                            img = pygame.image.load("temp.jpg")
                            img = pygame.transform.scale(img, (width//2,width//2))
                            screen.blit(img, (sidebar_width, 0))
                            pygame.display.flip()
                            item.play_song()


        screen.fill((40, 40, 40))

        width, height = pygame.display.get_surface().get_size()

        sidebar_width = width//4
        sidebar_rect = pygame.Rect(0, 0, sidebar_width, height)

        pygame.draw.rect(screen, (20, 20, 20), sidebar_rect)
        
        draw_explorer(base)

        pygame.display.flip()


    pygame.quit()

run()