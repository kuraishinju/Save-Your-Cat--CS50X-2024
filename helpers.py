import pygame

# * funzione testo lungo
class TextRectException:
    def __init__(self, message = None):
        self.message = message
    def __str__(self):
        return self.message

def render_textrect(string, font, rect, text_color, background_color, justification=0, line_spacing=0):
    final_lines = []

    requested_lines = string.splitlines()

    # Create a series of lines that will fit on the provided
    # rectangle.

    for requested_line in requested_lines:
        if font.size(requested_line)[0] > rect.width:
            words = requested_line.split(' ')
            # if any of our words are too long to fit, return.
            for word in words:
                if font.size(word)[0] >= rect.width:
                    raise TextRectException("Word too wide for the rectangle.")
            # Start a new line
            accumulated_line = ""
            for word in words:
                test_line = accumulated_line + word + " "
                # Build the line while the words fit.    
                if font.size(test_line)[0] < rect.width:
                    accumulated_line = test_line 
                else: 
                    final_lines.append(accumulated_line) 
                    accumulated_line = word + " " 
            final_lines.append(accumulated_line)
        else: 
            final_lines.append(requested_line) 

    # Let's try to write the text out on the surface.

    surface = pygame.Surface(rect.size) 
    surface.fill(background_color) 

    accumulated_height = 0 
    for line in final_lines: 
        if accumulated_height + font.size(line)[1] >= rect.height:
            raise TextRectException("Text too tall for the rectangle.")
        if line != "":
            tempsurface = font.render(line, 0, text_color)
            if justification == 0:
                surface.blit(tempsurface, (0, accumulated_height))
            elif justification == 1:
                surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
            elif justification == 2:
                surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
            else:
                raise TextRectException("Invalid justification argument.")
        accumulated_height += font.size(line)[1] + line_spacing

    return surface

# * helpers globali
def simple_text(font, text, color, center_p):
    content = font.render(text, False, color)
    rect = content.get_rect()
    rect.center = center_p
    return content, rect

def paragraph(text, width, height, center_p, font, tcolor, bcolor, just, space): 
    long = text
    rect = pygame.Rect(0, 0, width, height)
    rect.center = center_p
    content = render_textrect(long, font, rect, tcolor, bcolor, justification=just, line_spacing=space)
    return content, rect

# * helpers menu
def selected_hover(font, text, name, black, pink, blue, cl, ms):
    content = font.render(
        text,
        False,
        black if cl == name or ms == name else pink,
        pink if ms == name else blue if cl == name else black
    )
    return content

# TODO
def requirements(selected_class, cat_name):
    # class
    if selected_class not in ["knight", "adv", "wiz"]:
        return False
    # max strlen
    if len(cat_name) > 10:
        return False
    # alphanum
    if not cat_name.isalpha():
        return False