import pygame
import random

class Panier(pygame.sprite.Sprite):
    def __init__(self,Game):
        super().__init__()
        # Paramètres du ballon
        self.rect.x = random.randint(100,1000)
        self.rect.y = 100    # changer pour mettre la position du panier
        self.image = pygame.image.load("chemin")
        self.image = pygame.transform.scale(self.image, (?, ?))  # taille de l'image du ballon à remplir
        self.rect = self.image.get_rect()