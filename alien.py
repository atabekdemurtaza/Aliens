import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    """Отображаем хотя бы одну картину пришельца"""
    def __init__(self,ai_game):
        """Создаем образ пришельца"""
        super().__init__()
        self.screen = ai_game.screen

        """Загружаем картину"""
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        """Каждый пришелец должен появится рядом с левой стороны"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        """Сохраняем горизонтальную локацию пришельца"""
        self.x = float(self.rect.x)
