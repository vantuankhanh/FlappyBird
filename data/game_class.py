import pygame
from screen.service.visualize import GetImage

class Game():
    mode = 'menu'

    @staticmethod
    def quit_program(event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

class Collision():
    get = False

    @staticmethod
    def collision(bird, tree):
        collision_list = pygame.sprite.spritecollide(bird.sprite, tree, False)
        if collision_list:
            Collision.get = True