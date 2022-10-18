import pygame
from pygame.sprite import Sprite

class Alien(Sprite):

    """Отображаем хотя бы одну картину пришельца"""
    def __init__(self, ai_game):
        """Создаем образ пришельца"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        """Загружаем картину"""
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        """Каждый пришелец должен появится рядом с левой стороны"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        """Сохраняем горизонтальную локацию пришельца"""
        self.x = float(self.rect.x)
    def check_edge(self):

        # Возвращает True если один из частей флота врезается
        screen_rect = self.screen.get_rect()
        if self.rect.right >= self.rect.right or self.rect.left <= 0:
            return True

    def update(self):
        # Движение пришельца к правой стороне
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x