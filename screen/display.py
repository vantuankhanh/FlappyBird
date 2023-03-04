import pygame
import data.config as config

def display():
    screen = pygame.display.set_mode((config.screen_x, config.screen_y))
    pygame.display.set_caption('Final Project')