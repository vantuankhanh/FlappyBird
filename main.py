import pygame
from data import config
from data.game_class import Game
from screen.game_screen import play_screen, end_screen

def main():

    while True: 

        if Game.mode == 'menu':
            # menu_screen(screen)
            Game.mode = 'play'
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