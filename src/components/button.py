import pygame 


class Button():
    def __init__(self,x,y , width, height, fg, bg, content, fontsize):
        self.font = pygame.font.Font('src/assets/fonts/PressStart2P-Regular.ttf', 25)
        