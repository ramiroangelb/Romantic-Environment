import pygame

class Button():
    def __init__(self, surface, pos, sprite_dict, type, content, fontsize=8):
        self.clicked = False
        self.surface = surface
        self.image = sprite_dict['buttons'][type]
        self.rect = self.image.get_rect(center = (pos[0] * 3.5, pos[1] * 3.5))

        self.content = content
        self.font = pygame.font.Font('src/assets/fonts/PressStart2P-Regular.ttf', fontsize)
        self.text = self.font.render(self.content, True, 'dark green')

    def reset_clicked(self):
        self.clicked = False

    def draw(self):
        pygame.display.get_surface().blit(self.image, self.rect)
        pygame.display.get_surface().blit(self.text, (self.rect.x + 8, self.rect.y + 5))

        pos = pygame.mouse.get_pos()
        action = ''

        if not self.clicked:
            if self.rect.collidepoint(pos):
                if pygame.mouse.get_pressed()[0]:
                    self.clicked = True
                    action = self.content
                    print('click')
        return action