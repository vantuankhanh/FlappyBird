import pygame
from sys import exit
from bird import Bird
from prop import screen_x, screen_y

def main():
    
    #Initialize game
    pygame.init()
    screen = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption('Final Project')
    clock = pygame.time.Clock()
    game_start = 1
    score = 0

    #Background
    background = pygame.image.load('image/background.jpg').convert_alpha()
    background = pygame.transform.smoothscale(background, (screen_x, screen_y))

    #Group bird
    bird = pygame.sprite.GroupSingle()
    bird.add(Bird())
    bird.draw(screen)

    #Game loop
    while True:
        #Game event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        if game_start == 1:
            screen.blit(background, (0,0))

            bird.draw(screen)
            bird.update()

        pygame.display.update()
        clock.tick(60) #Lock FPS 60

if __name__ == '__main__':
    main()