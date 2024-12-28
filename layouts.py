import pygame
import pygame_gui
from string import capwords
from helpers import *

pygame.init()

pink = pygame.Color("deeppink")
blue = pygame.Color("cyan2")

main_font = "Retro_Gaming.ttf"
font_title = pygame.font.Font(main_font, 35)
font_footer = pygame.font.Font(main_font, 14)
font_text = pygame.font.Font(main_font, 15)
font_ending = pygame.font.Font(main_font, 25)

# * MAIN MENU
class Menu:
    def __init__(self, manager, selected_class):
        # input manager
        self.manager = manager

        # definiamo variabili uniche
        self.game_state = "menu"
        self.selected_class = selected_class
        self.error = 0
        self.mouse = None

        # titolo
        self.title, self.title_rect = simple_text(
            font_title, "SAVE YOUR CAT!", blue, (350, 0)
        )

        # footer
        self.footer, self.footer_rect = simple_text(
            font_footer, "CS50x 2024 final project by Margarita Kolessova", pink, (350, 470)
        )

        # testo welcome
        self.text_w, self.text_w_rect = paragraph(
            "You are a brave citizen of a far far away kingdom who lives alone with their cat. But one day a tragedy happens: your cat has been kidnapped by the enemy kindgom! Their ruler always preferred dogs, so you fear for your dear one's safety.\nQuick, you need to rescue them!\nWho are you? Click to select a class", 500, 250, (350, 230), font_text, pink, "Black", 1, 4
        )

        # choices x
        choices_x = 295

        # knight
        self.knight, self.knight_rect = simple_text(
            font_text, "KNIGHT", pink, (175, choices_x)
        )

        # adventurer
        self.adv, self.adv_rect = simple_text(
            font_text, "ADVENTURER", pink, (350, choices_x)
        )

        # wizard
        self.wiz, self.wiz_rect = simple_text(
            font_text, "WIZARD", pink, (525, choices_x)
        )

        # testo nome gatto
        self.cat_choice, self.cat_rect = simple_text(
            font_text, "What's your cat's name? Maximum 10 letters", pink, (350, 335)
        )

        # casella nome gatto
        self.cat_in = pygame_gui.elements.UITextEntryLine(
            relative_rect = pygame.Rect(290, 350, 150, 30),
            manager=self.manager,
            object_id="#cat_name",
            placeholder_text="Enter name"
        )

        # casella errore
        self.er, self.er_rect = simple_text(
            font_text, "Please, select at least one class and enter a valid cat name", pink, (350, 390)
        )

        # play button
        self.play_button, self.play_rect = paragraph(
            "+--------+\n|  PLAY  |\n+--------+", 90, 61, (350, 430), font_text, pink, "Black", 1, 0
        )

    # * events
    def class_selection(self, event):
        # Gestisce la selezione della classe
        mouse_pos = pygame.mouse.get_pos()
        if self.knight_rect.collidepoint(mouse_pos):
            self.selected_class = "knight"
        elif self.adv_rect.collidepoint(mouse_pos):
            self.selected_class = "adv"
        elif self.wiz_rect.collidepoint(mouse_pos):
            self.selected_class = "wiz"
        return self.selected_class
    
    
    def cat_naming(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if self.play_rect.collidepoint(mouse_pos):
            self.cat_name = capwords(self.cat_in.get_text())
            if requirements(self.selected_class, self.cat_name):
                self.game_state = "s1"
                return self.cat_name, self.game_state
            else:
                self.error = 1
        return None, "menu"

    def hover(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if self.knight_rect.collidepoint(mouse_pos):
            self.mouse = "knight"
        elif self.adv_rect.collidepoint(mouse_pos):
            self.mouse = "adv"
        elif self.wiz_rect.collidepoint(mouse_pos):
            self.mouse = "wiz"
        elif self.play_rect.collidepoint(mouse_pos):
            self.mouse = "play"
        else:
            self.mouse = None

    # * draw
    def draw(self, screen, fps):
        # colore bottoni
        self.knight = selected_hover(
            font_text, "KNIGHT", "knight", "Black", pink, blue, self.selected_class, self.mouse
        )
        self.adv = selected_hover(
            font_text, "ADVENTURER", "adv", "Black", pink, blue, self.selected_class, self.mouse
        )
        self.wiz = selected_hover(
            font_text, "WIZARD", "wiz", "Black", pink, blue, self.selected_class, self.mouse
        )
        self.play_button = render_textrect(
            "+--------+\n|  PLAY  |\n+--------+",
            font_text,
            self.play_rect,
            blue if self.mouse == "play" else pink,
            "Black",
            justification=1,
            line_spacing=0
        )
        
        # schermata
        screen.blit(self.title, self.title_rect)
        if self.title_rect.centery < 70:
            self.title_rect.centery += 4
        screen.blit(self.footer, self.footer_rect)
        screen.blit(self.text_w, self.text_w_rect)
        screen.blit(self.knight, self.knight_rect)
        screen.blit(self.adv, self.adv_rect)
        screen.blit(self.wiz, self.wiz_rect)
        screen.blit(self.cat_choice, self.cat_rect)
        screen.blit(self.play_button, self.play_rect)
        if self.error == 1:
            screen.blit(self.er, self.er_rect)
        
        self.manager.update(fps)
        self.manager.draw_ui(screen)

# * paths
class Choice:
    # * scelte multiple
    def __init__(self, screen_n, story_text, choice1, path1, choice2 = None, path2 = None):
        self.game_state = screen_n
        self.story_text = story_text
        self.choice1 = choice1
        self.choice2 = choice2
        self.path1 = path1
        self.path2 = path2
        self.mouse = None

        self.story, self.story_rect = paragraph(self.story_text, 550, 350, (350, 220), font_text, pink, "Black", 0, 4)
        self.scelta, self.scelta_rect = simple_text(font_text, self.choice1, pink, (350, 360)
        )
        if self.choice2 != None:
            self.scelta2, self.scelta2_rect = simple_text(font_text, self.choice2, pink, (350, 395))

    # * funzioni
    def update(self, event, selected_class, cat_name):
        self.selected_class = selected_class
        self.cat_name = cat_name

    def choice_hover(self, event):
        if self.choice2 != None:
            self.mouse = choice_hover_ex(event, self.scelta_rect, self.scelta2_rect, self.mouse)
        else:
            self.mouse = choice_hover_ex_s(event, self.scelta_rect, self.mouse)
    
    def path(self, event):
        if self.path2 != None:
            self.next_state = choice(event, self.scelta_rect, self.scelta2_rect, self.game_state, self.path1, self.path2)
            return self.next_state
        else:
            self.next_state = choice_s(event, self.scelta_rect, self.game_state, self.path1)
            return self.next_state
    
    def draw(self, screen):
        # hover
        self.scelta = color_hover(
            font_text, self.choice1, "scelta", "Black", pink, blue, self.mouse
        )
        if self.choice2 != None:
            self.scelta2 = color_hover(
                font_text, self.choice2, "scelta2", "Black", pink, blue, self.mouse
            )

        # schermata
        screen.blit(self.story, self.story_rect)
        screen.blit(self.scelta, self.scelta_rect)
        if self.choice2 != None:
            screen.blit(self.scelta2, self.scelta2_rect)

# * endings
class Ending:
    def __init__(self, screen_n, title_text, story_text, cat_name, selected_class):
        self.game_state = screen_n
        self.title_text = title_text
        self.story_text = story_text
        self.cat_name = cat_name
        self.selected_class = selected_class
        self.mouse = None

        self.title, self.title_rect = simple_text(font_title, self.title_text, pink, (350, 50))
        self.story, self.story_rect = paragraph(self.story_text, 550, 350, (350, 270), font_text, pink, "Black", 0, 4)
        self.exit_button, self.exit_rect = paragraph(
            "+---------------+\n|  EXIT GAME  |\n+---------------+", 150, 61, (200, 400), font_text, pink, "Black", 1, 0
        )
        self.menu_button, self.menu_rect = paragraph(
            "+-------------------+\n|  BACK TO MENU  |\n+-------------------+", 190, 61, (500, 400), font_text, pink, "Black", 1, 0
        )
    
    def hover(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if self.menu_rect.collidepoint(mouse_pos):
            self.mouse = "menu"
        elif self.exit_rect.collidepoint(mouse_pos):
            self.mouse = "exit"
        else:
            self.mouse = None

    def path(self, event):
        mouse_pos = pygame.mouse.get_pos()
        if self.menu_rect.collidepoint(mouse_pos):
            self.game_state = "menu"
            self.cat_name = None
            self.selected_class = None
            return self.game_state, self.cat_name, self.selected_class
        elif self.exit_rect.collidepoint(mouse_pos):
            pygame.quit()
            return None
            exit()
        return self.game_state, self.cat_name, self.selected_class

    # funzioni  
    def draw(self, screen):
        self.exit_button = render_textrect(
            "+---------------+\n|  QUIT GAME  |\n+---------------+",
            font_text,
            self.exit_rect,
            blue if self.mouse == "exit" else pink,
            "Black",
            justification=1,
            line_spacing=0
        )

        self.menu_button = render_textrect(
            "+-------------------+\n|  BACK TO MENU  |\n+-------------------+",
            font_text,
            self.menu_rect,
            blue if self.mouse == "menu" else pink,
            "Black",
            justification=1,
            line_spacing=0
        )

        # schermata
        screen.blit(self.title, self.title_rect)
        screen.blit(self.story, self.story_rect)
        screen.blit(self.exit_button, self.exit_rect)
        screen.blit(self.menu_button, self.menu_rect)