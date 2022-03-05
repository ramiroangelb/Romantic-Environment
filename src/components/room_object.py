import pygame

class RoomObject(pygame.sprite.Sprite):
    def __init__(self, pos, sprite_dict, type):

        super().__init__()
        #Sprite
        self.sprite_list = sprite_dict[type]
        self.image = self.sprite_list[0]
        self.rect = self.image.get_rect(topleft = pos)
        #Sprite animation
        self.frame = 0.0
        #Movement
        pass

    def update_sprite(self):
        if len(self.sprite_list) <= int(self.frame):
            self.frame = 0.0
        self.image = self.sprite_list[int(self.frame)]
        self.frame += 0.15

    def update(self):
        self.update_sprite()
        #Check click