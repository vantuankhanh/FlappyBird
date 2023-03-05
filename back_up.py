import pygame
from sys import exit
from component.bird import Bird
from component.tree import Tree
import data.config as config
from random import uniform
from screen.play_screen import play_screen

# def play_screen():
#     score = 0
#     #Game event
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#         if event.type == tree_timer:
#             tree_y = uniform(config.tree_min_y, config.tree_max_y)
#             tree.add(Tree('up', tree_y),Tree('down', tree_y))

#     screen.blit(background, (0,0))

#     bird.draw(screen)
#     bird.update()

#     tree.draw(screen)
#     tree.update()

# def collision():
#     if pygame.sprite.spritecollide(bird.sprite, tree, False):
#         pass

if __name__ == '__main__':
    #Initialize game
    pygame.init()
    screen = pygame.display.set_mode((config.screen_x, config.screen_y))
    pygame.display.set_caption('Final Project')
    clock = pygame.time.Clock()
    game_mode_list = ['menu_screen','play_screen','game_over_screen']
    game_mode = game_mode_list[1]

    # #Background
    # background = pygame.image.load('image/background.jpg').convert_alpha()
    # background = pygame.transform.smoothscale(background, (config.screen_x, config.screen_y))
    # screen.blit(background, (0,0))

    # #Group bird
    # bird = pygame.sprite.GroupSingle()
    # bird.add(Bird())

    # #Group tree
    # tree_y = uniform(config.tree_min_y, config.tree_max_y)
    # tree = pygame.sprite.Group()
    # tree.add(Tree('up', tree_y),Tree('down', tree_y))

    # #Tree timer
    # tree_timer = pygame.USEREVENT + 1
    # pygame.time.set_timer(tree_timer, config.tree_time)

    while True:
        if game_mode == 'play_screen':
            play_screen(screen)

        pygame.display.update()
        clock.tick(60) #Lock FPS 60