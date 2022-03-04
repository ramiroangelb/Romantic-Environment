from msilib import sequence
import pygame

class TitleCardImage(pygame.sprite.Sprite):
    def __init__(self, screen, sprites, pos):
        super().__init__()
        self.sprite_list = sprites.get_object_sprite('titlecard')
        self.image = self.sprite_list[0]
        self.rect = self.image.get_rect(center = pos)
        self.frame = 0.0
        self.screen = screen
        self.wait = False
        self.wait_time = 3000
        self.wait_begin = 0
        self.wait_now = 0
        self.completed = False

    def __animate_title_card(self):
        self.image = self.sprite_list[int(self.frame)]
        self.frame += 0.05
        if len(self.sprite_list) <= int(self.frame):
            self.wait = True
            self.wait_begin = pygame.time.get_ticks()

    def get_completed(self):
        return self.completed

    def update(self):
        if not self.wait:
            self.__animate_title_card()
        else:
            self.wait_now = pygame.time.get_ticks()
            if self.wait_now - self.wait_begin > self.wait_time:
                self.screen.sequence_over = True
                if self.rect.x < 200:
                    self.rect.x += 1
                else:
                    self.completed = True



class TitleCard():
    
    def __init__(self, surface, sprites):
        #Display
        self.display_surface = surface
        #Sprites
        self.sequence_over = False
        x, y = self.display_surface.get_size()
        x = x // 2
        y = y // 2
        self.completed = False
        self.title_card = TitleCardImage(self, sprites, (x, y))
        self.sprite_group = pygame.sprite.Group()
        self.sprite_group.add(self.title_card)



    def draw(self):
        self.display_surface.fill('black')
        self.display_surface.fill((5,57,25))
        self.sprite_group.update()
        self.sprite_group.draw(self.display_surface)
        return self.title_card.get_completed()
