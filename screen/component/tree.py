import pygame
from data import config
from screen.service.visualize import GetImage

class Tree(pygame.sprite.Sprite):
    def __init__(self, side, y):
        super().__init__()
        self.image = GetImage.wood()
        self.x = config.tree_start_x
        self.y = y
        self.side = side

        if side == 'up':
            self.image = pygame.transform.rotate(self.image, 180)
            self.rect = self.image.get_rect(bottomleft = (self.x, self.y))
        else:
            self.rect = self.image.get_rect(topleft = (self.x, self.y + config.tree_distance))

        self.can_score = True

    def delete(self):
        if self.rect.right <= 0:
            self.kill()

    def update(self):
        self.rect.x -= config.tree_speed
        self.delete()