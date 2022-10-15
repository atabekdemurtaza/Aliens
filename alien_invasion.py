import pygame 
import sys
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien

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
		self.bullets = pygame.sprite.Group()
		#Пришелец
		self.aliens = pygame.sprite.Group()
		self._create_fleet()
		#Установка заднего фона
		self.bg_color = self.settings.bg_color

	def run_game(self):
		#Старт игры
		while True:
			#Событие
			self._check_events()
			#Движение корабля
			self.ship.update()
			#Макет снаряда
			self.bullets.update()
			#Удаляем старые снаряды из памяти
			self._update_bullet()
			#print(len(self.bullets))
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

	def _check_keydown_events(self, event):
		if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
			# Двигаем кораблик на право
			self.ship.moving_right = True
		elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
			self.ship.moving_left = True
		elif event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
			sys.exit()
		elif event.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_events(self, event):
		if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
			self.ship.moving_right = False
		elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
			self.ship.moving_left = False

	def _fire_bullet(self):
		"""Создаем новых снарядов и добавляем в группу"""
		if len(self.bullets) < self.settings.bullet_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullet(self):
		"""Берем старые данные и обновляем на новое"""
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

	def _create_fleet(self):
		#Создаем флот
		#Cоздаем образ
		alien = Alien(self)
		alien_width = alien.rect.width
		available_space_x = self.settings.screen_width - (2 * alien_width)
		numbers_alien_x = available_space_x // (2 * alien_width)

		for alien_number in range(numbers_alien_x):
			#Создаем пришельца и измеряем локацию
			alien = Alien(self)
			alien.x = alien_width + (2 * alien_number * alien_width)
			alien.rect.x = alien.x
			self.aliens.add(alien)

	def _update_screen(self):
		#Рисовать
		self.screen.fill(self.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		self.aliens.draw(self.screen)
		#Создаем образ
		pygame.display.flip()


if __name__ == '__main__':
	#Запуск
	ai = AlienInvasion()
	ai.run_game()

