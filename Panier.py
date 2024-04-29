import pygame
import random

class Panier(pygame.sprite.Sprite):
    def __init__(self,Game):
        super().__init__()
        # Paramètres du ballon
        self.rect.x = random.randint(100,1000)
        self.rect.y = 100    # changer pour mettre la position du panier
        self.image = pygame.image.load("Image/Ballon.png")
        self.image = pygame.transform.scale(self.image, (100, 100))  # taille de l'image du ballon à remplir
        self.rect = self.image.get_rect()

    def spawn_panier(self):
        position_aleatoire_panier_x = random.randint(400, 800)
        position_aleatoire_panier_y = random.randint(1, 500)
        self.rect.x = position_aleatoire_panier_x
        self.rect.y = position_aleatoire_panier_y