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

    def get_rect(self):
        return self.rect

    def update_sprite(self):
        if len(self.sprite_list) - 1 <= int(self.frame):
            self.frame = 0.0
        self.image = self.sprite_list[int(self.frame)]
        self.frame += 0.15
    
    def move_right(self, speed):
        self.rect.x += speed
    
    def move_left(self, speed):
        self.rect.x -= speed
    
    def move_up(self, speed):
        self.rect.y -= speed
    
    def move_down(self, speed):
        self.rect.y += speed

    def update(self):
        self.update_sprite()
        #Check click