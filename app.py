import pygame
from pygame.locals import QUIT
from sys import exit
from game import Menu

pygame.init()

# nome gioco
pygame.display.set_caption("•ﻌ• Save the cat •ﻌ•")

# window
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# fonts
main_font = "graphics/Retro Gaming.ttf"
font_title = pygame.font.Font(main_font, 50)
font_footer = pygame.font.Font(main_font, 14)
font_text = pygame.font.Font(main_font, 15)

# colors
pink = pygame.Color("deeppink")
blue = pygame.Color("cyan2")

# background image
background_image = pygame.image.load("graphics/cat.png").convert_alpha()

# * CHOICES
selected_class = None
cat_name = None
game_state = "menu"

# * imported classes
menu = Menu(font_title, font_footer, font_text, pink, blue, selected_class, cat_name, game_state)

# * MAIN LOOP
while True:
    # controllo eventi
    for event in pygame.event.get():
        # chiusura finestra
        if event.type == pygame.QUIT:
            # chiusura pygame
            pygame.quit()
            # uscita dal loop e chiusura
            exit()

        # * eventi game states
        if game_state == "menu":
            menu.hover(event)
            selected_class = menu.class_selection(event)
            cat_name = menu.cat_naming(event)

    # background
    screen.fill("Black")
    screen.blit(background_image, (600,400))

    # * game states drawing
    if game_state == "menu":
        menu.draw(screen, font_text, pink, blue)

    # funzione update della finestra
    pygame.display.update()
    # max framerate
    fps = pygame.time.Clock().tick(60)/1000