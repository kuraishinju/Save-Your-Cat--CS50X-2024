import pygame
import pygame_gui
from pygame.locals import QUIT, MOUSEMOTION, MOUSEBUTTONDOWN
from sys import exit
from game import update
from layouts import Menu

# gioco
pygame.display.set_caption("•ﻌ• Save Your Cat •ﻌ•")
SCREEN_WIDTH = 700
SCREEN_HEIGHT = 500
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# window
background_image = pygame.image.load("graphics/cat.png").convert_alpha()

# menu variables
manager = pygame_gui.UIManager((SCREEN_HEIGHT, SCREEN_WIDTH), "theme.json")
game_state = "menu"
selected_class = None
cat_name = None
menu = Menu(manager, selected_class)

game_states = {}
endings = {}

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
            elif game_state in game_states:
                game_states[game_state].choice_hover(event)
            elif game_state in endings:
                endings[game_state].hover(event)

        if event.type == MOUSEBUTTONDOWN:
            if game_state == "menu":
                selected_class = menu.class_selection(event)
                cat_name, game_state = menu.cat_naming(event)
                if cat_name != None and selected_class != None:
                    update(selected_class, cat_name, game_states, endings)

            elif game_state in game_states:
                game_states[game_state].update(event, selected_class, cat_name)
                game_state = game_states[game_state].path(event)

            elif game_state in endings:
                result = endings[game_state].path(event)
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
        menu.draw(screen, fps)
    
    elif game_state in game_states:
       game_states[game_state].draw(screen)
    
    elif game_state in endings:
        endings[game_state].draw(screen)

    # funzione update della finestra
    pygame.display.update()