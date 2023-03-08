import pygame
from data import config
from data.game_class import Game
from screen.game_screen import menu_screen,play_screen, end_screen

def main():

    while True: 

        if Game.mode == 'menu':
            menu_screen()
        elif Game.mode == 'play':
            play_screen()
        elif Game.mode == 'end':
            end_screen()

        pygame.display.update()
        clock.tick(config.fps)

pygame.init() 

clock = pygame.time.Clock()

if __name__ == '__main__':
    main()