import pygame
from data import config
from paths import IMAGE, FONT

pygame.init()
screen = pygame.display.set_mode((config.screen_x, config.screen_y))

def get_image(path, x, y):
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.smoothscale(img, (x,y))
    return img

class GetImage:
    @staticmethod
    def title():
        return get_image(IMAGE / 'title.png', config.title_w, config.title_h)
    
    @staticmethod
    def bird_menu_1():
        return get_image(IMAGE / 'bird1.png', config.bird_menu_w, config.bird_menu_h)
    
    @staticmethod
    def bird_menu_2():
        return get_image(IMAGE / 'bird2.png', config.bird_menu_w, config.bird_menu_h)
    
    @staticmethod
    def space_button():
        return get_image(IMAGE / 'space_button.png', config.space_button_w, config.space_button_h)

    @staticmethod
    def img1():
        return get_image(IMAGE / 'bird1.png', config.bird_scale_x, config.bird_scale_y)
    
    @staticmethod
    def img2():
        return get_image(IMAGE / 'bird2.png', config.bird_scale_x, config.bird_scale_y)
    
    @staticmethod
    def img3():
        return get_image(IMAGE / 'bird3.png', config.bird_scale_x, config.bird_scale_y)
    
    @staticmethod
    def img4():
        return get_image(IMAGE / 'bird4.png', config.bird_scale_x, config.bird_scale_y)
    
    @staticmethod
    def img5():
        return get_image(IMAGE / 'bird5.png', config.bird_scale_x, config.bird_scale_y)
    
    @staticmethod
    def img6():
        return get_image(IMAGE / 'bird6.png', config.bird_scale_x, config.bird_scale_y)
    
    @staticmethod
    def img7():
        return get_image(IMAGE / 'bird7.png', config.bird_scale_x, config.bird_scale_y)
    
    @staticmethod
    def background():
        return get_image(IMAGE / 'background.jpg', config.screen_x, config.screen_y)
    
    @staticmethod
    def ground_layer_top():
        return get_image(IMAGE / 'ground_layer_top.png', config.ground_x, config.ground_top_y)
    
    @staticmethod
    def ground_layer():
        return get_image(IMAGE / 'ground_layer.png', config.ground_x, config.ground_y)
    
    @staticmethod
    def wood():
        return get_image(IMAGE / 'wood.png', config.tree_weight, config.tree_height)
    
    @staticmethod
    def scoreboard():
        return get_image(IMAGE / 'scoreboard.png', config.scoreboard_weight, config.scoreboard_height)
    
    @staticmethod
    def medal():
        return get_image(IMAGE / 'medal.png', config.medal_x, config.medal_y)
    
    @staticmethod
    def nice():
        return get_image(IMAGE / 'nice.png', config.medal_x, config.medal_y)
    
    @staticmethod
    def sad():
        return get_image(IMAGE / 'sad.png', config.medal_x, config.medal_y)
    
    @staticmethod
    def play_again():
        return get_image(IMAGE / 'play_again_box.png', config.play_again_x, config.play_again_y)
    
    @staticmethod
    def game_over():
        return get_image(IMAGE / 'game_over_box.png', config.game_over_x, config.game_over_y)
    
class GetFont:
    @staticmethod
    def menu():
        return pygame.font.Font(FONT / 'space_menu.ttf', config.menu_font_size)

    @staticmethod
    def score():
        return pygame.font.Font(FONT / 'score.ttf', config.score_font_size)
    
    @staticmethod
    def score_board():
        return pygame.font.Font(FONT / 'score.ttf', config.scoreboard_font_size)
    
    @staticmethod
    def play_again():
        return pygame.font.Font(FONT / 'play_again.ttf', config.play_again_font_size)
    
    @staticmethod
    def game_over():
        return pygame.font.Font(FONT / 'score.ttf', config.game_over_font_size)