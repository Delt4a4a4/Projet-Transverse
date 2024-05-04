import pygame
import random

class Panier(pygame.sprite.Sprite):
    def __init__(self,Game):
        super().__init__()
        # Paramètres du ballon
        self.image = pygame.image.load("Image/Panier.png")
        self.image = pygame.transform.scale(self.image, (100, 85))  # taille de l'image du ballon à remplir
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(400, 800)
        self.rect.y = random.randint(1, 500)



    def spawn_panier(self):
        self.rect.x = random.randint(400, 700)
        self.rect.y = random.randint(1, 400)
