import pygame

class Text():
    def __init__(self, screen, text_color, text_antialias, font, font_size):
        self.text_font = pygame.font.Font(font, font_size)
        # Initialize the screen, color, and antialiasing propertie.
        self.screen = screen
        self.text_color = text_color
        self.text_antialias = text_antialias

class Label(Text):
    def __init__(self, screen, text_color=(0,0,0), text_antialias=True, font=None, font_size=100):
        super().__init__(screen, text_color, text_antialias, font, font_size)
    
    # Define a method to write text on the screen.
    def write(self, text, pos, center_w=False, center_h=False):
        # Render the text as a surface using the font and color.
        text_surf = self.text_font.render(str(text), self.text_antialias, self.text_color)
        # Calculate the centering offset if centering is enabled.
        center_width = text_surf.get_width() / 2 if center_w else 0
        center_height = text_surf.get_height() / 2 if center_h else 0
        # Blit the text surface onto the screen at the specified position.
        self.screen.blit(text_surf, (pos[0] - center_width, pos[1] - center_height))
