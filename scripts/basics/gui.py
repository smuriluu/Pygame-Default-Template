import pygame

class Text:
    def __init__(self, screen, text_color, text_antialias, text_font, text_font_size):
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
        self.text_font = pygame.font.Font(text_font, text_font_size)
        # Store screen, text color, and antialiasing properties.
        self.screen = screen
        self.text_color = text_color
        self.text_antialias = text_antialias

class Label(Text):
    def __init__(self, screen, text_color=(0,0,0), text_antialias=True, font=None, font_size=100, border_radius=0, border_color=(0,0,0), border_width=-1, border_padding=0):
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
        self.border_radius = border_radius
        self.border_color = border_color
        self.border_width = border_width
        self.border_padding = border_padding
    
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
        text_rect = text_surf.get_rect(topleft=(pos[0] - center_width, pos[1] - center_height))
        # Blit the text surface onto the screen at the adjusted position.
        self.screen.blit(text_surf, (pos[0] - center_width, pos[1] - center_height))
        pygame.draw.rect(self.screen, self.border_color, text_rect.inflate(self.border_padding, -self.border_padding).move(0, -self.border_padding/1.5), self.border_width, self.border_radius)

class TextButton(Text):
    def __init__(self, screen, text_color, text_antialias, text_font, text_font_size):
        '''
        Initializes a TextButton object, inheriting from Text.

        Parameters:
        - screen: The Pygame screen where the button text will be rendered;
        - text_color: Color of the text;
        - text_antialias: Boolean to enable or disable antialiasing;
        - font: Path to the font file or None for the default font;
        - font_size: Size of the font.
        '''
        super().__init__(screen, text_color, text_antialias, text_font, text_font_size)
    
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

class TextBoxText(Text):
    def __init__(self, screen, text_color, text_antialias, font, font_size):
        super().__init__(screen, text_color, text_antialias, font, font_size)
        self.text_surf = self.text_font.render('', self.text_antialias, self.text_color)
    
    def write(self, text, pos, offset, text_box_size, padding, center_h=True):
        self.text_surf = self.text_font.render(text, self.text_antialias, self.text_color)
        center_height = text_box_size[1]/3 if center_h else 0
        clip_surface = pygame.Surface(((text_box_size[0]-(padding*2)), text_box_size[1]), pygame.SRCALPHA)
        clip_surface.fill((0,0,0,0))
        clip_surface.blit(self.text_surf, (-offset, 0))
        self.screen.blit(clip_surface, ((pos[0]+padding), pos[1]+center_height))

class ElementsAttributes: # Graphical User Interface Basic Attributes
    def __init__(self,
                screen,
                aspect_ratio,
                pos,
                size=(100,100),
                visible=True,
                text_color=(0,0,0),
                text_hover_color=(0,0,0),
                text_antialias=True,
                text_font=None,
                text_font_size=100,
                box_color=(128,128,128),
                box_hover_color=(100,100,100),
                box_transparency=0,
                box_border_radius=0,
                shadow=False,
                shadow_size=(10,10),
                shadow_color=(0,0,0),
                border=False,
                border_thickness=1,
                border_color=(0,0,0),
                **kwargs):
        self.screen = screen
        self.aspect_ratio = aspect_ratio
        self.pos = pos
        self.size = size
        self.visible = visible
        self.text_color = text_color
        self.text_current_color = text_color
        self.text_hover_color = text_hover_color
        self.text_antialias = text_antialias
        self.text_font = text_font
        self.text_font_size = text_font_size
        self.box_color = box_color
        self.box_current_color = box_color
        self.box_hover_color = box_hover_color
        self.box_transparency = box_transparency
        self.box_border_radius = box_border_radius
        self.shadow = shadow
        self.shadow_size = shadow_size
        self.shadow_color = shadow_color
        self.border = border
        self.border_thickness = border_thickness
        self.border_color = border_color

        self.box_rect = pygame.Rect(0, 0, size[0], size[1])
        self.box_rect.center = (pos[0], pos[1])

        self.shadow_rect = pygame.Rect(0, 0, size[0], size[1])
        self.shadow_rect.center = (pos[0] + shadow_size[0], pos[1] + shadow_size[1])

        super().__init__(**kwargs)

class Button(ElementsAttributes):
    def __init__(self,
                 screen,
                 aspect_ratio,
                 pos,
                 size=(300, 100),
                 text_color=(0,0,0),
                 text_hover_color=(0,0,0),
                 visible=True,
                 text_antialias=True,
                 text_font=None,
                 text_font_size=100,
                 box_color=(128,128,128),
                 box_hover_color=(100,100,100),
                 box_border_radius=0,
                 shadow=False,
                 shadow_size=(0,0),
                 shadow_color=(0,0,0),
                 border=False,
                 border_thickness=1,
                 border_color=(0,0,0),
                 box_transparency=0):
        '''
        Initializes the Button object, which inherits from the TextButton class.
        '''
        super().__init__(screen=screen,
                         aspect_ratio=aspect_ratio,
                         pos=pos,
                         size=size,
                         visible=visible,
                         text_color=text_color,
                         text_hover_color=text_hover_color,
                         text_antialias=text_antialias,
                         text_font=text_font,
                         text_font_size=text_font_size,
                         box_color=box_color,
                         box_hover_color=box_hover_color,
                         box_border_radius=box_border_radius,
                         box_transparency=box_transparency,
                         shadow=shadow,
                         shadow_size=shadow_size,
                         shadow_color=shadow_color,
                         border=border,
                         border_thickness=border_thickness,
                         border_color=border_color)
        # Tracks whether the button is currently pressed.
        self.text = TextButton(screen, text_color, text_antialias, text_font, text_font_size)
        self.pressed = False
        
    def draw_button(self, text):
        '''
        Draws the button on the screen.

        Parameters:
        - text: Text to display on the button.
        '''
        if self.visible:
            # Draw the shadow (background).
            if self.shadow:
                pygame.draw.rect(self.screen, self.shadow_color, self.shadow_rect, border_radius=self.box_border_radius, width=self.box_transparency)
            # Draw the button (main rectangle).
            pygame.draw.rect(self.screen, self.box_current_color, self.box_rect, border_radius=self.box_border_radius, width=self.box_transparency)
            # Draw the border, if enabled.
            if self.border:
                pygame.draw.rect(self.screen, self.border_color, self.box_rect, border_radius=self.box_border_radius, width=self.border_thickness)
            # Draw the text at the center of the button.
            self.text.write(text, (self.box_rect.centerx, self.box_rect.centery), self.box_rect.width)
    
    def click_button(self) -> bool:
        '''
        Handles mouse interaction with the button.

        Returns:
        - True if the button was clicked, False otherwise.
        '''
        if self.visible:
            # Get the current mouse position.
            mouse_pos = pygame.mouse.get_pos()
            # Adjust the button's clickable area based on the aspect ratio.
            updated_rect = pygame.Rect(self.box_rect.x * self.aspect_ratio[0], self.box_rect.y * self.aspect_ratio[1], self.box_rect.width * self.aspect_ratio[0], self.box_rect.height * self.aspect_ratio[1])
            # Check if the mouse is within the updated rectangle.
            if updated_rect.collidepoint(mouse_pos):
                # Change the button and text color for hover state.
                self.box_current_color = self.box_hover_color
                self.text_color = self.text_hover_color
                
                # Check if the left mouse button is pressed.
                if pygame.mouse.get_pressed()[0]:
                    # Move the button slightly to simulate a press (with shadow offset).
                    self.box_rect.center = (self.pos[0] + self.shadow_size[0], self.pos[1] + self.shadow_size[1])
                    self.pressed = True
                else:
                    # If the button was pressed and is now released, register a click.
                    if self.pressed:
                        # Reset button position.
                        self.box_rect.center = (self.pos[0], self.pos[1])
                        self.pressed = False
                        # Button click registered.
                        return True
            else:
                # Reset button state if the mouse is not over it.
                self.box_rect.center = (self.pos[0], self.pos[1])
                self.box_current_color = self.box_color
                self.text_color = self.text_current_color
                self.burron_pressed = False
                # Button was not clicked.
                return False
        else:
            return False

class Slider(ElementsAttributes):
    def __init__(self,
                 screen,
                 aspect_ratio,
                 pos,
                 slider_value,
                 slider_padding = 20,
                 slider_pointer_radius = 8,
                 slider_multiplier=1,
                 slider_line=True,
                 slider_line_thickness=2,
                 size=(300, 30),
                 visible = True,
                 box_color = (100,100,100),
                 box_hover_color = (100,100,100),
                 box_border_radius = 20,
                 shadow_size=(0,0),
                 shadow=False,
                 shadow_color=(0,0,0),
                 box_transparency=0):
        '''
        Initializes the Slider object, which inherits from the Button class.
        '''
        super().__init__(screen,
                         aspect_ratio,
                         pos, size,
                         visible,
                         box_color=box_color,
                         box_hover_color=box_hover_color,
                         box_border_radius=box_border_radius,
                         shadow=shadow,
                         shadow_size=shadow_size,
                         shadow_color=shadow_color,
                         box_transparency=box_transparency)
        # Space on either side of the slider line.
        self.slider_padding = slider_padding
        # Size of the pointer (circle).
        self.slider_pointer_radius = slider_pointer_radius
        # Scaling factor for slider values.
        self.slider_multiplier = slider_multiplier
        # Calculate the initial pointer position based on the slider value.
        self.slider_pointer_pos = int(((self.box_rect.width - slider_padding * 2) * slider_value / 100) / slider_multiplier) + self.slider_padding
        self.slider_line = slider_line
        self.slider_line_thickness = slider_line_thickness

    def draw_slider(self):
        '''
        Draws the slider on the screen.

        Draws the button using the parent draw method;
        Draws a horizontal line for the slider's track;
        Draws a circular pointer to represent the current slider value.
        '''
        if self.visible:
            # Draw the shadow (background).
            if self.shadow:
                pygame.draw.rect(self.screen, self.shadow_color, self.shadow_rect, border_radius=self.box_border_radius, width=self.box_transparency)
            # Draw the button (main rectangle).
            pygame.draw.rect(self.screen, self.box_current_color, self.box_rect, border_radius=self.box_border_radius, width=self.box_transparency)
            # Draw the border, if enabled.
            if self.border:
                pygame.draw.rect(self.screen, self.border_color, self.box_rect, border_radius=self.box_border_radius, width=self.border_thickness)
            # Line width for the slider track.
            if self.slider_line:
                pygame.draw.line(self.screen, (0,0,0), (self.box_rect.x + self.slider_padding, self.box_rect.y+self.box_rect.height/2), (self.box_rect.width - self.slider_padding + self.box_rect.x, self.box_rect.height/2 + self.box_rect.y), width=self.slider_line_thickness)
            # Draw the slider pointer as a circle
            pygame.draw.circle(self.screen, (0,0,0), (self.box_rect.x + self.slider_pointer_pos, self.box_rect.y+self.box_rect.height/2), radius=self.slider_pointer_radius)
    
    def click_slider(self):
        '''
        Handles mouse interaction with the slider.

        Returns:
        - True if the slider was clicked and value was updated;
        - False otherwise.
        '''
        # Get the current mouse position.
        mouse_pos = pygame.mouse.get_pos()
        # Adjust the slider's clickable area based on the aspect ratio.
        updated_rect = pygame.Rect((self.box_rect.x + self.slider_padding) * self.aspect_ratio[0], self.box_rect.y * self.aspect_ratio[1], (self.box_rect.width-self.slider_padding * 2) * self.aspect_ratio[0], self.box_rect.height * self.aspect_ratio[1])
        # Check if the mouse is within the slider's clickable area.
        if updated_rect.collidepoint(mouse_pos):
            # Check if the left mouse button is pressed.
            if pygame.mouse.get_pressed()[0]:
                # Update the pointer position relative to the mouse.
                self.slider_pointer_pos =  mouse_pos[0] - updated_rect.x
                # Calculate the slider value based on the pointer's position.
                self.slider_value = round((self.slider_pointer_pos*100/updated_rect.width)*self.slider_multiplier)
                self.slider_pointer_pos = int(((self.box_rect.width - self.slider_padding*2) * self.slider_value / 100) / self.slider_multiplier) + self.slider_padding
                # Slider value was updated.
                return True
        # Slider was not clicked or updated.
        return False

class TextBox(ElementsAttributes):
    def __init__(self,
                 screen,
                 aspect_ratio,
                 pos,
                 size=(300, 100),
                 visible=True,
                 display_text='',
                 text_padding=10,
                 password=False,
                 text_color=(0,0,0),
                 display_text_color=(0,0,0),
                 text_antialias=True,
                 text_font=None,
                 text_font_size=40,
                 box_color=(128,128,128),
                 border=True,
                 border_thickness=1,
                 border_color=(0,0,0),
                 box_border_radius=0,
                 box_transparency=0):
        super().__init__(screen=screen,
                         aspect_ratio=aspect_ratio,
                         pos=pos,
                         size=size,
                         visible=visible,
                         text_color=text_color,
                         text_antialias=text_antialias,
                         text_font=text_font,
                         text_font_size=text_font_size,
                         box_color=box_color,
                         border=border,
                         border_color=border_color,
                         border_thickness=border_thickness,
                         box_border_radius=box_border_radius,
                         box_transparency=box_transparency)
        self.text = TextBoxText(screen, text_color, text_antialias, text_font, text_font_size)
        # Text input by the user
        self.text_input = ''
        self.text_padding = text_padding
        self.pressed = False
        # Offset for text if it overflows the text box
        self.offset = 0
        # Whether the text box should hide input (password)
        self.password = password
        self.display_text = display_text
        self.display_text_label = Label(screen, font_size=text_font_size, font=text_font, text_color=display_text_color)
        self.bar_text_label = Label(screen, font_size=text_font_size, font=text_font)
        self.text_padding = text_padding
        
    def draw(self):
        '''
        Draws the text box on the screen.

        Draws the text box background with a potential border, 
        then renders the user input (text or masked if password) inside it.
        '''
        if self.visible:
            # Draw the text box background and border
            pygame.draw.rect(self.screen, self.box_color, self.box_rect, border_radius=self.box_border_radius, width=self.box_transparency)
            pygame.draw.rect(self.screen, self.border_color, self.box_rect, border_radius=self.box_border_radius, width=self.border_thickness)
            # Adjust text offset if it overflows the text box width
            if self.text.text_surf.get_width() > self.box_rect.width - self.text_padding * 2:
                self.offset = self.text.text_surf.get_width() - (self.box_rect.width - self.text_padding * 2)
            else:
                self.offset = 0
        
            # If the text box is set to password mode, display '*' for each character typed
            if self.password:
                self.text.write(f'{'*'*len(self.text)}', (self.box_rect.x, self.box_rect.y), self.offset, (self.box_rect.width, self.box_rect.height), self.text_padding)
            else:
                # Otherwise, display the actual user text
                self.text.write(self.text_input, (self.box_rect.x, self.box_rect.y), self.offset, (self.box_rect.width, self.box_rect.height), self.text_padding)
            
            # Blinking logic
            if self.text_input == '':
                self.display_text_label.write(self.display_text, (self.box_rect.x+self.text_padding, self.box_rect.y + self.box_rect.height/3))
            if self.pressed:
                self.blink_time = pygame.time.get_ticks() - self.start_blink
                if self.blink_time <= 1000:
                    self.bar_text_label.write('|', ((self.box_rect.x+self.text.text_surf.get_width()+self.text_padding/2) - self.offset, self.box_rect.y + self.box_rect.height/2), center_h=True)
                elif (self.blink_time//1000) % 2 == 0:
                    self.bar_text_label.write('|', ((self.box_rect.x+self.text.text_surf.get_width()+self.text_padding/2) - self.offset, self.box_rect.y + self.box_rect.height/2), center_h=True)
            else:
                self.start_blink = pygame.time.get_ticks()
    
    def click(self):
        '''
        Handles mouse interaction with the text box.

        Returns:
        - True if the text box was clicked;
        - False otherwise.
        '''
        if self.visible:
            # Get the current mouse position
            mouse_pos = pygame.mouse.get_pos()
            # Adjust the text box rectangle for different screen aspect ratios
            updated_rect = pygame.Rect(self.box_rect.x*self.aspect_ratio[0], self.box_rect.y*self.aspect_ratio[1], self.box_rect.width*self.aspect_ratio[0], self.box_rect.height*self.aspect_ratio[1])
            # If the mouse click is within the text box, set the 'pressed' flag to True
            if updated_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed()[0]:
                self.pressed = True
            elif pygame.mouse.get_pressed()[0]:
                # If mouse is released outside, set the 'pressed' flag to False
                self.pressed = False
    
    def event(self, event):
        '''
        Handles keyboard events to capture user input when the text box is clicked.

        Parameters:
        - event: The Pygame event object that contains the keyboard input.

        Updates the user text based on key events (backspace, typing, etc.).
        '''
        # If the text box is pressed, process key events
        if self.pressed:
            if event.type == pygame.KEYDOWN:
                # Handle backspace key to delete last character
                if event.key == pygame.K_BACKSPACE:
                    self.text_input = self.text_input[:-1]
                # Handle enter key to submit (currently does nothing)
                elif event.key == pygame.K_RETURN:
                    pass
                else:
                    # Add the character pressed to the user text
                    self.text_input += event.unicode

class Panel():
    def __init__(self, screen, aspect_ratio, pos, size=(100,100), color=(128,128,128)):
        self.screen = screen
        self.aspect_ratio = aspect_ratio
        self.pos = pygame.math.Vector2(pos[0], pos[1])
        self.velocity = pygame.math.Vector2(0, 0)
        self.acceleration = pygame.math.Vector2(0, 0)
        self.color = color
        self.panel_surf = pygame.Surface((size[0], size[1]), pygame.SRCALPHA)
        self.acc = -10
    
    def draw(self):
        self.panel_surf.fill(self.color)
        self.screen.blit(self.panel_surf, self.pos)
    
    def update(self, dt):
        self.acceleration.x += self.acc * dt
        self.velocity += self.acceleration * dt
        self.pos += self.velocity * dt
