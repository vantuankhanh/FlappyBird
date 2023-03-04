import pygame
from sys import exit
from component.bird import Bird
from component.tree import Tree
import data.config as config
from random import uniform

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

def play_screen(screen):
    #Game event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == tree_timer:
            tree_y = uniform(config.tree_min_y, config.tree_max_y)
            tree.add(Tree('up', tree_y),Tree('down', tree_y))

    bird.draw(screen)
    bird.update()

    tree.draw(screen)
    tree.update()