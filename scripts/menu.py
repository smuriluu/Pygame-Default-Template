import pygame
from scripts.text import Label
from scripts.button import Button, Slider

class Menu():
    def __init__(self, game):
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.new_screen()
    
    def new_screen(self):
        # Create a new screen surface with the game's width and height.
        self.menu_screen = pygame.Surface((self.screen.WIDTH, self.screen.HEIGHT))

        # Create text and button objects.
        self.text = Label(self.menu_screen)
        self.button1 = Button(self.menu_screen, pos=(150, 150))
        self.button2 = Button(self.menu_screen, pos=(150, 300), border_radius=20, text_color=(0,0,255), text_hover_color=(255,0,0))
        self.button3 = Button(self.menu_screen, pos=(150, 450), shadow_size=(6,6))
        self.button4 = Button(self.menu_screen, pos=(500, 600), border=2, transparency=-1, text_hover_color=(128,128,128))
        self.button5 = Button(self.menu_screen, pos=(500, 150), border=2, border_radius=20)
        self.button6 = Button(self.menu_screen, pos=(500, 300), border_radius=20, shadow_size=(6,6), border=2)
        self.button7 = Button(self.menu_screen, pos=(500, 450), border_radius=20, shadow_size=(6,6), text_color=(255,255,255), text_hover_color=(255,255,255), button_color=(20,20,20), button_hover_color=(0,0,0), shadow_color=(100,100,100))
        self.button8 = Button(self.menu_screen, pos=(1200, 30), size=(150, 50), text_font_size=50, border_radius=20, shadow_size=(6,6), border=2)
        self.slider = Slider(self.menu_screen, pos=(850, 175), slider_value=self.settings.audio_settings['main_volume'])

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

        # Draw buttons with their respective text.
        self.button1.draw('1600x900')
        self.button2.draw('1280x720')
        self.button3.draw('720x480')
        if self.settings.video_settings['show_fps']:
            status = 'ON'
            self.text.write('FPS: ', (0, 550))
            self.text.write(str(int(self.screen.clock.get_fps())), (170, 550))
        else:
            status = 'OFF'
        self.button4.draw(f'{self.settings.game_texts['show_fps']} - {status}')
        self.button5.draw('English')
        self.button6.draw('Português')
        if self.settings.video_settings['vsync'] == 1:
            status = 'ON'
        else:
            status = 'OFF'
        self.button7.draw(f'VSync - {status}')
        self.text.write(self.settings.game_texts['title'], (int(self.screen.WIDTH/2), 0), center_w=True)
        self.button8.draw(self.settings.game_texts['exit'])
        self.slider.draw_slider()
        self.text.write(self.settings.audio_settings['main_volume'], (850, 100), center_w=True)

    def inputs(self):
        # Handle button clicks.
        if self.button1.click(self.screen.aspect_ratio):
            self.screen.resize_screen(1600, 900, self.settings.video_settings['vsync'])
            self.new_screen()
        if self.button2.click(self.screen.aspect_ratio):
            self.screen.resize_screen(1280, 720, self.settings.video_settings['vsync'])
            self.new_screen()
        if self.button3.click(self.screen.aspect_ratio):
            self.screen.resize_screen(720, 480, self.settings.video_settings['vsync'])
            self.new_screen()
        if self.button4.click(self.screen.aspect_ratio):
            self.settings.set_settings('video', 'show_fps', False) if self.settings.video_settings['show_fps'] else self.settings.set_settings('video', 'show_fps', True)
        if self.button5.click(self.screen.aspect_ratio):
            self.settings.set_settings('language', 'language_set', 'en-US')
        if self.button6.click(self.screen.aspect_ratio):
            self.settings.set_settings('language', 'language_set', 'pt-BR')
        if self.button7.click(self.screen.aspect_ratio):
            self.settings.set_settings('video', 'vsync', 0) if self.settings.video_settings['vsync'] == 1 else self.settings.set_settings('video', 'vsync', 1)
            self.screen.resize_screen(self.settings.video_settings['width'], self.settings.video_settings['height'], self.settings.video_settings['vsync'])
        if self.button8.click(self.screen.aspect_ratio):
            self.game.running = False
        if self.slider.click_slider(self.screen.aspect_ratio):
            self.settings.set_settings('audio', 'main_volume', self.slider.slider_value)
