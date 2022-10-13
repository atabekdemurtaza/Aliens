import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    """Класс для контроля пулей"""
    def __init__(self, ai_game):
        """Создаем образ пуля"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        """Создаем макет пуля и локация"""
        self.rect = pygame.Rect(
            0,0,
            self.settings.bullet_width,
            self.settings.bullet_height
        )
        self.rect.midtop = ai_game.ship.rect.midtop

        """Сохраняем образ в виде чисел"""
        self.y = float(self.rect.y)

    def update(self):
        """Движение снаряда по экрану"""
        self.y -= self.settings.bullet_speed
        """Обновляем снаряда"""
        self.rect.y = self.y

    def draw_bullet(self):
        """Рисуем снаряда по экрану"""
        pygame.draw.rect(self.screen, self.color, self.rect)