import pygame
import data.config as config
from screen.play_screen import play_screen

#Initialize game
pygame.init()
screen = pygame.display.set_mode((config.screen_x, config.screen_y))
pygame.display.set_caption('Final Project')
clock = pygame.time.Clock()
game_start = 1
score = 0

#Background
background = pygame.image.load('image/background.jpg').convert_alpha()
background = pygame.transform.smoothscale(background, (config.screen_x, config.screen_y))
screen.blit(background, (0,0))

#Game loop
while True:
    screen.blit(background, (0,0))
    play_screen(screen)

    pygame.display.update()
    clock.tick(60) #Lock FPS 60