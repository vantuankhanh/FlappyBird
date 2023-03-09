import pygame
from paths import AUDIO
from random import choice

class GetSound:

    @staticmethod
    def background_sound():
        return [AUDIO / 'background1.ogg',
                AUDIO / 'background2.ogg',
                AUDIO / 'background3.ogg',
                AUDIO / 'background4.ogg']
    
    @staticmethod
    def play_background_sound():
        list_sound = GetSound.background_sound()
        
        if pygame.mixer.music.get_busy():
            return None
        
        pygame.mixer.music.load(choice(list_sound))
        pygame.mixer.music.play(-1)
    
    @staticmethod
    def swing():
        return pygame.mixer.Sound(AUDIO / 'swing.ogg')
    
    @staticmethod
    def crash():
        return pygame.mixer.Sound(AUDIO / 'crash.ogg')