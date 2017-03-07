###EtherEngine

import collisions
from globalVars import *
from playerClass import *
from enemyClass import *
from wallClass import *

import pygame
initialize()

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Open a New Window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Crystal Ether")

#--------------------------------------------------

spr_player = pygame.image.load("spr_player.png")
spr_background_one = pygame.image.load("spr_background_one.png")
spr_wall = pygame.image.load("spr_wall.png")

#player_location = [x, y, xsize, ysize]
player = Player(spr_player)

wall = WallObject(location = [300, 0, 0, 0])

clock = pygame.time.Clock()

carryOn = True
while carryOn:
	clock.tick(60)
	#Quit the Game
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			carryOn = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_x:
				carryOn = False

	#Movement Input
	keys = pygame.key.get_pressed()
	player.player_movement(keys)	

	#Draw to Screen
	screen.fill(WHITE)
	screen.blit(spr_background_one, [0, 0, 1400, 1000])
	
	#screen.blit(spr_wall, wall_location)
	for wall in globalVars.walls:
		screen.blit(wall.sprite, wall.location)

	#Draw Player Last
	screen.blit(player.sprite, player.location)

	#Updating Display
	pygame.display.flip()