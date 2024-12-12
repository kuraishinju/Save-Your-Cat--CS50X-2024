import pygame
from sys import exit

pygame.init()
# nome gioco
pygame.display.set_caption("•ﻌ• Save the cat •ﻌ•")
# window
screen = pygame.display.set_mode((700,500))

# fonts
font_title = pygame.font.Font("graphics/Minecraft.ttf", 50)
font_footer = pygame.font.Font("graphics/Minecraft.ttf", 17)
# background
background_image = pygame.image.load("graphics/cat.png").convert_alpha()

# main menu text and variables
title = font_title.render("SAVE THE CAT", False, pygame.Color("hotpink2"))
title_position = 0
footer = font_footer.render("CS50x 2024 final project by Margarita Kolessova", False, pygame.Color("hotpink2"))

# main loop
while True:
    # controllo eventi
    for event in pygame.event.get():
        # chiusura finestra
        if event.type == pygame.QUIT:
            # chiusura pygame
            pygame.quit()
            # uscita dal loop e chiusura
            exit()

    # background with cat
    screen.fill(pygame.Color("lavenderblush"))
    screen.blit(background_image, (600,400))

    # menu
    screen.blit(title, (200,title_position))
    if title_position < 100:
        title_position += 3
    screen.blit(footer, (200,450))


    # funzione update della finestra
    pygame.display.update()
    # max framerate
    pygame.time.Clock().tick(60)