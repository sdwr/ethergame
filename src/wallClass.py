###Wall Object Class

import pygame
import globalVars

class WallObject:
	sprite, location = 0,0
	
	def __init__(self, location = [1, 1, 16, 16], sprite = pygame.image.load(globalVars.spriteDirectory + "spr_wall.png")):
		self.sprite = sprite
		self.location = location.copy()
		self.location[2] = sprite.get_rect()[2]
		self.location[3] = sprite.get_rect()[3]

		globalVars.walls.append(self)