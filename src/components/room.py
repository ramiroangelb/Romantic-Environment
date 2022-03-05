import pygame
from src.components.tiles import Tile
#from src.components.player import Player

class Room:
    
    def __init__(self, surface, tiles, sprites):
        #Room layout:
        room_layout = [
            '------------',
            '----T-------',
            '--------T---',
            '--T---------',
            '------------'
        ]
        #Display
        self.display_surface = surface
        #Tiles
        self.tile_list = tiles.get_tiles_dict()['room']
        self.tile_size = tiles.tile_size
        #Sprites
        self.sprite_dict = sprites.get_sprites_dict()
        #Enemies
        self.enemies = []
        #Level
        self.layout = room_layout
        self.__create_room()

    def __create_room(self):
        self.tiles_group = pygame.sprite.Group()
        self.sprites_group = pygame.sprite.Group()
        self.enemies_group = pygame.sprite.Group()
        for row_index, row in enumerate(self.layout):
            for celd_index, celd in enumerate(row):
                if celd != '-':
                    x = celd_index * self.tile_size
                    y = row_index * self.tile_size
                    if celd == 'T':
                        



    def draw(self):
        ##Add update method for animated tiles?
        #Tiles
        self.display_surface.fill('black')
        self.tiles_group.update()
        self.tiles_group.draw(self.display_surface)
        self.player_group.update()
        self.player_group.draw(self.display_surface)