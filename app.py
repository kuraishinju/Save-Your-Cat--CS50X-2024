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
font_ending = pygame.font.Font(main_font, 25)

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
menu = Menu(font_title, font_footer, font_text, pink, blue, selected_class, cat_name, game_state, manager)

# TODO tutto a None
s1 = None
s2 = None
s3 = None
s4 = None
s5 = None
s6 = None
s7 = None
s8 = None
s9 = None
e1 = None
e2 = None

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

        if game_state == "menu":
            manager.process_events(event)
        
        if event.type == MOUSEMOTION:
            if game_state == "menu":
                menu.hover(event)
            elif game_state == "s1":
                s1.choice_hover(event)
            elif game_state == "s2":
                s2.choice_hover(event)
            elif game_state == "s3":
                s3.choice_hover(event)
            elif game_state == "s4":
                s4.choice_hover(event)
            elif game_state == "s5":
                s5.choice_hover(event)
            elif game_state == "s6":
                s6.choice_hover(event)
            elif game_state == "s7":
                s7.choice_hover(event)
            elif game_state == "s8":
                s8.choice_hover(event)
            elif game_state == "s9":
                s9.choice_hover(event)
            elif game_state == "e1":
                e1.hover(event)
            elif game_state == "e2":
                e2.hover(event)

        if event.type == MOUSEBUTTONDOWN:
            if game_state == "menu":
                selected_class = menu.class_selection(event)
                cat_name, game_state = menu.cat_naming(event)
                if cat_name != None and selected_class != None:
                    s1 = State1(font_text, pink, cat_name, game_state)
                    s2 = State2(font_text, pink, cat_name, game_state)
                    s3 = State3(font_text, pink, game_state, selected_class)
                    s4 = State4(font_text, pink, cat_name, game_state)
                    s5 = State5(font_text, pink, cat_name, game_state)
                    s6 = State6(font_text, pink, game_state, selected_class)
                    s7 = State7(font_text, pink, game_state)
                    s8 = State8(font_text, pink, game_state, selected_class, cat_name)
                    s9 = State9(font_text, pink, game_state)

                    e1 = Ending1(font_text, font_ending, pink, cat_name, game_state, selected_class)
                    e2 = Ending2(font_text, font_ending, pink, cat_name, game_state, selected_class)

            elif game_state == "s1":
                game_state = s1.path(event)
            elif game_state == "s2":
                s2 = State2(font_text, pink, cat_name, game_state)
                game_state = s2.path(event)
            elif game_state == "s3":
                s3 = State3(font_text, pink, game_state, selected_class)
                game_state = s3.path(event)
            elif game_state == "s4":
                s4 = State4(font_text, pink, cat_name, game_state)
                game_state = s4.path(event)
            elif game_state == "s5":
                s5 = State5(font_text, pink, cat_name, game_state)
                game_state = s5.path(event)
            elif game_state == "s6":
                s6 = State6(font_text, pink, game_state, selected_class)
                game_state = s6.path(event)
            elif game_state == "s7":
                s7 = State7(font_text, pink, game_state)
                game_state = s7.path(event)
            elif game_state == "s8":
                s8 = State8(font_text, pink, game_state, selected_class, cat_name)
                game_state = s8.path(event)
            elif game_state == "s9":
                s9 = State9(font_text, pink, game_state)
                game_state = s9.path(event)
            elif game_state == "e1":
                e1 = Ending1(font_text, font_ending, pink, cat_name, game_state, selected_class)
                result = e1.path(event)
                if result == None:
                    pygame.quit()
                    exit()
                else:
                    game_state, cat_name, selected_class = result
            elif game_state == "e2":
                e2 = Ending2(font_text, font_ending, pink, cat_name, game_state, selected_class)
                result = e2.path(event)
                if result == None:
                    pygame.quit()
                    exit()
                else:
                    game_state, cat_name, selected_class = result

    # background
    screen.fill("Black")
    screen.blit(background_image, (600,400))

    # * game states drawing
    if game_state == "menu":
        menu.draw(screen, fps, font_text, pink, blue)
    
    elif game_state == "s1":
        s1.draw(screen, font_text, pink, blue)
    
    elif game_state == "s2":
        s2.draw(screen, font_text, pink, blue)
    
    elif game_state == "s3":
        s3.draw(screen, font_text, pink, blue)
    
    elif game_state == "s4":
        s4.draw(screen, font_text, pink, blue)
    
    elif game_state == "s5":
        s5.draw(screen, font_text, pink, blue)

    elif game_state == "s6":
        s6.draw(screen, font_text, pink, blue)

    elif game_state == "s7":
        s7.draw(screen, font_text, pink, blue)

    elif game_state == "s8":
        s8.draw(screen, font_text, pink, blue)

    elif game_state == "s9":
        s9.draw(screen, font_text, pink, blue)

    elif game_state == "e1":
        e1.draw(screen, font_text, pink, blue)

    elif game_state == "e2":
        e2.draw(screen, font_text, pink, blue)

    # funzione update della finestra
    pygame.display.update()