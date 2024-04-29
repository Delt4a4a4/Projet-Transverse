import pygame
import math
import Game

pygame.init()
from Ballon import Ballon
from Panier import Panier
from Background import Fondecran

pygame_icon = pygame.image.load("chemin")
pygame.display.set_mode((800,500))
pygame.display.set_icon(pygame_icon)
pygame.display.set_caption("SuperBasketBall ver1.22 474 487 139")

screen = pygame.display.set_mode((1000,585))

if Fondecran.niveau == 0 :
    background = pygame.image.load("chemin")
elif Fondecran.niveau == 1 :
    background = pygame.image.load("chemin")
elif Fondecran.niveau == 2 :
    background = pygame.image.load("chemin")
else :
    background = pygame.image.load("chemin")

running = True

Welcome_logo = pygame.image.load("chemin")
start_button = pygame.image.load("chemin")
start_button_rect = start_button.get_rect()
start_button_rect.x = math.ceil(screen.get_width() / 3.33)
start_button_rect.y = math.ceil(screen.get_height() / 2)
game = Game()

while running:

    screen.blit(background, (0, 0))
    screen.blit(game.Ballon.image, game.Joueur.rect)

    if game.is_playing:
        # déclencher les instructions du jeu
        game.update(screen)