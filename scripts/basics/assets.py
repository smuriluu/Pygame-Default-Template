import pygame
import os

class Assets:
    def __init__(self, path):
        '''
        Initializes the Sprites class, setting up the directory for loading images.

        Parameters:
        - path: The base directory path where the 'images' folder is located.
        '''
        # Set the path to the 'images' directory by joining the base path with 'images'.
        self.images_dir = os.path.join(path, 'images')

    def load_sprite(self):
        '''
        Loads a sprite image from the 'images' directory.

        Functionality:
        - Loads an image file named 'sprite.png' located in the 'images' folder;
        - Uses `pygame.image.load` to load the image;
        - Applies `convert_alpha()` to the loaded image to preserve transparency (useful for PNG images with alpha channels);

        Note:
        - The method assumes that 'sprite.png' exists in the specified directory.
        '''
        # Load the image sprite.png from the images directory.
        # The convert_alpha() method optimizes the image for transparency and faster blitting.
        self.sprite = pygame.image.load(os.path.join(self.images_dir, 'sprite.png')).convert_alpha()
    
    def groups(self):
        '''
        Initializes a pygame sprite group.
        
        Functionality:
        - Creates an empty `pygame.sprite.Group()` to store multiple sprites.
        '''
        self.all_sprites = pygame.sprite.Group()

    def animated_sprites(self, image, frames, matrix, image_size):
        '''
        Extracts animation frames from a sprite sheet.

        Parameters:
        - image: The sprite sheet image.
        - frames: The total number of frames to extract.
        - matrix: A tuple (rows, columns) defining the sprite sheet grid.
        - image_size: A tuple (width, height) defining the size of each frame.

        Functionality:
        - Iterates through the sprite sheet based on the given matrix.
        - Extracts individual frames using `subsurface()`.
        - Returns a 
        '''
        images_frames = []
        count = 1
        for y in range (matrix[0]):
            for x in range(matrix[1]):
                if count <= frames:
                    images_frames.append(image.subsurface(pygame.Rect(x * image_size[0], y * image_size[1], image_size[0], image_size[1])))
                    count += 1
        return images_frames
