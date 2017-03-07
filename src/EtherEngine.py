###EtherEngine

import collisions
import globalVars as gv
from playerClass import *
from enemyClass import *
from wallClass import *

import pygame
gv.initialize()

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

#Open a New Window
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Crystal Ether")

#--------------------------------------------------

spr_player = pygame.image.load(gv.spriteDirectory + "spr_player.png")
spr_background_one = pygame.image.load(gv.spriteDirectory + "spr_background_one.png")
spr_wall = pygame.image.load(gv.spriteDirectory + "spr_wall.png")

#player_location = [x, y, xsize, ysize]
player = Player(spr_player)
enemy = Enemy([50,50], spr_player)


wall = Wall([300,0], spr_wall)

clock = gv.clock



carryOn = True
while carryOn:

	clock.tick(60)

	#Check to quit
	#-------------------
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			carryOn = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_x:
				carryOn = False

	#User Input
	#-------------------
	keys = pygame.key.get_pressed()
	player.actions(keys)	


	
	#Draw to Screen
	#-------------------
	screen.fill(WHITE)

	screen.blit(spr_background_one, spr_background_one.get_rect())
	
	for wall in gv.walls:
		screen.blit(wall.sprite, wall.location)

	for effect in gv.effects:
		pygame.draw.circle(screen, RED, (effect[0], effect[1]), 20)
		effect[2] = effect[2] - 1
		if effect[2] <= 0:
			gv.effects.remove(effect)

	#Draw enemy
	enemy.randomWalk()
	screen.blit(enemy.sprite, enemy.location)

	#Draw Player Last
	screen.blit(player.sprite, player.location)


	#Update Display
	pygame.display.flip()
