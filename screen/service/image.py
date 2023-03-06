import pygame
import data.config as config

def get_image(path, x, y):
    img = pygame.image.load(path).convert_alpha()
    img = pygame.transform.smoothscale(img, (x,y))
    return img

class GetImage:
    @staticmethod
    def img1():
        return get_image('image/bird1.png', config.bird_scale_x, config.bird_scale_y)
    
    @staticmethod
    def img2():
        return get_image('image/bird2.png', config.bird_scale_x, config.bird_scale_y)
    
    @staticmethod
    def img3():
        return get_image('image/bird3.png', config.bird_scale_x, config.bird_scale_y)
    
    @staticmethod
    def img4():
        return get_image('image/bird4.png', config.bird_scale_x, config.bird_scale_y)
    
    @staticmethod
    def img5():
        return get_image('image/bird5.png', config.bird_scale_x, config.bird_scale_y)
    
    @staticmethod
    def img6():
        return get_image('image/bird6.png', config.bird_scale_x, config.bird_scale_y)
    
    @staticmethod
    def img7():
        return get_image('image/bird7.png', config.bird_scale_x, config.bird_scale_y)
    
    @staticmethod
    def background():
        return get_image('image/background.jpg', config.screen_x, config.screen_y)
    
    @staticmethod
    def ground_layer_top():
        return get_image('image/ground_layer_top.png', config.ground_x, config.ground_top_y)
    
    @staticmethod
    def ground_layer():
        return get_image('image/ground_layer.png', config.ground_x, config.ground_y)
    
    @staticmethod
    def wood():
        return get_image('image/wood.png', config.tree_weight, config.tree_height)
    
    @staticmethod
    def scoreboard():
        return get_image('image/scoreboard.png', config.scoreboard_weight, config.scoreboard_height)
    
    @staticmethod
    def high_score():
        return get_image('image/high_score.png', 0, 0)