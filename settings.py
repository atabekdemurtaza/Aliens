class Settings:
	#Настройки
	def __init__(self):
		#Настройки экрана
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (231,230,230)

		#Настройка корабля
		self.ship_speed = 1.5

		#Настройка пули
		self.bullet_speed = 1.0
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullet_allowed = 3

		# Настройка пришельца
		self.alien_speed = 1.0

		# Граница
		self.fleet_drop_speed = 10
		# +1 +1 -> -1 -1 <-
		self.fleet_direction = 1

