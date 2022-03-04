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
                pygame.image.load(sprites_file_path + 'screens/start/start1.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start2.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start3.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start4.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start5.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start6.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start7.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start8.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start9.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start10.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start11.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start12.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start13.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start14.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start15.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start16.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start17.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start18.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start19.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start20.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'screens/start/start21.png').convert_alpha()
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
        return sprites

