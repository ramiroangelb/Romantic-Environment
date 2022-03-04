import pygame
from src.components.tiles import Tile
#from src.components.player import Player

class Room:
    
    def __init__(self, surface, tiles, sprites):
        #Room layout:
        room_layout = [
            '------------',
            '------------',
            '------------',
            '------------',
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
        self.__create_room()

    def __create_room(self):
        pass


    def draw(self):
        ##Add update method for animated tiles?
        #Tiles
        self.display_surface.fill('black')
        self.tiles_group.update()
        self.tiles_group.draw(self.display_surface)
        self.player_group.update()
        self.player_group.draw(self.display_surface)