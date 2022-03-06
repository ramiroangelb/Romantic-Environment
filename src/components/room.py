import pygame
from src.components.cursor import Cursor
from src.components.tile import Tile
from src.components.room_object import RoomObject

class Room:
    
    def __init__(self, surface, tiles, sprites):
        #Room layout:
        room_layout = [
            'WDWWWWWWWWW',
            'WWWWWWWWWWW',
            'WWWWWWWMWWW',
            'WWWWWWWWWWW',
            'P----------',
            '-----C-----',
            '--T--T--T--',
            '-----E-----',
            '-----------',
            '-----------',
            '-----------'
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
        #Food
        self.food_cord1_left = (0,0)
        self.food_cord2_left = (0,0)
        self.food_cord1_center = (0,0)
        self.food_cord2_center = (0,0)
        self.food_cord1_right = (0,0)
        self.food_cord2_right = (0,0)
        #Cursor
        self.clickeable_list = []
        self.table = None
        self.__create_room()

    def __create_room(self):

        self.tiles_group = pygame.sprite.Group()
        self.sprites_group = pygame.sprite.Group()
        self.enemies_group = pygame.sprite.Group()
        for row_index, row in enumerate(self.layout):
            for celd_index, celd in enumerate(row):
                x = celd_index * self.tile_size
                y = row_index * self.tile_size
                if celd == 'W':
                    tile = Tile((x, y), self.tile_list, 1)
                    self.tiles_group.add(tile)
                else:
                    tile = Tile((x, y), self.tile_list, 0)
                    self.tiles_group.add(tile)
                    if celd == 'T':
                        obj = RoomObject((x, y), self.sprite_dict, 'table')
                        self.sprites_group.add(obj)
                        self.clickeable_list.append(obj)
                        self.table = obj
                    elif celd == 'C':
                        she = RoomObject((x,y), self.sprite_dict, 'she')
                        self.sprites_group.add(she)
                        self.clickeable_list.append(she)
                    elif celd == 'E':
                        him = RoomObject((x,y), self.sprite_dict, 'him')
                        self.sprites_group.add(him)
                        self.clickeable_list.append(him)
                    elif celd == 'P':
                        obj = RoomObject((x, y - 16), self.sprite_dict, 'plant')
                        self.sprites_group.add(obj)
                    elif celd == 'M':
                        obj = RoomObject((x, y), self.sprite_dict, 'mercader_wall')
                        self.sprites_group.add(obj)
                    elif celd == 'D':
                        tile = Tile((x, y), self.tile_list, 1)
                        self.tiles_group.add(tile)
                        obj = RoomObject((x, y), self.sprite_dict, 'three_dog')
                        self.sprites_group.add(obj)
        
        self.cursor = Cursor((50,50), self.sprite_dict, self.clickeable_list)
        self.sprites_group.add(self.cursor)



    def draw(self):
        ##Add update method for animated tiles?
        #Tiles
        self.display_surface.fill('white')
        self.tiles_group.update()
        self.tiles_group.draw(self.display_surface)
        self.sprites_group.update()
        self.sprites_group.draw(self.display_surface)
        pygame.draw.rect(pygame.display.get_surface(), 'white', self.table, 2)