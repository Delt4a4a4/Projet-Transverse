import pygame
import Background
import Panier
from Ballon import Ballon
from Panier import Panier
class Game:
    def __init__(self):
        self.is_playing= False
        self.pressed = {}
        self.score = 0
        self.ballon = Ballon(self)
        self.panier = Panier(self)
        self.puissance_game = 60
        self.angle_de_tir_game = 330
        self.chrono = 0

    '''
    permet d'afficher les infos de la partie en haut de l'ecran 
    Entrée : Class Game, Fenêtre
    Sortie : NULL
    '''

    def score_affichage(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 800, 25))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(650,0 , 800, 25))
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(400, 0, 500,25))

        font = pygame.font.SysFont("lato", 36)
        argent_text = font.render(f"score : {self.score}", 1, (255, 255, 255))
        screen.blit(argent_text, (0, 0))

        # afficher la bank du joueur sur l'écran
        font = pygame.font.SysFont("lato", 36)
        bank_text = font.render(f" {self.angle_de_tir_game}°", 1, (255, 255, 255))
        screen.blit(bank_text, (650, 0))

        font = pygame.font.SysFont("lato", 36)
        bank_text = font.render(f" {self.puissance_game}", 1, (255, 255, 255))
        screen.blit(bank_text, (750, 0))

        font = pygame.font.SysFont("lato", 36)
        bank_text = font.render(f" {self.chrono}Second", 1, (255, 255, 255))
        screen.blit(bank_text, (400, 0))