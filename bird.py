import pygame
import prop

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        bird1 = pygame.image.load('image/bird1.png').convert_alpha()
        bird1 = pygame.transform.smoothscale(bird1, (prop.bird_scale_x, prop.bird_scale_y))
        bird2 = pygame.image.load('image/bird2.png').convert_alpha()
        bird2 = pygame.transform.smoothscale(bird2, (prop.bird_scale_x, prop.bird_scale_y))
        bird_fly_down = pygame.image.load('image/bird3.png').convert_alpha()
        bird_fly_down = pygame.transform.smoothscale(bird_fly_down, (prop.bird_scale_x, prop.bird_scale_y))

        self.bird_fly = [bird1, bird2]
        self.bird_fly_index = 0
        self.image = self.bird_fly[self.bird_fly_index]
        self.rect = self.image.get_rect(center = (50, prop.screen_y//2))
        self.gravity = 0

        self.bird_fly_down = bird_fly_down
        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom > 0:
            self.gravity = -5

    def fly_down(self):
        self.gravity += prop.gravity_increase
        self.rect.y += self.gravity
        if self.rect.bottom >= prop.screen_y:
            self.rect.bottom = prop.screen_y

    def fly_animation(self):
        if self.rect.bottom >= prop.screen_y: 
            self.image = self.bird_fly_down
            self.rect.bottom = prop.screen_y
        else:
            self.bird_fly_index += 0.1
            if self.bird_fly_index >= len(self.bird_fly):
                self.bird_fly_index = 0
            self.image = self.bird_fly[int(self.bird_fly_index)]

    def update(self):
        self.player_input()
        self.fly_down()
        self.fly_animation()