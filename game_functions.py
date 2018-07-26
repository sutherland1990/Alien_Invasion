import sys

import pygame

def check_events():
	"""Respond to keypresses and mouse events."""
def update_screen(ai_settings,screen, ship):
	"""Update images on the screennabd fli to new screen"""	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()