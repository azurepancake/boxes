import pygame

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([100, 100])
		self.image.fill((0, 0, 200))
		self.rect = self.image.get_rect()

import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))

player = Player()
playerSprites = pygame.sprite.RenderPlain((player))

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			exit()
	
		screen.fill((0, 0, 0))
		playerSprites.draw(screen)
		pygame.display.flip()
