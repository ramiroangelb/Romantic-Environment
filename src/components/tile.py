import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, tile_list, index):
        super().__init__()
        self.tiles = tile_list
        self.image = self.tiles[index]
        self.rect = self.image.get_rect(topleft = pos)

    def get_rect(self):
        return self.rect