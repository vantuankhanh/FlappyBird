import pygame
from random import uniform
from data import config
from screen.component.bird import Bird
from screen.component.tree import Tree
from data.game_class import Game, Collision
from screen.service.visualize import GetImage, GetFont
from screen.service.score import Score
from screen.service.sound import GetSound

pygame.init()

def display_background():
    screen.blit(background, (0,0))

def menu_screen():
    
    global bird_menu_index, bird_menu_rect, bird_menu, move, down
    display_background()

    for event in pygame.event.get():
        Game.quit_program(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Game.mode = 'play'

    screen.blit(title, title_rect)

    screen.blit(bird_menu, bird_menu_rect)
    #animate the swing
    bird_menu_index += 0.06
    if bird_menu_index >= 2:
        bird_menu_index = 0
    bird_menu = bird_menu_list[int(bird_menu_index)]
    #animate move up and down
    move += 0.07
    if down == True:
        bird_menu_rect.y += move
        if bird_menu_rect.centery >= 360:
            move = 0
            down = False
    elif down == False:
        bird_menu_rect.y -= move
        if bird_menu_rect.centery <= config.bird_menu_y:
            move = 0
            down = True

    screen.blit(space_menu, space_menu_rect)
    
def play_screen():

    display_background()
    Collision.collision(bird, tree)

    for event in pygame.event.get():
        Game.quit_program(event)
        if event.type == tree_timer and Collision.get == False:
            tree_y = uniform(config.tree_min_y, config.tree_max_y)
            # tree_y = config.tree_min_y
            tree.add(Tree('up', tree_y),Tree('down', tree_y))

    #draw the top of the ground
    screen.blit(ground_top, ground_top_rect)
    if Collision.get == False:
        ground_top_rect.left -= config.ground_speed
        if ground_top_rect.x <= -20:
            ground_top_rect.x = 0

        bird.draw(screen)
        bird.update()

    tree.draw(screen)        

    #draw the bottom of the ground
    screen.blit(ground, ground_rect)
    if Collision.get == False:
        tree.update()
        ground_rect.left -= config.ground_speed
        if ground_rect.x <= -20:
            ground_rect.x = 0

    #update the score
    Score.play_score(screen, bird, tree)

    if Collision.get == True:
        GetSound.crash().play()
        bird.sprite.collision = True
        Score.create_high_score_file()
        Score.update_high_score()
        pygame.time.delay(500)
        Game.mode = 'end'

def end_screen():
    global bird, tree
    display_background()

    screen.blit(ground_top, ground_top_rect)
    tree.draw(screen)
    screen.blit(ground, ground_rect)

    #animate the bird to fall down
    bird.draw(screen)
    bird.update()

    if bird.sprite.rect.bottom >= config.screen_y - config.ground_y:
        bird.sprite.rect.bottom = config.screen_y - config.ground_y
        Score.create_game_over_box(screen)
        Score.create_score_board(screen)
        Score.create_play_again_box(screen)

    for event in pygame.event.get():
        Game.quit_program(event)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and Score.play_again_appear == True:
                bird.empty()
                bird = pygame.sprite.GroupSingle()
                bird.add(Bird())
                tree = pygame.sprite.Group()

                Game.reset()
                Game.mode = 'play'

#Display
screen = pygame.display.set_mode((config.screen_x, config.screen_y))
icon = GetImage.img1()
pygame.display.set_caption('Flappy Bird')
pygame.display.set_icon(icon)

#Background
background = GetImage.background()

#Title
title = GetImage.title()
title_rect = title.get_rect(center = (config.title_x, config.title_y))

#Bird at menu
bird_menu_1 = GetImage.bird_menu_1()
bird_menu_2 = GetImage.bird_menu_2()
bird_menu_list = [bird_menu_1, bird_menu_2]
bird_menu_index = 0
bird_menu = bird_menu_list[bird_menu_index]
bird_menu_rect = bird_menu.get_rect(center = (config.bird_menu_x, config.bird_menu_y))
move = 0
down = True

#Press space to play at menu
font_menu = GetFont.menu()
space_menu = font_menu.render('Press SPACE to start', True, 'black')
space_menu_rect = space_menu.get_rect(center = (config.space_menu_x, config.space_menu_y))

#Ground
ground = GetImage.ground_layer()
ground_rect = ground.get_rect(topleft = (0, config.screen_y - config.ground_y))

ground_top = GetImage.ground_layer_top()
ground_top_rect = ground_top.get_rect(topleft = (0, config.screen_y - config.ground_y - config.ground_top_y))

#Group bird
bird = pygame.sprite.GroupSingle()
bird.add(Bird())

#Group tree
tree = pygame.sprite.Group()

#Tree timer
tree_timer = pygame.USEREVENT + 1
pygame.time.set_timer(tree_timer, config.tree_time)