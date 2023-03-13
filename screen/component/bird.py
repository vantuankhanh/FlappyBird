import pygame
from data import config
from screen.service.visualize import GetImage
from screen.service.sound import GetSound

class Bird(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        #Bird image
        self.bird_fly_1 = [GetImage.img1(), GetImage.img2()]
        self.bird_fly_2 = [GetImage.img3(), GetImage.img4()]
        self.bird_fly_3 = [GetImage.img5(), GetImage.img6()]
        self.bird_fly_3[0] = pygame.transform.rotate(self.bird_fly_3[0], - config.bird_rotate)
        self.bird_fly_3[1] = pygame.transform.rotate(self.bird_fly_3[1], - config.bird_rotate)
        self.bird_fly_index = 0

        self.bird_fall = GetImage.img7()
        self.bird_fall = pygame.transform.rotate(self.bird_fall, - 0)

        self.jump_sound = GetSound.swing()

        #Initial property
        self.collision = False
        self.image = self.bird_fly_1[self.bird_fly_index]
        self.rect = self.image.get_rect(center = (config.screen_x//3, config.screen_y//2))
        self.gravity = 0
        self.jump = True
        self.start_jump = 0

    #Player's control by SPACE    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.jump:
            self.jump_sound.play()
            self.gravity = - config.gravity_jump
            self.jump = False
            self.start_jump = pygame.time.get_ticks()
        elif not keys[pygame.K_SPACE]:
            self.jump = True

    def fly_down(self):
        self.gravity += config.gravity_increase
        self.rect.y += self.gravity
        if self.rect.bottom >= config.screen_y - config.ground_y:
            self.rect.bottom = config.screen_y - config.ground_y

    def fly_animation(self):        
        current_time = pygame.time.get_ticks()
        #index to change animation of the swing
        self.bird_fly_index += 0.1
        if self.bird_fly_index >= 2:
            self.bird_fly_index = 0
        #change animation from img12 to img34
        if current_time - self.start_jump < config.bird_time_rotate:
            if self.rect.y <= config.bird_danger:
                self.image = self.bird_fly_1[int(self.bird_fly_index)]
            else:
                self.image = self.bird_fly_2[int(self.bird_fly_index)]                
        else:
            self.image = self.bird_fly_3[int(self.bird_fly_index)]
    
    def update(self):
        if self.collision == False:
            self.player_input()
            self.fly_down()
            self.fly_animation()
        else:
            self.image = self.bird_fall
            self.fly_down()