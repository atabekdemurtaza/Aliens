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
			self._check_events()
			#Рисовать
			self._update_screen()
	
	def _check_events(self):
		#Событие которое выделеляет действия мышки и клавиатуры
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RIGHT:
					#Двигаем кораблик на право
					self.ship.rect.x += 1
				 
	
	def _update_screen(self):
		#Рисовать
		self.screen.fill(self.bg_color)
		self.ship.blitme()
		#Создаем образ
		pygame.display.flip()


if __name__ == '__main__':
	#Запуск
	ai = AlienInvasion()
	ai.run_game()

