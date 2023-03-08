import pygame
from screen.service.visualize import GetImage
from data import config
from sys import exit

pygame.init()
background = GetImage.background()
medal = GetImage.medal()
screen = pygame.display.set_mode((config.screen_x,config.screen_y))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(background, (0,0))
    scale = 50
    x = 512 - scale
    y = 512 - scale
    if x <= config.medal_x and y <= config.medal_y:
        x = config.medal_x
        y = config.medal_y
    scale += 50
    medal = GetImage.medal()
    medal = pygame.transform.smoothscale(medal, (x, y))
    medal_rect = medal.get_rect(center = (325,525))
    screen.blit(medal, medal_rect)