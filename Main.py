import pygame
from Ballon import Ballon

Welcome_logo = pygame.image.load("assets/Nouveau dossier/Logo d'acceuil.png")
start_button = pygame.image.load("assets/Nouveau dossier/Start Button.png")
start_button_rect = start_button.get_rect()
start_button_rect.x = math.ceil(screen.get_width() / 3.33)
start_button_rect.y = math.ceil(screen.get_height() / 2)