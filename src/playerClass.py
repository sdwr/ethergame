###Player Object Class

import pygame
import collisions

class Player:
	hp, speed, sprite, location = 0,0,0,0

	def __init__(self, sprite):
		self.hp = 10
		self.speed = 10
		self.sprite = sprite
		self.location = sprite.get_rect()

	def actions(self, keys):

		#movement
		new_location = self.location.copy()

		if keys[pygame.K_a]:
			new_location[0] -= 10
		if keys[pygame.K_d]:
			new_location[0] += 10
		if keys[pygame.K_w]:
			new_location[1] -= 10
		if keys[pygame.K_s]:
			new_location[1] += 10

		if not collisions.doesCollide(new_location):
			self.location = new_location


		#attacking


	def canAttack():

		return True