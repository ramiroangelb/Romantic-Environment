import pygame
from sys import exit
from src.components.data.screen_data import GameWindow, RenderSurface
from src.components.data.img_data import TilesSource, SpritesSource
#from src.components.room import Room
from src.components.write import Write
from src.components.title_card import TitleCard


################
#Hello Mini Jam!
################

#Setup
game_window = GameWindow(640, 640)
render_surface = RenderSurface(game_window.get_width(), game_window.get_height())
clock = pygame.time.Clock()
#tiles = TilesSource()
sprites = SpritesSource()
current_screen = TitleCard(render_surface.get_renderer(), sprites)
pygame.font.init()
completed_title_card = False
text_1 = Write('', (0,0))
text_2 = Write('', (0,0))
text_3 = Write('', (0,0))
text_4 = Write('', (0,0))
text_5 = Write('', (0,0))
#Message
message_string_1 = '''Hello!'''
message_string_2 = '''You're on a date...'''
message_string_3 = '''Keep control of the'''
message_string_4 = '''environment. Keep things'''
message_string_5 = '''romantic and smooth!!!'''

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    #Renderer update
    scaled_renderer = pygame.transform.scale(render_surface.get_renderer(), game_window.get_size())
    game_window.get_screen().blit(scaled_renderer, (0,0))
    
    if not completed_title_card:
        completed_title_card = current_screen.draw()
    else:
        text_1.change_pos((20,20))
        text_1.change_text(message_string_1)
        text_1.draw()
        text_2.change_pos((20,60))
        text_2.change_text(message_string_2)
        text_2.draw()
        text_3.change_pos((20,100))
        text_3.change_text(message_string_3)
        text_3.draw()
        text_4.change_pos((20,140))
        text_4.change_text(message_string_4)
        text_4.draw()
        text_5.change_pos((20,180))
        text_5.change_text(message_string_5)
        text_5.draw()

    pygame.display.update()

    clock.tick(60)