import pygame
import time
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
current_screen = TitleCard(render_surface.get_renderer(), sprites)
pygame.font.init()
completed_title_card = False
start = False
first_time_call = True
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
play_button = Button(game_window.get_width()/2 - btn_W/2 , 260, btn_W, btn_H, "green", "#0A3409", "Start") 
help_button = Button(game_window.get_width()/2 - btn_W/2, 360, btn_W, btn_H, "green", "#0A3409", "Help")
exit_button = Button(game_window.get_width()/2 - btn_W/2, 460, btn_W, btn_H, "green", "#0A3409", "Exit")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    #Renderer update
    scaled_renderer = pygame.transform.scale(render_surface.get_renderer(), game_window.get_size())
    game_window.get_screen().blit(scaled_renderer, (0,0))
    
    if completed_title_card:
        completed_title_card = current_screen.draw()
    else:
        mouse_pos = pygame.mouse.get_pos()
        mouse_pressed = pygame.mouse.get_pressed()

        if play_button.is_pressed(mouse_pos, mouse_pressed):
            start = True
        elif help_button.is_pressed(mouse_pos, mouse_pressed):
            print('help button')
        elif exit_button.is_pressed(mouse_pos, mouse_pressed):
            pygame.quit()
            exit()

        if not start:
            game_window.get_screen().blit(play_button.image, play_button.rect)
            game_window.get_screen().blit(help_button.image, help_button.rect)
            game_window.get_screen().blit(exit_button.image, exit_button.rect)

        if start and first_time_call:
            current_screen = Room(render_surface.get_renderer(),tiles,sprites)
            first_time_call = False
        elif start and not first_time_call:
            current_screen.draw()


    pygame.display.update()

    clock.tick(60)