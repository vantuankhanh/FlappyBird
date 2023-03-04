import pygame
from sys import exit
from component.bird import Bird
from component.tree import Tree
import data.config as config
from random import uniform

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

#Group bird
bird = pygame.sprite.GroupSingle()
bird.add(Bird())

#Group tree
tree_y = uniform(config.tree_min_y, config.tree_max_y)
tree = pygame.sprite.Group()
tree.add(Tree('up', tree_y),Tree('down', tree_y))

#Tree timer
tree_timer = pygame.USEREVENT + 1
pygame.time.set_timer(tree_timer, config.tree_time)

def play_screen():
    #Game event
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == tree_timer:
                tree_y = uniform(config.tree_min_y, config.tree_max_y)
                tree.add(Tree('up', tree_y),Tree('down', tree_y))

        screen.blit(background, (0,0))

        bird.draw(screen)
        bird.update()

        tree.draw(screen)
        tree.update()

        pygame.display.update()
        clock.tick(60) #Lock FPS 60

if __name__ == '__main__':
    play_screen()