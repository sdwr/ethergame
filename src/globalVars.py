###Global Variables

import pygame
import collisions

global spriteDirectory 
spriteDirectory = "../sprites/"



def initialize():
	pygame.init()
	global walls
	global enemies	

	walls = []
	enemies = []


