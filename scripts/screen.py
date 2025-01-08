import pygame

class Screen():
    # Manages the game screen.
    def __init__(self, settings):
        self.settings = settings
        # Set default screen width and height.
        self.WIDTH = 1280
        self.HEIGHT = 720
        # Set the screen using the video settings from the Settings class.
        self.set_screen(self.settings.video_settings['width'], self.settings.video_settings['height'], self.settings.video_settings['vsync'])
        self.clock = pygame.time.Clock()

    def set_screen(self, width, height, vsync):
        self.display_surf = pygame.display.set_mode((width, height), vsync=vsync)
        # Calculate the width and height ratios to scale the screen.
        self.width_ratio = width / self.WIDTH
        self.height_ratio = height / self.HEIGHT
        self.aspect_ratio = (self.width_ratio, self.height_ratio)
        pygame.display.set_caption('Pygame Default Template')
    
    def scale_screen(self, screen):
        # Scale the screen surface to fit the display surface.
        pygame.transform.scale(screen, self.display_surf.get_size(), self.display_surf)
    
    def resize_screen(self, width, height, vsync):
        # Update the video settings in the Settings class.
        self.settings.set_settings('video', 'width', width)
        self.settings.set_settings('video', 'height', height)
        self.settings.set_settings('video', 'vsync', vsync)
        # Quit the current display and set up a new one with the updated settings.
        pygame.display.quit()
        self.set_screen(width, height, vsync)
    
    def delta_time(self):
        # Get the time since the last frame in milliseconds and convert it to seconds.
        self.dt = self.clock.tick(self.settings.video_settings['fps']) / 1000
    
    def screen_update(self):
        # Update the entire display window.
        pygame.display.update()
