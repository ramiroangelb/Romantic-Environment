import pygame

class She(pygame.sprite.Sprite):
    def __init__(self, pos, sprite_dict):

        super().__init__()
        #Sprite
        self.sprite_list = sprite_dict['she']
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
        if 
        self.update_sprite()
        #Check click