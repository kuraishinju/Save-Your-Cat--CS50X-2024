import pygame
from pygame.locals import MOUSEBUTTONDOWN, MOUSEMOTION
from string import capwords
from helpers import render_textrect, TextRectException, simple_text, paragraph, selected_hover, requirements

# * MAIN MENU
class Menu:
    def __init__(self, font_title, font_footer, font_text, pink, blue, selected_class, cat_name, game_state):
        
        # definiamo variabili uniche
        self.selected_class = selected_class
        self.cat_name = cat_name
        self.game_state = game_state
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

        # scelta classe
        self.cat_choice, self.cat_rect = simple_text(
            font_text, "What's your cat's name? Maximum 10 letters", pink, (350, 335)
        )

        # TODO casella nome gatto
        

        # casella errore
        self.er, self.er_rect = simple_text(
            font_text, "Please, select at least one class and enter a valid cat name", pink, (350, 335)
        )

        # play button
        self.play_button, self.play_rect = paragraph(
            "+--------+\n|  PLAY  |\n+--------+", 90, 61, (350, 430), font_text, pink, "Black", 1, 0
        )

    # * events
    def class_selection(self, event):
        # Gestisce la selezione della classe
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.knight_rect.collidepoint(mouse_pos):
                # print debug statements
                print("Knight clicked!")
                self.selected_class = "knight"
            elif self.adv_rect.collidepoint(mouse_pos):
                print("adv clicked!")
                self.selected_class = "adv"
            elif self.wiz_rect.collidepoint(mouse_pos):
                print("wiz clicked!")
                self.selected_class = "wiz"
        return self.selected_class
    
    
    def cat_naming(self, event):
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.play_rect.collidepoint(mouse_pos):
                if requirements(self.selected_class, user_in):
                    # self.cat_name = capwords(user_in)
                    # self.game_state = "menu"
                    return self.cat_name, self.game_state
                else:
                    self.error = 1
                    return

    def hover(self, event):
        if event.type == MOUSEMOTION:
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
    def draw(self, screen, font_text, pink, blue):
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