###Global Variables

import pygame
import collisions


global collision_handler 

def initialize():
	pygame.init()
	global walls
	global enemies

	walls = []
	enemies = []