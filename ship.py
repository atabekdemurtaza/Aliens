import pygame 

class Ship:

	def __init__(self, ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()
		#Настройка
		self.settings = ai_game.settings

		#Загружаем иконку
		self.image = pygame.image.load('images/ship.bmp')
		self.rect  = self.image.get_rect()

		#Локация
		self.rect.midbottom = self.screen_rect.midbottom
		
		#Сохраяняем данные о корабля двигающийся по горизантали
		self.x = float(self.rect.x)

		#Движение кораблика
		self.moving_right = False
		self.moving_left  = False

	def update(self):
		#Обновляем движение
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed

		#Обновляем по горизонтали
		self.rect.x = self.x

	def blitme(self):
		self.screen.blit(self.image, self.rect)



