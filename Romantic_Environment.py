import pygame
from sys import exit
from src.components.data.screen_data import GameWindow, RenderSurface
from src.components.data.img_data import TilesSource, SpritesSource
from src.components.room import Room
from src.components.write import Write
from src.components.title_card import TitleCard
from src.components.button import *

################
#Hello Mini Jam!
################

#Setup
game_window = GameWindow(616, 616)
render_surface = RenderSurface(game_window.get_width(), game_window.get_height())
clock = pygame.time.Clock()
tiles = TilesSource()
sprites = SpritesSource()
pygame.font.init()
completed_title_card = False
in_main_menu = False
start = False
in_help = False
first_time_call = True
#SCREENS
title_card = TitleCard(render_surface.get_renderer(), sprites)
#Message
text_1 = Write('', (0,0))
text_2 = Write('', (0,0))
text_3 = Write('', (0,0))
text_4 = Write('', (0,0))
text_5 = Write('', (0,0))

message_string_list= []
message_string_list.append('''Hello!''')
message_string_list.append('''You're on a date...''')
message_string_list.append('''Keep control of the''')
message_string_list.append('''environment. Keep things''')
message_string_list.append('''romantic and smooth!!!''')


#Buttons
btn_W = 400
btn_H = 70
play_button = Button(render_surface, (88,70), sprites.get_sprites_dict(),1,'Play') 
exit_button = Button(render_surface, (88,90), sprites.get_sprites_dict(),1,'Exit') 


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    #Renderer update
    scaled_renderer = pygame.transform.scale(render_surface.get_renderer(), game_window.get_size())
    game_window.get_screen().blit(scaled_renderer, (0,0))
    
    in_main_menu = True

    if completed_title_card:
        completed_title_card = title_card.draw()
        if completed_title_card:
            in_main_menu = True
    elif in_main_menu:
        render_surface.get_renderer().fill('black')
        
        render_surface.get_renderer().blit(sprites.get_sprites_dict()['title'][0], (30,20))

        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()
        action = ''

        if not start:
            action = play_button.draw()
            if action == 'Play':
                start = True
            action = exit_button.draw()
            if action == 'Exit':
                pygame.quit()
                exit()
        elif start and first_time_call:
            current_screen = Room(render_surface.get_renderer(),tiles,sprites)
            first_time_call = False
        elif start and not first_time_call:
            current_screen.draw()




    pygame.display.update()

    clock.tick(60)