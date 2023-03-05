import pygame
import data.config as config
from screen.game_mode import GameMode
from screen.play_screen import play_screen
from screen.menu_screen import menu_screen
from screen.end_screen import end_screen

def main():

    while True:
        screen.blit(background, (0,0))

        if GameMode.mode == 'menu':
            menu_screen(screen)
            GameMode.mode = 'play'
        elif GameMode.mode == 'play':
            play_screen(screen)
        elif GameMode.mode == 'end':
            end_screen(screen)
        
        pygame.display.update()
        clock.tick(config.fps)

pygame.init() 

#Background
background = pygame.image.load('image/background.jpg').convert_alpha()
background = pygame.transform.smoothscale(background, (config.screen_x, config.screen_y))

clock = pygame.time.Clock()

screen = pygame.display.set_mode((config.screen_x, config.screen_y))
pygame.display.set_caption('Final Project')

if __name__ == '__main__':
    main()