import pygame
from pygame.locals import *

class Player(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface([30, 30])
		self.image.fill((0, 0, 200))
		self.rect = self.image.get_rect()
		self.rect.centerx = 200
		self.rect.centery = 285
		self.yVel = 0
		self.gravity = 1.2
		self.floor = 285
		self.jumping = False

	def jump(self):
		if not self.jumping:
			self.yVel = -15
			self.jumping = True

	def update(self):
		if self.jumping:
			self.yVel += self.gravity
			self.rect.centery += self.yVel
			if self.rect.centery > self.floor:
				self.rect.centery = self.floor
				self.yVel = 0
				self.jumping = False

def main():
	pygame.init()
	screen = pygame.display.set_mode((600, 300))
	player = Player()
	playerSprites = pygame.sprite.RenderPlain((player))
	clock = pygame.time.Clock()

	while True:
		clock.tick(45)
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				exit()
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					player.jump()
	
		screen.fill((0, 0, 0))
		playerSprites.draw(screen)
		playerSprites.update()
		pygame.display.flip()

if __name__ == "__main__":
	main()
