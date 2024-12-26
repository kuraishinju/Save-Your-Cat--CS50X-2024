import pygame
import pygame_gui
from pygame.locals import MOUSEBUTTONDOWN, MOUSEMOTION
from string import capwords
from helpers import *

# * MAIN MENU
class Menu:
    def __init__(self, font_title, font_footer, font_text, pink, blue, selected_class, cat_name, game_state, manager):
        # input manager
        self.manager = manager

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
    def draw(self, screen, fps, font_text, pink, blue):
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

# * Screen 1
class State1:
    def __init__(self, font_text, pink, cat_name, game_state):
        self.game_state = "s1"
        self.cat_name = cat_name
        self.mouse = None

        # testo
        self.story_text = (f"You come back home from a long work day at the king's castle when... you don't hear {self.cat_name} meowing, complaining that you didn't give them their favorite food but some chicken (how many times do they have to tell you that they love salmon but absolutely despise chicken?!) You are in shock, {self.cat_name} definetly has been kidnapped by the enemy kingdom: the Land of Retrievers! What do you do?")

        self.story, self.story_rect = paragraph(self.story_text, 550, 350, (350, 220), font_text, pink, "Black", 0, 4)

        # scelta 1
        self.scelta, self.scelta_rect = simple_text(font_text, "1. You look for some clues", pink, (350, 360)
        )

        # scelta 2
        self.scelta2, self.scelta2_rect = simple_text(font_text, "2. You pack up for the journey and leave at once", pink, (350, 395)
        )

    # funzioni
    def choice_hover(self, event):
        self.mouse = choice_hover_ex(event, self.scelta_rect, self.scelta2_rect, self.mouse)
    
    def path(self, event):
        self.state_a = "s2"
        self.state_b = "s3"
        self.next_state = choice(event, self.scelta_rect, self.scelta2_rect, self.game_state, self.state_a, self.state_b)
        return self.next_state
    
    def draw(self, screen, font_text, pink, blue):
        # hover
        self.scelta = color_hover(
            font_text, "1. You look for some clues", "scelta", "Black", pink, blue, self.mouse
        )
        self.scelta2 = color_hover(
            font_text, "2. You pack up for the journey and leave at once", "scelta2", "Black", pink, blue, self.mouse
        )

        # schermata
        screen.blit(self.story, self.story_rect)
        screen.blit(self.scelta, self.scelta_rect)
        screen.blit(self.scelta2, self.scelta2_rect)

# * Screen 2
class State2:
    def __init__(self, font_text, pink, cat_name, game_state):
        self.game_state = "s2"
        self.cat_name = cat_name
        self.mouse = None

        # testo
        self.story_text = (f"There are no clues apart from {self.cat_name}'s bowl being untouched and still full of chicken. Your remorse haunts you, you'd better hurry!")

        self.story, self.story_rect = paragraph(self.story_text, 550, 350, (350, 220), font_text, pink, "Black", 0, 4)

        # scelta
        self.scelta, self.scelta_rect = simple_text(font_text, "1. You pack up for the journey and leave", pink, (350, 360)
        )

    # funzioni
    def choice_hover(self, event):
        self.mouse = choice_hover_ex_s(event, self.scelta_rect, self.mouse)
    
    def path(self, event):
        self.state_a = "s3"
        self.game_state = choice_s(event, self.scelta_rect, self.game_state, self.state_a)
        return self.game_state
    
    def draw(self, screen, font_text, pink, blue):
        # hover
        self.scelta = color_hover(
            font_text, "1. You pack up for the journey and leave", "scelta", "Black", pink, blue, self.mouse
        )

        # schermata
        screen.blit(self.story, self.story_rect)
        screen.blit(self.scelta, self.scelta_rect)

# * Screen 3
class State3:
    def __init__(self, font_text, pink, game_state, selected_class):
        self.game_state = "s3"
        self.selected_class = selected_class
        self.mouse = None

        # testo
        self.cl = None
        if self.selected_class == "knight":
            self.cl = "sword and shield"
        elif self.selected_class == "adv":
            self.cl = "bow and arrows"
        elif self.selected_class == "wiz":
            self.cl = "spell book"

        self.story_text = (f"Haste is the best choice! You pick up your {self.cl} and venture to the enemy kingdom. Along the way your neighbour stops you and tells you: <They left not a long time ago and went into the forest, if you're quick enough you might be able to catch up!> You run into the woods, but you have no idea where you are supposed to go from there.")

        self.story, self.story_rect = paragraph(self.story_text, 550, 350, (350, 220), font_text, pink, "Black", 0, 4)

        # scelta 1
        self.scelta, self.scelta_rect = simple_text(font_text, "1. East, towards the nearest inn", pink, (350, 360)
        )

        # scelta 2
        self.scelta2, self.scelta2_rect = simple_text(font_text, "2. North west, straight towards the enemy kingdom", pink, (350, 395)
        )

    # funzioni
    def choice_hover(self, event):
        self.mouse = choice_hover_ex(event, self.scelta_rect, self.scelta2_rect, self.mouse)
    
    def path(self, event):
        self.state_a = "s4"
        self.state_b = "s5"
        self.game_state = choice(event, self.scelta_rect, self.scelta2_rect, self.game_state, self.state_a, self.state_b)
        return self.game_state
    
    def draw(self, screen, font_text, pink, blue):
        # hover
        self.scelta = color_hover(
            font_text, "1. East, towards the nearest inn", "scelta", "Black", pink, blue, self.mouse
        )
        self.scelta2 = color_hover(
            font_text, "2. North west, straight towards the enemy kingdom", "scelta2", "Black", pink, blue, self.mouse
        )

        # schermata
        screen.blit(self.story, self.story_rect)
        screen.blit(self.scelta, self.scelta_rect)
        screen.blit(self.scelta2, self.scelta2_rect)

# * Screen 4
class State4:
    def __init__(self, font_text, pink, cat_name, game_state):
        self.game_state = "s4"
        self.cat_name = cat_name
        self.mouse = None

        # testo
        self.story_text = (f"Since night is approaching, you choose to check if the kidnappers stopped by the only inn in the area to rest and have supper. You walk into the building and are met with the delicious smell of salmon soup... wait... you forgot to bring with you the salmon for {self.cat_name}! How could you?! But you have no time to spare and need to catch up with the kidnappers (who are not there).")

        self.story, self.story_rect = paragraph(self.story_text, 550, 350, (350, 220), font_text, pink, "Black", 0, 4)

        # scelta 1
        self.scelta, self.scelta_rect = simple_text(font_text, "1. Screw it, I need to retrieve some salmon!", pink, (350, 360)
        )

        # scelta 2
        self.scelta2, self.scelta2_rect = simple_text(font_text, "2. You ask the inn keeper if someone passed by", pink, (350, 395)
        )

    # funzioni
    def choice_hover(self, event):
        self.mouse = choice_hover_ex(event, self.scelta_rect, self.scelta2_rect, self.mouse)
    
    def path(self, event):
        self.state_a = "e1"
        self.state_b = "s6"
        self.game_state = choice(event, self.scelta_rect, self.scelta2_rect, self.game_state, self.state_a, self.state_b)
        return self.game_state
    
    def draw(self, screen, font_text, pink, blue):
        # hover
        self.scelta = color_hover(
            font_text, "1. Screw it, I need to retrieve some salmon!", "scelta", "Black", pink, blue, self.mouse
        )
        self.scelta2 = color_hover(
            font_text, "2. You ask the inn keeper if someone passed by", "scelta2", "Black", pink, blue, self.mouse
        )

        # schermata
        screen.blit(self.story, self.story_rect)
        screen.blit(self.scelta, self.scelta_rect)
        screen.blit(self.scelta2, self.scelta2_rect)

# * Screen 5
class State5:
    def __init__(self, font_text, pink, cat_name, game_state):
        self.game_state = "s5"
        self.cat_name = cat_name
        self.mouse = None

        # testo
        self.story_text = (f"You have no time to spare, you rush towards the Land of Retrievers and run through the woods all night, determined to save {self.cat_name}. No wild animals dare to approach you out of fear. As morning comes you walk through the gates of the kingdom and find yourself surrounded by people and… dogs. What a nightmare! (... You liar, you love dogs, you just never had the courage to tell {self.cat_name}). You catch a glimpse of a sketchy man with a cage with a cat inside, but no sight of {self.cat_name}.")

        self.story, self.story_rect = paragraph(self.story_text, 550, 350, (350, 220), font_text, pink, "Black", 0, 4)

        # scelta 1
        self.scelta, self.scelta_rect = simple_text(font_text, f"1. You have no time to waste, look for {self.cat_name}", pink, (350, 360)
        )

        # scelta 2
        self.scelta2, self.scelta2_rect = simple_text(font_text, "2. Save that cat!", pink, (350, 395)
        )

    # funzioni
    def choice_hover(self, event):
        self.mouse = choice_hover_ex(event, self.scelta_rect, self.scelta2_rect, self.mouse)
    
    def path(self, event):
        self.state_a = "s7"
        self.state_b = "s8"
        self.game_state = choice(event, self.scelta_rect, self.scelta2_rect, self.game_state, self.state_a, self.state_b)
        return self.game_state
    
    def draw(self, screen, font_text, pink, blue):
        # hover
        self.scelta = color_hover(
            font_text, f"1. You have no time to waste, look for {self.cat_name}", "scelta", "Black", pink, blue, self.mouse
        )
        self.scelta2 = color_hover(
            font_text, "2. Save that cat!", "scelta2", "Black", pink, blue, self.mouse
        )

        # schermata
        screen.blit(self.story, self.story_rect)
        screen.blit(self.scelta, self.scelta_rect)
        screen.blit(self.scelta2, self.scelta2_rect)

# * Screen 6
class State6:
    def __init__(self, font_text, pink, game_state, selected_class):
        self.game_state = "s6"
        self.selected_class = selected_class
        self.mouse = None

        # testo
        self.cl = None
        if self.selected_class == "knight":
            self.cl = "sword and shield"
        elif self.selected_class == "adv":
            self.cl = "menacing bow"
        elif self.selected_class == "wiz":
            self.cl = "spell book"

        self.story_text = (f"The inn keeper, intimidated by your {self.cl}, stutters and tells you that someone stopped by less than half an hour ago and was carrying with them a cat in a cage. Furious with rage you ask them the direction and go...")

        self.story, self.story_rect = paragraph(self.story_text, 550, 350, (350, 220), font_text, pink, "Black", 0, 4)

        # scelta 1
        self.scelta, self.scelta_rect = simple_text(font_text, "1. North west, straight towards the enemy kingdom", pink, (350, 360)
        )

    # funzioni
    def choice_hover(self, event):
        self.mouse = choice_hover_ex_s(event, self.scelta_rect, self.mouse)
    
    def path(self, event):
        self.state_a = "s5"
        self.game_state = choice_s(event, self.scelta_rect, self.game_state, self.state_a)
        return self.game_state
    
    def draw(self, screen, font_text, pink, blue):
        # hover
        self.scelta = color_hover(
            font_text, "1. North west, straight towards the enemy kingdom", "scelta", "Black", pink, blue, self.mouse
        )

        # schermata
        screen.blit(self.story, self.story_rect)
        screen.blit(self.scelta, self.scelta_rect)

# * Screen 7
class State7:
    def __init__(self, font_text, pink, game_state):
        self.game_state = "s7"
        self.mouse = None

        self.story_text = (f"WHAT?! You abandon that poor cat?!")

        self.story, self.story_rect = paragraph(self.story_text, 550, 350, (350, 220), font_text, pink, "Black", 0, 4)

        # scelta 1
        self.scelta, self.scelta_rect = simple_text(font_text, "1. No, you ABSOLUTELY save the cat!", pink, (350, 360)
        )

    # funzioni
    def choice_hover(self, event):
        self.mouse = choice_hover_ex_s(event, self.scelta_rect, self.mouse)
    
    def path(self, event):
        self.state_a = "s8"
        self.game_state = choice_s(event, self.scelta_rect, self.game_state, self.state_a)
        return self.game_state
    
    def draw(self, screen, font_text, pink, blue):
        # hover
        self.scelta = color_hover(
            font_text, "1. No, you ABSOLUTELY save that cat!", "scelta", "Black", pink, blue, self.mouse
        )

        # schermata
        screen.blit(self.story, self.story_rect)
        screen.blit(self.scelta, self.scelta_rect)

# * Screen 8
class State8:
    def __init__(self, font_text, pink, game_state, selected_class, cat_name):
        self.game_state = "s8"
        self.cat_name = cat_name
        self.selected_class = selected_class
        self.mouse = None

        # testo
        self.cl = None
        if self.selected_class == "knight":
            self.cl = "sword"
        elif self.selected_class == "adv":
            self.cl = "bow"
        elif self.selected_class == "wiz":
            self.cl = "spell book"

        self.story_text = (f"You approach the sketchy man who, intimidated by your {self.cl} drops the cage and runs in fear. Nobody seems to care about you and that man. You hear a voice from the cage telling you: <Thank you my saviour! Oh, I recognize you! You are {self.cat_name}'s servant! The one who forgot about the salmon! You must be so worried about them... Bring me back to your house and I will tell you where {self.cat_name} is!>")

        self.story, self.story_rect = paragraph(self.story_text, 550, 350, (350, 220), font_text, pink, "Black", 0, 4)

        # scelta 1
        self.scelta, self.scelta_rect = simple_text(font_text, "1. Well... all right, let's go back.", pink, (350, 360)
        )

        # scelta 2
        self.scelta2, self.scelta2_rect = simple_text(font_text, f"2. No way, you leave and go look for {self.cat_name}", pink, (350, 395)
        )

    # funzioni
    def choice_hover(self, event):
        self.mouse = choice_hover_ex(event, self.scelta_rect, self.scelta2_rect, self.mouse)
    
    def path(self, event):
        self.state_a = "e2"
        self.state_b = "s9"
        self.game_state = choice(event, self.scelta_rect, self.scelta2_rect, self.game_state, self.state_a, self.state_b)
        return self.game_state
    
    def update(self, selected_class, cat_name):
        self.selected_class = selected_class
        self.cat_name = cat_name
    
    def draw(self, screen, font_text, pink, blue):
        # hover
        self.scelta = color_hover(
            font_text, "1. Well... all right, let's go back.", "scelta", "Black", pink, blue, self.mouse
        )
        self.scelta2 = color_hover(
            font_text, f"2. No way, you leave and go look for {self.cat_name}", "scelta2", "Black", pink, blue, self.mouse
        )

        # schermata
        screen.blit(self.story, self.story_rect)
        screen.blit(self.scelta, self.scelta_rect)
        screen.blit(self.scelta2, self.scelta2_rect)

# * Screen 9
class State9:
    def __init__(self, font_text, pink, game_state):
        self.game_state = "s9"
        self.mouse = None

        self.story_text = (f"REALLY?!")

        self.story, self.story_rect = paragraph(self.story_text, 550, 350, (350, 220), font_text, pink, "Black", 0, 4)

        # scelta 1
        self.scelta, self.scelta_rect = simple_text(font_text, "1. No no, I listen to the cat and save her!", pink, (350, 360)
        )

    # funzioni
    def choice_hover(self, event):
        self.mouse = choice_hover_ex_s(event, self.scelta_rect, self.mouse)
    
    def path(self, event):
        self.state_a = "e2"
        self.game_state = choice_s(event, self.scelta_rect, self.game_state, self.state_a)
        return self.game_state
    
    def draw(self, screen, font_text, pink, blue):
        # hover
        self.scelta = color_hover(
            font_text, "1. No no, I listen to the cat and save her", "scelta", "Black", pink, blue, self.mouse
        )

        # schermata
        screen.blit(self.story, self.story_rect)
        screen.blit(self.scelta, self.scelta_rect)

# * Ending 1
class Ending1:
    def __init__(self, font_text, font_title, pink, cat_name, game_state, selected_class):
        self.game_state = "e1"
        self.cat_name = cat_name
        self.selected_class = selected_class
        self.mouse = None

        # titolo
        self.title, self.title_rect = simple_text(font_title, "You got the Salmon Ending!", pink, (350, 70))

        # testo
        self.story_text = (f"You approach the inn keeper and kindly ask them for some salmon, explaining your misadventure. She starts laughing at you and you are enraged: <How dare you!> But she quickly tells you that {self.cat_name}, actually, is in the kitchen eating salmon by themselves because you were so distracted by work that you dared to forget what their favorite food was! You reunite with {self.cat_name} (after they meow at you all of their complaints) and go straight back home. I hope that from now on you will never forget to give them salmon again!")

        self.story, self.story_rect = paragraph(self.story_text, 550, 300, (350, 280), font_text, pink, "Black", 0, 4)

        # bottoni
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
    def draw(self, screen, font_text, pink, blue):
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

# * Ending 2
class Ending2:
    def __init__(self, font_text, font_title, pink, cat_name, game_state, selected_class):
        self.game_state = "e2"
        self.cat_name = cat_name
        self.selected_class = selected_class
        self.mouse = None

        # titolo
        self.title, self.title_rect = simple_text(font_title, "You got the Fluffy Ending!", pink, (350, 70))

        # testo
        self.story_text = (f"It takes you a few hours, but eventually you get home in the evening. The cat (whose name is Miss Fluffy, at least that's what she said) looks at you satisfied and tells you: <Well... {self.cat_name} is actually happily eating salmon at the inn in the woods. They run away from home because you gave them chicken. Maybe next time be more mindful! They will be back soon, don't worry.> A few hours pass and {self.cat_name} is back home complaining about your ineptitude as a servant, while Pizza already went back home to her's (equally incompetent).")

        self.story, self.story_rect = paragraph(self.story_text, 550, 300, (350, 280), font_text, pink, "Black", 0, 4)

        # bottoni
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
            return None
        return self.game_state, self.cat_name, self.selected_class

    # funzioni  
    def draw(self, screen, font_text, pink, blue):
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