import pygame 
import sys
from settings import Settings
from ship import Ship

class AlienInvasion:

	def __init__(self):
		#Установка
		pygame.init()
		self.settings = Settings() 
		self.screen = pygame.display.set_mode(
			(self.settings.screen_width, self.settings.screen_height)
		)
		pygame.display.set_caption('Alien Invasion')
		self.ship = Ship(self)
		#Установка заднего фона
		self.bg_color = self.settings.bg_color

	def run_game(self):
		#Старт игры
		while True:
			#Событие 
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
			#Рисовать
			self.screen.fill(self.bg_color)
			self.ship.blitme()
			#Создаем образ
			pygame.display.flip()

if __name__ == '__main__':
	#Запуск
	ai = AlienInvasion()
	ai.run_game()

