import pygame

class Text():
    def __init__(self, screen, text_color, text_antialias, font, font_size):
        '''
        Initializes a Text object for rendering text on the screen.

        Parameters:
        - screen: The Pygame screen where the text will be rendered;
        - text_color: Color of the text (RGB tuple);
        - text_antialias: Boolean to enable or disable antialiasing;
        - font: Path to the font file or None for the default font;
        - font_size: Size of the font.
        '''
        # Create a font object with the specified font and size.
        self.text_font = pygame.font.Font(font, font_size)
        # Store screen, text color, and antialiasing properties.
        self.screen = screen
        self.text_color = text_color
        self.text_antialias = text_antialias

class Label(Text):
    def __init__(self, screen, text_color=(0,0,0), text_antialias=True, font=None, font_size=100):
        '''
        Initializes a Label object, inheriting from Text.

        Parameters:
        - screen: The Pygame screen where the label will be rendered;
        - text_color: Color of the text (default is black);
        - text_antialias: Boolean to enable or disable antialiasing (default is True);
        - font: Path to the font file or None for the default font;
        - font_size: Size of the font (default is 100).
        '''
        super().__init__(screen, text_color, text_antialias, font, font_size)
    
    def write(self, text, pos, center_w=False, center_h=False):
        '''
        Renders and draws text on the screen.

        Parameters:
        - text: The string to be displayed;
        - pos: Tuple (x, y) indicating the position on the screen;
        - center_w: Boolean to center the text horizontally around pos[0];
        - center_h: Boolean to center the text vertically around pos[1].
        '''
        # Render the text as a surface with the specified font, color, and antialiasing.
        text_surf = self.text_font.render(str(text), self.text_antialias, self.text_color)
        # Calculate offsets for centering the text, if enabled.
        center_width = text_surf.get_width() / 2 if center_w else 0
        center_height = text_surf.get_height() / 2 if center_h else 0
        # Blit the text surface onto the screen at the adjusted position.
        self.screen.blit(text_surf, (pos[0] - center_width, pos[1] - center_height))

class TextButton(Text):
    def __init__(self, screen, text_color, text_antialias, font, font_size):
        '''
        Initializes a TextButton object, inheriting from Text.

        Parameters:
        - screen: The Pygame screen where the button text will be rendered;
        - text_color: Color of the text;
        - text_antialias: Boolean to enable or disable antialiasing;
        - font: Path to the font file or None for the default font;
        - font_size: Size of the font.
        '''
        super().__init__(screen, text_color, text_antialias, font, font_size)
    
    def write(self, text, pos, buttom_width, center=True):
        '''
        Renders and draws text on the screen, optionally resizing it to fit within a button.

        Parameters:
        - text: The string to be displayed;
        - pos: Tuple (x, y) indicating the position on the screen;
        - buttom_width: The maximum width allowed for the text (0 for no limit);
        - center: Boolean to center the text both horizontally and vertically around pos;
        '''
        # Render the text as a surface.
        text_surf = self.text_font.render(text, self.text_antialias, self.text_color)
        # If the button's width is smaller than the text's width, scale the text down.
        if buttom_width < text_surf.get_width() and buttom_width != 0:
            # Scale the text surface to fit within the button width (subtracting 20 for padding).
            text_surf = pygame.transform.scale_by(text_surf, (buttom_width-20) / text_surf.get_width())
        # Calculate offsets for centering the text, if enabled.
        center_width = text_surf.get_width() / 2 if center else 0
        center_height = text_surf.get_height() / 2 if center else 0
        # Blit the text surface onto the screen at the adjusted position.
        self.screen.blit(text_surf, (pos[0] - center_width, pos[1] - center_height))
