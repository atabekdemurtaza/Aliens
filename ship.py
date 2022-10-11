import pygame 

class Ship:

	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		#Загружаем иконку
		self.image = pygame.image.load('images/ship.bmp')
		self.rect  = self.image.get_rect()
		#Локация
		self.rect.midbottom = self.screen_rect.midbottom
		#Движение кораблика
		self.moving_right = False
		self.moving_left  = False

	def update(self):
		#Обновляем движение
		if self.moving_right:
			self.rect.x += 1
		if self.moving_left:
			self.rect.x -= 1

	def blitme(self):
		self.screen.blit(self.image, self.rect)



