import pygame
import data.config as config
from data.game_class import GameMode
from screen.game_screen import play_screen, end_screen

def main():

    while True: 

        if GameMode.mode == 'menu':
            # menu_screen(screen)
            GameMode.mode = 'play'
        elif GameMode.mode == 'play':
            play_screen()
        elif GameMode.mode == 'end':
            end_screen()

        pygame.display.update()
        clock.tick(config.fps)

pygame.init() 

clock = pygame.time.Clock()

if __name__ == '__main__':
    main()