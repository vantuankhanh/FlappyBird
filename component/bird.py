import pygame
import data.config as config

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #Bird image
        bird1 = pygame.image.load('image/bird1.png').convert_alpha()
        bird1 = pygame.transform.smoothscale(bird1, (config.bird_scale_x, config.bird_scale_y))
        bird2 = pygame.image.load('image/bird2.png').convert_alpha()
        bird2 = pygame.transform.smoothscale(bird2, (config.bird_scale_x, config.bird_scale_y))
        bird3 = pygame.image.load('image/bird3.png').convert_alpha()
        bird3 = pygame.transform.smoothscale(bird3, (config.bird_scale_x, config.bird_scale_y))
        bird4 = pygame.image.load('image/bird4.png').convert_alpha()
        bird4 = pygame.transform.smoothscale(bird4, (config.bird_scale_x, config.bird_scale_y))
        bird5 = pygame.image.load('image/bird5.png').convert_alpha()
        bird5 = pygame.transform.smoothscale(bird5, (config.bird_scale_x, config.bird_scale_y))
        bird5 = pygame.transform.rotate(bird5, - config.bird_rotate)
        bird6 = pygame.image.load('image/bird6.png').convert_alpha()
        bird6 = pygame.transform.smoothscale(bird6, (config.bird_scale_x, config.bird_scale_y))
        bird6 = pygame.transform.rotate(bird6, - config.bird_rotate)
        bird7 = pygame.image.load('image/bird7.png').convert_alpha()
        bird7 = pygame.transform.smoothscale(bird7, (config.bird_scale_x, config.bird_scale_y))

        self.bird_fly_1 = [bird1, bird2]
        self.bird_fly_2 = [bird3, bird4]
        self.bird_fly_3 = [bird5, bird6]
        self.bird_fly_index = 0
        self.bird_fall = bird7
        self.bird_rotate = 0

        #Initial place
        self.image = self.bird_fly_1[self.bird_fly_index]
        self.rect = self.image.get_rect(center = (config.screen_x//3, config.screen_y//2))
        self.gravity = 0
        self.jump = 1
        self.start_jump = 0
        
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.jump:
            self.gravity = - config.gravity_jump
            self.jump = 0
            self.start_jump = pygame.time.get_ticks()
        elif not keys[pygame.K_SPACE]:
            self.jump = 1

    def fly_down(self):
        self.gravity += config.gravity_increase
        self.rect.y += self.gravity
        if self.rect.bottom >= config.screen_y - config.ground_y:
            self.rect.bottom = config.screen_y - config.ground_y
        elif self.rect.top <= 0:
            self.rect.top = 0

    def fly_animation(self):        
        current_time = pygame.time.get_ticks()
        self.bird_fly_index += 0.1
        if self.bird_fly_index >= 2:
            self.bird_fly_index = 0
        if current_time - self.start_jump < config.bird_time_rotate:
            if self.rect.centery < config.bird_danger:
                self.image = self.bird_fly_1[int(self.bird_fly_index)]
            else:
                self.image = self.bird_fly_2[int(self.bird_fly_index)]                
        else:
            self.image = self.bird_fly_3[int(self.bird_fly_index)]

    def update(self):
        self.player_input()
        self.fly_down()
        self.fly_animation()