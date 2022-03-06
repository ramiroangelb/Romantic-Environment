import pygame

class Cursor(pygame.sprite.Sprite):
    def __init__(self, pos, sprite_dict, clickeable_list):
        
        super().__init__()

        #Sprite
        self.player_sprites = sprite_dict
        self.image = self.player_sprites['cursor'][0]
        self.rect = self.image.get_rect(topleft = pos)
        self.click_rect = pygame.Rect(pos, (3,3))
        #Click logic
        self.clicked = False
        self.can_click = True
        self.delay = False
        self.delay_time = 500
        self.delay_now = 0
        self.delay_start = 0
        self.clickeable_list = clickeable_list
    
    def get_input(self):

        movement_input = pygame.key.get_pressed()

        if movement_input[pygame.K_RIGHT]:
            self.rect.x += 1
            self.click_rect.x +=1
        if movement_input[pygame.K_LEFT]:
            self.rect.x -= 1
            self.click_rect.x -=1
        if movement_input[pygame.K_UP]:
            self.rect.y -= 1
            self.click_rect.y -=1
        if movement_input[pygame.K_DOWN]:
            self.rect.y += 1
            self.click_rect.y +=1
        self.delay_now = pygame.time.get_ticks()
        if movement_input[pygame.K_x] and self.can_click:
            self.clicked = True
            if self.clicked:
                self.can_click = False
                if not self.delay:
                    self.delay_start = pygame.time.get_ticks()
                    self.delay = True
                print('click')
        if self.delay and self.delay_now - self.delay_start > self.delay_time: #delay_terminado
            self.can_click = True
            self.delay = False

        #Do stuff
        if self.clicked:
            for object in self.clickeable_list:
                if self.click_rect.colliderect((object.rect)):
                    print('Interaction')

        self.clicked = False

    
    def update(self):
        self.get_input()
        pygame.draw.rect(pygame.display.get_surface(), 'white', self.click_rect, 2)