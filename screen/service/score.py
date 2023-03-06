import pygame
import data.config as config
import os
from screen.service.image import GetImage

class Score():
    @staticmethod
    def create_high_score_file():
        if not os.path.isfile('data/high_score.txt'):
            with open('data/high_score.txt','w') as file:
                file.write('high score: 0')

    @staticmethod
    def get_high_score():
        with open('data/high_score.txt') as file:
            highscore = file.read().split(':')[1].strip()
        return int(highscore)
    
    @staticmethod
    def update_high_score(score):
        try:
            highscore = Score.get_high_score()
            if score > highscore:
                with open('data/high_score.txt','r+') as file:
                    file.seek(0)
                    file.write('high score: ' + str(score))
        except:
            with open('data/high_score.txt','w') as file:
                file.seek(0)
                file.write('high score: '+str(score))

#     def create_score_board(screen, font, score):
#         screen.blit(score_board, score_board_rect)
#         score_board_rect.bottom -= 10
#         if score_board_rect.bottom <= config.screen_y - config.ground_y + 10:
#             score_board_rect.bottom = config.screen_y - config.ground_y + 10
        
#         show_score = font.render(f'Score: {score}', True, config.scoreboard_color)
#         show_score_rect = show_score.get_rect(x = 160, y = 130)
#         show_highscore = font.render(f'Best: {Score.get_high_score()}', True, config.scoreboard_color)
#         show_highscore_rect = show_score.get_rect(x = 160, y = 180)
#         score_board.blit(show_score, show_score_rect)
#         score_board.blit(show_highscore, show_highscore_rect)

# #Scoreboard
# score_board = GetImage.scoreboard()
# score_board_rect = score_board.get_rect(midbottom = (config.screen_x//2, config.screen_y + config.scoreboard_height))