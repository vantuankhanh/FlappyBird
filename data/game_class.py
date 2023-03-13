import pygame
from screen.service.score import Score
from data import config
from screen.service.visualize import GetImage

class Game:
    mode = 'menu'
    first_spawn = False

    @staticmethod
    def quit_program(event):
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    @staticmethod
    def reset():
        Score.score = 0
        Score.score_board_appear = False
        Score.play_again_appear = False
        Score.score_board = GetImage.scoreboard()
        Score.score_board_rect = Score.score_board.get_rect(midbottom = (config.screen_x//2, config.screen_y + config.scoreboard_height))
        Score.play_again_rect = Score.play_again.get_rect(center = (config.screen_x//2, config.screen_y + (config.screen_y - config.play_again_y//2 - 10)))
        Score.game_over_rect = Score.game_over.get_rect(center = (config.screen_x//2, - config.game_over_y))
        Collision.get = False
        config.tree_time = 1600
        config.tree_distance = 190
        config.gravity_increase = 0.7

class Collision:
    get = False

    #Check collision
    @staticmethod
    def collision(bird, tree):
        collision_list = pygame.sprite.spritecollide(bird.sprite, tree, False)
        if collision_list:
            Collision.get = True