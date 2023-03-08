from data import config
import os
from screen.service.visualize import GetImage, GetFont

class Score():
    score = 0
    score_board_appear = False

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
    def update_high_score():
        try:
            highscore = Score.get_high_score()
            if Score.score > highscore:
                with open('data/high_score.txt','r+') as file:
                    file.seek(0)
                    file.write('high score: ' + str(Score.score))
        except:
            with open('data/high_score.txt','w') as file:
                file.seek(0)
                file.write('high score: '+str(Score.score))

    @staticmethod
    def get_score(bird, tree):
        score_add = 0
        for t in tree:
            if t.rect.right <= bird.sprite.rect.left and t.can_score == True:
                t.can_score = False
                score_add += 0.5
        return int(score_add)

    @staticmethod
    def play_score(screen, bird, tree):
        font_score = GetFont.score()
        Score.score += Score.get_score(bird, tree)
        score_board = font_score.render(f'{Score.score}', True, config.score_color)
        score_board_rect = score_board.get_rect(center = (config.screen_x//2, 50))
        screen.blit(score_board, score_board_rect)

    @staticmethod
    def create_score_board(screen):

        show_score = font_scoreboard.render(f'Score: {Score.score}', True, config.scoreboard_color)
        show_score_rect = show_score.get_rect(x = 160, y = 130)
        show_highscore = font_scoreboard.render(f'Best: {Score.get_high_score()}', True, config.scoreboard_color)
        show_highscore_rect = show_score.get_rect(x = 160, y = 180)

        screen.blit(score_board, score_board_rect)
        score_board_rect.bottom -= 10
        score_board.blit(show_score, show_score_rect)
        score_board.blit(show_highscore, show_highscore_rect)

        if score_board_rect.bottom <= config.screen_y - config.ground_y + 10:
            score_board_rect.bottom = config.screen_y - config.ground_y + 10
            if Score.score > Score.get_high_score():
                score_board.blit(medal, medal_rect)
            Score.score_board_appear = True
        
        if Score.score_board_appear == True:
            play_again_text = font_play_again.render('Press SPACE to play again', True, config.play_again_color)
            play_again_text_rect = play_again_text.get_rect(center = (config.play_again_x//2, 22))

            screen.blit(play_again, play_again_rect)
            play_again.blit(play_again_text, play_again_text_rect)
            play_again_rect.centery -= 10
            if play_again_rect.centery <= config.screen_y - config.play_again_y//2 - 10:
                play_again_rect.centery = config.screen_y - config.play_again_y//2 - 10

#Scoreboard
score_board = GetImage.scoreboard()
score_board_rect = score_board.get_rect(midbottom = (config.screen_x//2, config.screen_y + config.scoreboard_height))

medal = GetImage.medal()
medal_rect = medal.get_rect(center = (250,260))

play_again = GetImage.play_again()
play_again_rect = play_again.get_rect(center = (config.screen_x//2, config.screen_y + (config.screen_y - config.play_again_y//2 - 10)))

#Font
font_scoreboard = GetFont.score_board()
font_play_again = GetFont.play_again()