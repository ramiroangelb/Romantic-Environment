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
                pygame.image.load(tiles_file_path + 'floor.png').convert_alpha(),
                pygame.image.load(tiles_file_path + 'wall.png').convert_alpha()
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
            'title':[

            ],
            'him': [

            ],
            'she': [

            ],
            'soup': [

            ],
            'NPC': [
                [],
                [],
                []
            ],
            'table':[
                pygame.image.load(sprites_file_path + 'sprites/room/table.png').convert_alpha()
            ],
            'plant':[
                pygame.image.load(sprites_file_path + 'sprites/room/plant.png').convert_alpha()
            ],
            'mercader_wall':[
                pygame.image.load(sprites_file_path + 'sprites/room/mercader_wall.png').convert_alpha()
            ],
            'three_dog':[
                pygame.image.load(sprites_file_path + 'sprites/room/three_dog.png').convert_alpha()
            ],
            'buttons':[
                pygame.image.load(sprites_file_path + 'sprites/ui/button_two.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'sprites/ui/button_one.png').convert_alpha(),
                pygame.image.load(sprites_file_path + 'sprites/ui/button_three.png').convert_alpha()
            ]
        }
        self.fill_images_in_order(sprites,'titlecard',sprites_file_path,'screens/start/start', 21)
        self.fill_images_in_order(sprites,'title',sprites_file_path,'sprites/ui/title', 8)
        return sprites

    def fill_images_in_order(self,dic, key,file_path, path, images): 
        for i in range(images):
            dic[key].append(pygame.image.load(file_path + path + str(i+1) + '.png').convert_alpha())
