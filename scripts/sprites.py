import pygame
import os

class Sprites:
    def __init__(self, path):
        # Set the images directory path by joining the provided path with 'images'.
        self.images_dir = os.path.join(path, 'images')
    
    # Load Sprite Example:
    def load_sprite(self):
        # Load a sprite image from the images directory using pygame's image load function.
        # The convert_alpha method is used to preserve the transparency of the image.
        self.sprite = pygame.image.load(os.path.join(self.images_dir, 'sprite.png')).convert_alpha()
