import pygame
from pygame.locals import QUIT
from sys import exit
from game import Menu

# * GAME
pygame.init()

# nome gioco
pygame.display.set_caption("•ﻌ• Save the cat •ﻌ•")
# window
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# fonts and colors
font_title = pygame.font.Font("graphics/Minecraft.ttf", 50)
font_footer = pygame.font.Font("graphics/Minecraft.ttf", 17)
font_text = pygame.font.Font("graphics/Minecraft.ttf", 19)
pink = pygame.Color("deeppink")
# background
background_image = pygame.image.load("graphics/cat.png").convert_alpha()

# * CHOICES
selected_class = None
game_state = "menu"

# * imported classes
menu = Menu(font_title, font_footer, font_text, pink, selected_class)

# * MAIN LOOP
while True:
    # * controllo eventi
    for event in pygame.event.get():
        # chiusura finestra
        if event.type == pygame.QUIT:
            # chiusura pygame
            pygame.quit()
            # uscita dal loop e chiusura
            exit()

        # selezione classe
        if game_state == "menu":
            selected_class = menu.class_selection(event)

    # background
    screen.fill("Black")
    screen.blit(background_image, (600,400))

    if game_state == "menu":
        menu.draw(screen, font_text, pink)

    # funzione update della finestra
    pygame.display.update()
    # max framerate
    pygame.time.Clock().tick(60)