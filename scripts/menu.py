import pygame
from scripts.text import Label

class Menu():
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.new_screen()
    
    def new_screen(self):
        # Create a new screen surface with the game's width and height.
        self.menu_screen = pygame.Surface((self.screen.WIDTH, self.screen.HEIGHT))
        self.text = Label(self.menu_screen)

    def run(self):
        self.events()
        self.update()
        self.draw()
        self.inputs()
    
    def update(self):
        pass

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game.running = False
        
    def draw(self):
        # Scale the screen surface to fit the display surface.
        self.screen.scale_screen(self.menu_screen)
        self.menu_screen.fill((255,255,255))
        self.text.write('Pygame Default Template', (self.settings.video_settings['width']/2, self.settings.video_settings['height']/2), center_w=True, center_h=True)

    def inputs(self):
        pass
