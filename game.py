import pygame
from pygame.locals import MOUSEBUTTONDOWN
from helpers import render_textrect, TextRectException

# * MAIN MENU text, variables and function
class Menu:
    def __init__(self, font_title, font_footer, font_text, pink, selected_class):
        # definiamo selezione
        self.selected_class = selected_class

        # titolo
        self.title = font_title.render("SAVE THE CAT", False, pink)
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (350, 0)

        # footer
        self.footer = font_footer.render("CS50x 2024 final project by Margarita Kolessova", False, pink)
        self.footer_rect = self.footer.get_rect()
        self.footer_rect.center = (350, 470)

        # testo welcome
        self.text1_i = "You are a brave citizen of a far far away kingdom who lives alone with their cat. But one day a tragedy happens: your cat has been kidnapped by the enemy kindgom! Their ruler always preferred dogs, so you fear for your dear one's safety.\nQuick, you need to rescue them!\nWho are you?"
        self.rect1 = pygame.Rect(0, 0, 500, 140)
        self.rect1.center = (350, 200)
        self.text1 = render_textrect(self.text1_i, font_text, self.rect1, pink, "White", justification=1)

        # knight
        self.knight = font_text.render("KNIGHT", False, pink, "Black")
        self.knight_rect = self.knight.get_rect()
        self.knight_rect.center = (175, 285)

        # adventurer
        self.adv = font_text.render("ADVENTURER", False, pink, "Black")
        self.adv_rect = self.adv.get_rect()
        self.adv_rect.center = (350, 285)

        # wizard
        self.wiz = font_text.render("WIZARD", False, pink, "Black")
        self.wiz_rect = self.wiz.get_rect()
        self.wiz_rect.center = (525, 285)

        # scelta classe
        self.cat_choice = font_text.render("What's your cat's name?", False, pink, "White")
        self.cat_rect = self.cat_choice.get_rect()
        self.cat_rect.center = (350, 320)

        # play button
        self.play_text = "+--------+\n|  PLAY  |\n+--------+"
        self.play_rect = pygame.Rect(0, 0, 90, 60)
        self.play_rect.center = (350, 420)
        self.play_button = render_textrect(self.play_text, font_text, self.play_rect, pink, "White", justification=1)

    # event
    def class_selection(self, event):
        # Gestisce la selezione della classe
        if event.type == MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.knight_rect.collidepoint(mouse_pos):
                print("Knight clicked!")  # Debug se il click è su "KNIGHT"
                self.selected_class = "knight"
            elif self.adv_rect.collidepoint(mouse_pos):
                print("adv clicked!")
                self.selected_class = "adv"
            elif self.wiz_rect.collidepoint(mouse_pos):
                print("wiz clicked!")
                self.selected_class = "wiz"
        return self.selected_class
    

    def draw(self, screen, font_text, pink):
        # colore bottoni
        self.knight = font_text.render("KNIGHT", False, "Black" if self.selected_class == "knight" else pink, pink if self.selected_class == "knight" else "Black")
        self.adv = font_text.render("ADVENTURER", False, "Black" if self.selected_class == "adv" else pink, pink if self.selected_class == "adv" else "Black")
        self.wiz = font_text.render("WIZARD", False, "Black" if self.selected_class == "wiz" else pink, pink if self.selected_class == "wiz" else "Black")
        # resto
        screen.blit(self.title, self.title_rect)
        if self.title_rect.centery < 100:
            self.title_rect.centery += 4
        screen.blit(self.footer, self.footer_rect)
        screen.blit(self.text1, self.rect1)
        screen.blit(self.knight, self.knight_rect)
        screen.blit(self.adv, self.adv_rect)
        screen.blit(self.wiz, self.wiz_rect)
        screen.blit(self.cat_choice, self.cat_rect)
        screen.blit(self.play_button, self.play_rect)