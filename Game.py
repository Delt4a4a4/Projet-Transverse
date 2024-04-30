import pygame
import Background
import Panier
from Ballon import Ballon
class Game:
    def __init__(self):
        self.is_playing= False
        self.pressed = {}
        # score
        self.score = 0
        self.ballon = Ballon(self)
        self.puissance_game = 60
        self.angle_de_tir_game = 330

    # fait apparraitre les "stats"

    def score_affichage(self, screen):
        # font = pygame.font.SysFont("mono" ,16)
        # argent_text = font.render(f"argent : {self.argent}",1,(0,0,0))
        # screen.blit(argent_text,(20,20)

        font = pygame.font.SysFont("lato", 36)
        argent_text = font.render(f"score : {self.score}", 1, (255, 255, 255))
        screen.blit(argent_text, (50, 20))

        # afficher la bank du joueur sur l'écran
        font = pygame.font.SysFont("lato", 36)
        bank_text = font.render(f" {self.angle_de_tir_game}°", 1, (255, 255, 255))
        screen.blit(bank_text, (600, 20))

        font = pygame.font.SysFont("lato", 36)
        bank_text = font.render(f" {self.puissance_game}", 1, (255, 255, 255))
        screen.blit(bank_text, (700, 20))