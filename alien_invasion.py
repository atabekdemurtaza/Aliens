import pygame 
import sys
from settings import Settings
from ship import Ship

class AlienInvasion:
	def __init__(self):
		#Установка
		pygame.init()
		self.settings = Settings() 
		self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height
		pygame.display.set_caption('Alien Invasion')
		self.ship = Ship(self)
		#Установка заднего фона
		self.bg_color = self.settings.bg_color

	def run_game(self):
		#Старт игры
		while True:
			#Событие
			self._check_events()
			#Движение корабля
			self.ship.update()
			#Рисовать
			self._update_screen()
	
	def _check_events(self):
		#Событие которое выделеляет действия мышки и клавиатуры
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			#Корабль не может одновременно двигать по обоим сторонам
			elif event.type == pygame.KEYDOWN:
				self._check_keydown_events(event)

			elif event.type == pygame.KEYUP:
				self._check_keyup_events(event)

	def _update_screen(self):
		#Рисовать
		self.screen.fill(self.bg_color)
		self.ship.blitme()
		#Создаем образ
		pygame.display.flip()

	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
			# Двигаем кораблик на право
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
			self.ship.moving_left = True
		elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
			sys.exit()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
			self.ship.moving_left = False

if __name__ == '__main__':
	#Запуск
	ai = AlienInvasion()
	ai.run_game()

