import pygame

class GameWindow:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height
        self.screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('Romantic Environment')

    def get_screen(self):
        return self.screen

    def get_width(self):
        return self.window_width
    
    def get_height(self):
        return self.window_height
    
    def get_size(self):
        return (self.window_width, self.window_height)

    def set_width(self, new_width):
        self.window_width = new_width
    
    def set_height(self, new_height):
        self.window_height = new_height

class RenderSurface:
    def __init__(self, window_width, window_height):
        self.renderer = pygame.Surface((window_width // 3.5, window_height // 3.5))
    
    def get_renderer(self):
        return self.renderer