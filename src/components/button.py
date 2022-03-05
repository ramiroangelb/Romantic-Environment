import pygame 


class Button(pygame.sprite.Sprite):
    def __init__(self,x,y , width, height, fg, bg, content, fontsize=25):
        self.font = pygame.font.Font('src/assets/fonts/PressStart2P-Regular.ttf', fontsize)
        self.content = content

        self.x, self.y = x, y
        self.width, self.height = width, height

        self.fg, self.bg = fg, bg
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.bg)
        self.rect = self.image.get_rect()

        self.rect.x, self.rect.y = self.x, self.y
        self.text = self.font.render(self.content, True, self.fg )
        self.text_rect = self.text.get_rect(center=(self.width/2,self.height/2))
        self.image.blit(self.text, self.text_rect)
    
    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
        return False