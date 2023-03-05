import pygame
import data.config as config
import os
from component.bird import Bird
from component.tree import Tree
from random import uniform
from screen.game_mode import GameMode
from time import sleep

pygame.init()

def create_high_score_file():
    if not os.path.isfile('data/high_score.txt'):
        with open('data/high_score.txt','w') as file:
            file.write('high score: 0')

def high_score():
    global score
    file = open('data/high_score.txt', 'r+')
    highscore = file.read()
    try:
        highscore = highscore.split(':')[1].strip()
        if score > int(highscore):
            file.seek(0)
            file.write('high score: '+str(score))
        file.close()
    except:
        file.seek(0)
        file.write('high score: '+str(score))
        file.close()
    
def get_score():
    score_add = 0
    for t in tree:
        if t.rect.right <= bird.sprite.rect.left and t.can_score == True:
            t.can_score = False
            score_add += 0.5
    return int(score_add)

def collision():
    if pygame.sprite.spritecollide(bird.sprite, tree, False):
        tree.empty()
        return True
    return False

def play_screen(screen):
    global score
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == tree_timer:
            tree_y = uniform(config.tree_min_y, config.tree_max_y)
            tree.add(Tree('up', tree_y),Tree('down', tree_y))

    screen.blit(ground_top, ground_top_rect)
    ground_top_rect.left -= config.ground_speed
    if ground_top_rect.x <= -20:
        ground_top_rect.x = 0

    bird.draw(screen)
    bird.update()

    tree.draw(screen)
    tree.update()

    screen.blit(ground, ground_rect)
    ground_rect.left -= config.ground_speed
    if ground_rect.x <= -20:
        ground_rect.x = 0

    score += get_score()
    score_board = font.render(f'{score}', True, config.score_color)
    score_board_rect = score_board.get_rect(center = (config.screen_x//2, 50))
    screen.blit(score_board, score_board_rect)

    if collision():
        create_high_score_file()
        high_score()
        sleep(2)
        GameMode.mode = 'end'

screen = pygame.display.set_mode((config.screen_x, config.screen_y))
font = pygame.font.Font('data/score.ttf', config.score_font_size)

#Ground
ground = pygame.image.load('image/ground_layer.png').convert_alpha()
ground = pygame.transform.smoothscale(ground, (config.ground_x, config.ground_y))
ground_rect = ground.get_rect(topleft = (0, config.screen_y - config.ground_y))
ground_top = pygame.image.load('image/ground_layer_top.png').convert_alpha()
ground_top = pygame.transform.smoothscale(ground_top, (config.ground_x, config.ground_top_y))
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

score = 0