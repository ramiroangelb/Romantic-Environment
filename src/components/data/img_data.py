from xml.etree.ElementTree import tostring
import pygame

class TilesSource:
    def __init__(self):
        self.tiles_dict = self.__load_tiles('src/assets/tiles/')
        self.tile_size = 16
    
    def get_tiles_dict(self):
        return self.tiles_dict

    def __load_tiles(self, tiles_file_path):
        tiles = {
            'room': [
                [pygame.image.load(tiles_file_path + 'floor.png').convert_alpha()],
                [pygame.image.load(tiles_file_path + 'wall.png').convert_alpha()],
                [pygame.image.load(tiles_file_path + 'table.png').convert_alpha()],
            ]
        }
        return tiles

class SpritesSource:
    def __init__(self):
        self.sprites_dict = self.__load_sprites('src/assets/')
    
    def get_sprites_dict(self):
        return self.sprites_dict
    
    def get_object_sprite(self, identifier):
        return self.sprites_dict[identifier]

    def __load_sprites(self, sprites_file_path):
        sprites = {
            'titlecard':[
            ],
            'him': [

            ],
            'she': [

            ],
            'food': [

            ],
            'NPC': [
                
            ]
        }
        self.fill_images_in_order(sprites,'titlecard',sprites_file_path,'screens/start/start', 21)
        return sprites

    def fill_images_in_order(self,dic, key,file_path, path, images): 
        for i in range(images):
            dic[key].append(pygame.image.load(file_path + path + str(i+1) + '.png').convert_alpha())
