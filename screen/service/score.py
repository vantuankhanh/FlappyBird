from data import config
import os
from screen.service.visualize import GetImage, GetFont
from screen.service.sound import GetSound

class Score():
    score = 0
    score_board_appear = False
    play_again_appear = False

    #Scoreboard
    score_board = GetImage.scoreboard()
    score_board_rect = score_board.get_rect(midbottom = (config.screen_x//2, config.screen_y + config.scoreboard_height))

    #Medal
    medal = GetImage.medal()
    medal_rect = medal.get_rect(center = (250,260))

    nice = GetImage.nice()
    nice_rect = nice.get_rect(center = (250,260))

    sad = GetImage.sad()
    sad_rect = sad.get_rect(center = (250,260))

    #Play again box
    play_again = GetImage.play_again()
    play_again_rect = play_again.get_rect(center = (config.screen_x//2, config.screen_y + (config.screen_y - config.play_again_y//2 - 10)))

    #Game over
    game_over = GetImage.game_over()
    game_over_rect = game_over.get_rect(center = (config.screen_x//2, - config.game_over_y))

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
                point_sound.play()
                
        return int(score_add)

    @staticmethod
    def play_score(screen, bird, tree):
        font_score = GetFont.score()
        Score.score += Score.get_score(bird, tree)
        score_board = font_score.render(f'{Score.score}', True, config.score_color)
        score_board_rect = score_board.get_rect(center = (config.screen_x//2, 50))
        screen.blit(score_board, score_board_rect)

    @staticmethod
    def create_game_over_box(screen):
        game_over_text_1 = font_game_over.render('GAME', True, config.game_over_color)
        game_over_text_1_rect = game_over_text_1.get_rect(center = (config.game_over_x//2, 90))
        game_over_text_2 = font_game_over.render('OVER', True, config.game_over_color)
        game_over_text_2_rect = game_over_text_2.get_rect(center = (config.game_over_x//2, 125))

        screen.blit(Score.game_over, Score.game_over_rect)
        Score.game_over.blit(game_over_text_1, game_over_text_1_rect)
        Score.game_over.blit(game_over_text_2, game_over_text_2_rect)
        Score.game_over_rect.bottom += 10
        if Score.game_over_rect.bottom >= config.game_over_y:
            Score.game_over_rect.bottom = config.game_over_y

    @staticmethod
    def create_score_board(screen):

        show_score = font_scoreboard.render(f'Score: {Score.score}', True, config.scoreboard_color)
        show_score_rect = show_score.get_rect(x = 160, y = 130)
        show_highscore = font_scoreboard.render(f'Best: {Score.get_high_score()}', True, config.scoreboard_color)
        show_highscore_rect = show_score.get_rect(x = 160, y = 180)

        screen.blit(Score.score_board, Score.score_board_rect)
        Score.score_board.blit(show_score, show_score_rect)
        Score.score_board.blit(show_highscore, show_highscore_rect)

        Score.score_board_rect.bottom -= 10
        if Score.score_board_rect.bottom <= config.screen_y - config.ground_y + 10:
            Score.score_board_rect.bottom = config.screen_y - config.ground_y + 10
            if Score.score > Score.get_high_score():
                Score.score_board.blit(Score.medal, Score.medal_rect)
            elif Score.score <= 10:
                Score.score_board.blit(Score.sad, Score.sad_rect)
            else:
                Score.score_board.blit(Score.nice, Score.nice_rect)
            Score.score_board_appear = True

    @staticmethod
    def create_play_again_box(screen):
        if Score.score_board_appear == True:
            play_again_text = font_play_again.render('Press SPACE to play again', True, config.play_again_color)
            play_again_text_rect = play_again_text.get_rect(center = (config.play_again_x//2, config.play_again_y//2))

            screen.blit(Score.play_again, Score.play_again_rect)
            Score.play_again.blit(play_again_text, play_again_text_rect)
            Score.play_again_rect.centery -= 10
            if Score.play_again_rect.centery <= config.screen_y - config.play_again_y//2 - 10:
                Score.play_again_rect.centery = config.screen_y - config.play_again_y//2 - 10
                Score.play_again_appear = True

#Font
font_game_over = GetFont.game_over()
font_scoreboard = GetFont.score_board()
font_play_again = GetFont.play_again()

#Point sound
point_sound = GetSound.point()
point_sound.set_volume(1)