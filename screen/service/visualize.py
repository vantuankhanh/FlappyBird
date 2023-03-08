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
    
class GetFont:
    @staticmethod
    def score():
        return pygame.font.Font(FONT / 'score.ttf', config.score_font_size)
    
    def score_board():
        return pygame.font.Font(FONT / 'score.ttf', config.score_font_size)