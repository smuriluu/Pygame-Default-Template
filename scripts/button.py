import pygame
from scripts.text import TextButton

class Button(TextButton):
    def __init__(self, screen, pos, size=(300, 100), text_color=(0,0,0), text_hover_color=(0,0,0), text_antialias=True, text_font=None, text_font_size=100, button_color=(128,128,128), button_hover_color=(100,100,100), shadow_size=(0,0), shadow_color=(0,0,0), border=-1, border_color=(0,0,0), border_radius=0, transparency=0):
        super().__init__(screen, text_color, text_antialias, text_font, text_font_size)
        self.screen = screen
        self.pos = pos

        # Create the button rect.
        self.button_rect = pygame.Rect(0, 0, size[0], size[1])
        self.button_rect.center = (pos[0], pos[1])
        self.button_x = self.button_rect.x
        self.button_y = self.button_rect.y
        self.button_color = button_color
        self.current_button_color = button_color

        # Create the shadown rect.
        self.shadow_rect = pygame.Rect(0,0,size[0], size[1])
        self.shadow_rect.center = (pos[0]+shadow_size[0], pos[1]+shadow_size[1])
        self.shadow_size = shadow_size
        self.shadow_color = shadow_color

        # Border
        self.border = border # Border=-1: OFF / Border>1: ON
        self.border_color = border_color
        self.border_radius = border_radius

        self.button_hover_color = button_hover_color
        self.text_hover_color = text_hover_color
        self.text_current_color = self.text_color
        self.transparency = transparency # Transparency=0: OFF / Transparency=-1: ON
        self.pressed = False
        
    def draw(self, text):
        # Draw Shadow
        pygame.draw.rect(self.screen, self.shadow_color, self.shadow_rect, border_radius=self.border_radius, width=self.transparency)
        # Draw Buttom
        pygame.draw.rect(self.screen, self.current_button_color, self.button_rect, border_radius=self.border_radius, width=self.transparency)
        # Draw border
        pygame.draw.rect(self.screen, self.border_color, self.button_rect, border_radius=self.border_radius, width=self.border)
        # Write the specified text at the center of the rectangle, with the width of the rectangle as the maximum width.
        self.write(text, (self.button_rect.centerx, self.button_rect.centery), self.button_rect.width, center=True)
    
    def click(self, aspect_ratio):
        mouse_pos = pygame.mouse.get_pos()
        # Update the rectangle's position and size based on the aspect ratio.
        updated_rect = pygame.Rect(self.button_x*aspect_ratio[0], self.button_y*aspect_ratio[1], self.button_rect.width*aspect_ratio[0], self.button_rect.height*aspect_ratio[1])
        # Check if the mouse is within the updated rectangle.
        if updated_rect.collidepoint(mouse_pos):
            self.current_button_color = self.button_hover_color
            self.text_color = self.text_hover_color
            # If the left mouse button is pressed.
            if pygame.mouse.get_pressed()[0]:
                self.button_rect.center = (self.pos[0]+self.shadow_size[0], self.pos[1]+self.shadow_size[1])
                self.pressed = True
            else:
                # If the pressed flag is True, it means the button was just released.
                if self.pressed:
                    self.button_rect.center = (self.pos[0], self.pos[1])
                    self.pressed = False
                    # Return to indicate a click.
                    return True
        else:
            self.button_rect.center = (self.pos[0], self.pos[1])
            self.current_button_color = self.button_color
            self.text_color = self.text_current_color
            self.pressed = False
            return False

class Slider(Button):
    def __init__(self, screen, pos, slider_value, size=(300, 30), multiplier=1, button_color = (100,100,100), button_hover_color = (100,100,100), border_radius = 20, padding = 20, pointer_radius = 8, smooth=True):
        '''
        Initializes the Slider object, which inherits from the Button class.

        Parameters:
        - screen: The Pygame screen to draw the slider on;
        - pos: Tuple containing the x and y position of the slider;
        - slider_value: Initial value of the slider (0 to 100);
        - size: Size of the slider as a tuple (width, height). Default is (300, 30);
        - multiplier: Multiplier for scaling the slider's value. Default is 1;
        - button_color: Color of the slider's button area. Default is (100, 100, 100);
        - button_hover_color: Hover color for the slider's button. Default is (100, 100, 100);
        - border_radius: Radius for the slider's button corners. Default is 20;
        - padding: Padding on the left and right sides of the slider. Default is 20;
        - pointer_radius: Radius of the slider pointer. Default is 8;
        - smooth: Boolean to determine if the slider moves smoothly or in discrete steps. Default is True.
        '''
        super().__init__(screen, pos, size, button_color=button_color, button_hover_color=button_hover_color, border_radius=border_radius)
        # Space on either side of the slider line.
        self.padding = padding
        # Size of the pointer (circle).
        self.pointer_radius = pointer_radius
        # Scaling factor for slider values.
        self.multiplier = multiplier
        # Determines smooth or discrete pointer movement.
        self.smooth = smooth
        # Calculate the initial pointer position based on the slider value.
        self.pointer_pos = int(((self.button_rect.width - self.padding*2) * slider_value / 100) / multiplier) + self.padding

    def draw_slider(self):
        '''
        Draws the slider on the screen.

        Draws the button using the parent draw method;
        Draws a horizontal line for the slider's track;
        Draws a circular pointer to represent the current slider value.
        '''
        # Draw the slider's button
        self.draw('')
        # Line width for the slider track.
        pygame.draw.line(self.screen, (0,0,0), (self.button_x + self.padding, self.button_y+self.button_rect.height/2), (self.button_rect.width - self.padding + self.button_x, self.button_rect.height/2 + self.button_y), width=2)
        # Draw the slider pointer as a circle
        pygame.draw.circle(self.screen, (0,0,0), (self.button_x + self.pointer_pos, self.button_y+self.button_rect.height/2), radius=self.pointer_radius)
    
    def click_slider(self, aspect_ratio):
        '''
        Handles mouse interaction with the slider.

        Parameters:
        - aspect_ratio: A tuple (x_scale, y_scale) to adjust for screen resizing.

        Returns:
        - True if the slider was clicked and value was updated;
        - False otherwise.
        '''
        # Get the current mouse position.
        mouse_pos = pygame.mouse.get_pos()
        # Adjust the slider's clickable area based on the aspect ratio.
        updated_rect = pygame.Rect((self.button_x + self.padding)*aspect_ratio[0], self.button_y*aspect_ratio[1], (self.button_rect.width-self.padding*2)*aspect_ratio[0], self.button_rect.height*aspect_ratio[1])
        # Check if the mouse is within the slider's clickable area.
        if updated_rect.collidepoint(mouse_pos):
            # Check if the left mouse button is pressed.
            if pygame.mouse.get_pressed()[0]:
                # Update the pointer position relative to the mouse.
                self.pointer_pos =  mouse_pos[0] - updated_rect.x
                # Calculate the slider value based on the pointer's position.
                self.slider_value = round((self.pointer_pos*100/updated_rect.width)*self.multiplier)
                if self.smooth:
                    # Smooth pointer movement.
                    self.pointer_pos = (self.pointer_pos + self.padding) / aspect_ratio[0]
                else:
                    # Discrete pointer movement.
                    self.pointer_pos = int(((self.button_rect.width - self.padding*2) * self.slider_value / 100) / self.multiplier) + self.padding
                # Slider value was updated.
                return True
        # Slider was not clicked or updated.
        return False
