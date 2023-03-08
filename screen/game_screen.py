import pygame
from random import uniform
from data import config
from screen.component.bird import Bird
from screen.component.tree import Tree
from data.game_class import Game, Collision
from screen.service.visualize import GetImage
from screen.service.score import Score

pygame.init()

def display_background():
    screen.blit(background, (0,0))

def menu_screen():

    display_background()

    for event in pygame.event.get():
        Game.quit_program(event)

def play_screen():

    display_background()
    Collision.collision(bird, tree)

    for event in pygame.event.get():
        Game.quit_program(event)
        if event.type == tree_timer and Collision.get == False:
            tree_y = uniform(config.tree_min_y, config.tree_max_y)
            tree.add(Tree('up', tree_y),Tree('down', tree_y))

    screen.blit(ground_top, ground_top_rect)
    if Collision.get == False:
        ground_top_rect.left -= config.ground_speed
        if ground_top_rect.x <= -20:
            ground_top_rect.x = 0

        bird.draw(screen)
        bird.update()

    tree.draw(screen)        

    screen.blit(ground, ground_rect)
    if Collision.get == False:
        tree.update()
        ground_rect.left -= config.ground_speed
        if ground_rect.x <= -20:
            ground_rect.x = 0

    Score.play_score(screen, bird, tree)

    if Collision.get == True:
        bird.sprite.collision = True
        Score.create_high_score_file()
        Score.update_high_score()
        pygame.time.delay(500)
        Game.mode = 'end'

def end_screen():

    display_background()

    screen.blit(ground_top, ground_top_rect)
    tree.draw(screen)
    screen.blit(ground, ground_rect)

    bird.draw(screen)
    bird.update()

    if bird.sprite.rect.bottom >= config.screen_y - config.ground_y:
        bird.sprite.rect.bottom = config.screen_y - config.ground_y
        Score.create_score_board(screen)

    for event in pygame.event.get():
        Game.quit_program(event)

#Display
screen = pygame.display.set_mode((config.screen_x, config.screen_y))
icon = GetImage.img1()
pygame.display.set_caption('Flappy Bird')
pygame.display.set_icon(icon)

#Background
background = GetImage.background()

#Ground
ground = GetImage.ground_layer()
ground_rect = ground.get_rect(topleft = (0, config.screen_y - config.ground_y))

ground_top = GetImage.ground_layer_top()
ground_top_rect = ground_top.get_rect(topleft = (0, config.screen_y - config.ground_y - config.ground_top_y))

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