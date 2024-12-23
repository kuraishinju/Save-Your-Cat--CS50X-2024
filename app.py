import pygame
import pygame_gui
from pygame.locals import QUIT, MOUSEMOTION
from sys import exit
from game import *

pygame.init()

# nome gioco
pygame.display.set_caption("•ﻌ• Save the cat •ﻌ•")

# window
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# input manager
manager = pygame_gui.UIManager((SCREEN_HEIGHT, SCREEN_WIDTH), "theme.json")

# fonts
main_font = "Retro_Gaming.ttf"
font_title = pygame.font.Font(main_font, 50)
font_footer = pygame.font.Font(main_font, 14)
font_text = pygame.font.Font(main_font, 15)

# colors
pink = pygame.Color("deeppink")
blue = pygame.Color("cyan2")

# background image
background_image = pygame.image.load("graphics/cat.png").convert_alpha()

# TODO CHOICES
selected_class = "adv"
cat_name = "Mary"
game_state = "s1"

# * imported classes
menu = Menu(font_title, font_footer, font_text, pink, blue, selected_class, cat_name, game_state, manager)
s1 = State1(font_text, pink, cat_name, game_state)
s2 = State2(font_text, pink, cat_name, game_state)
s3 = State3(font_text, pink, cat_name, game_state, selected_class)

# * MAIN LOOP
while True:
    # max framerate
    fps = pygame.time.Clock().tick(60)/1000

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
            manager.process_events(event)
            menu.hover(event)
            selected_class = menu.class_selection(event)
            cat_name, game_state = menu.cat_naming(event)
        
        if game_state == "s1":
            s1.choice_hover(event)
            game_state = s1.path(event)
        
        if game_state == "s2":
            s2.choice_hover(event)
            game_state = s2.path(event)
        
        if game_state == "s3":
            s3.choice_hover(event)
            game_state = s3.path(event)

    # background
    screen.fill("Black")
    screen.blit(background_image, (600,400))

    # * game states drawing
    if game_state == "menu":
        menu.draw(screen, fps, font_text, pink, blue)
    
    if game_state == "s1":
        s1.draw(screen, font_text, pink, blue)
    
    if game_state == "s2":
        s2.draw(screen, font_text, pink, blue)
    
    if game_state == "s3":
        s3.draw(screen, font_text, pink, blue)

    # funzione update della finestra
    pygame.display.update()