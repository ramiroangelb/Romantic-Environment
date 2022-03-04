import pygame

class Write():
    def __init__(self, string, pos):
        self.x, self.y = pos
        self.string = string
        self.font = pygame.font.Font('src/assets/fonts/PressStart2P-Regular.ttf', 25)
        self.display_surf = pygame.display.get_surface()


    def erase_text(self):
        self.string = ''
    
    def change_text(self, string):
        self.string = string
    
    def change_pos(self, pos):
        self.x, self.y = pos
    
    def draw(self):
        self.debug_surf = self.font.render(self.string, True, 'Green')
        self.debug_rect = self.debug_surf.get_rect(topleft = (self.x, self.y))
        self.display_surf.blit(self.debug_surf,self.debug_rect)