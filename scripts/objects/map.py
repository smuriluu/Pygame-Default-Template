import pygame
from os.path import join
from pytmx.util_pygame import load_pygame

class Map:
    def __init__(self, game):
        TILE_SIZE = 64
        self.map = load_pygame(join(game.settings.path, '...'))

        for obj in self.map.get_layer_by_name('Objects'):
            CollisionSprite((obj.x, obj.y), obj.image, game.assets.objects_sprites)

        for x, y, img self.map.get_layer_by_name('Ground').tiles():
            Sprite((x * TILE_SIZE, y * TILE_SIZE), img, game.assets.groud_sprites)

class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = pos)

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_frect(center = pos)

