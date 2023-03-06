import pygame
import data.config as config
from screen.component.bird import Bird
from screen.component.tree import Tree
from random import uniform
from data.game_class import GameMode, Collision, Fell
from screen.service.image import GetImage
from screen.service.score import Score
from time import sleep

pygame.init()

def display():
    screen.blit(background, (0,0))

def quit_program(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    
def get_score():
    score_add = 0
    for t in tree:
        if t.rect.right <= bird.sprite.rect.left and t.can_score == True:
            t.can_score = False
            score_add += 0.5
    return int(score_add)

def collision():
    collision_list = pygame.sprite.spritecollide(bird.sprite, tree, False)
    if collision_list:
        Collision.get = True

def play_screen():
    global score

    display()
    collision()

    for event in pygame.event.get():
        quit_program(event)
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

    score += get_score()
    score_board = font.render(f'{score}', True, config.score_color)
    score_board_rect = score_board.get_rect(center = (config.screen_x//2, 50))
    screen.blit(score_board, score_board_rect)

    if Collision.get == True:
        bird.sprite.collision = True
        bird.sprite.last_y = bird.sprite.rect.y
        Score.create_high_score_file()
        Score.update_high_score(score)
        pygame.time.delay(500)
        GameMode.mode = 'end'

def end_screen():

    display()

    screen.blit(ground_top, ground_top_rect)
    tree.draw(screen)
    screen.blit(ground, ground_rect)

    bird.draw(screen)
    bird.update()

    if bird.sprite.rect.bottom >= config.screen_y - config.ground_y:
        bird.sprite.rect.bottom = config.screen_y - config.ground_y
        # Score.create_score_board(screen, font, score)
        screen.blit(score_board, score_board_rect)
        score_board_rect.bottom -= 10
        if score_board_rect.bottom <= config.screen_y - config.ground_y + 10:
            score_board_rect.bottom = config.screen_y - config.ground_y + 10
        
        show_score = font.render(f'Score: {score}', True, config.scoreboard_color)
        show_score_rect = show_score.get_rect(x = 160, y = 130)
        show_highscore = font.render(f'Best: {Score.get_high_score()}', True, config.scoreboard_color)
        show_highscore_rect = show_score.get_rect(x = 160, y = 180)
        score_board.blit(show_score, show_score_rect)
        score_board.blit(show_highscore, show_highscore_rect)

    for event in pygame.event.get():
        quit_program(event)

score = 0

#Display
screen = pygame.display.set_mode((config.screen_x, config.screen_y))
icon = GetImage.img1()
pygame.display.set_caption('Flappy Bird')
pygame.display.set_icon(icon)

#Font
font = pygame.font.Font('data/score.ttf', config.score_font_size)

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

#Scoreboard
score_board = GetImage.scoreboard()
score_board_rect = score_board.get_rect(midbottom = (config.screen_x//2, config.screen_y + config.scoreboard_height))