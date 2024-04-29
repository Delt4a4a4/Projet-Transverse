import pygame

import Panier
import Ballon
class Game:
    def __init__(self):
        self.is_playing= False
        self.pressed = {}
        # score
        self.score = 0

    # fait apparraitre les "stats"
    def update(self, screen):
        font = pygame.font.SysFont("lato", 36)
        score_text = font.render(f" {self.score}", 1, (255, 255, 255))
        screen.blit(score_text, (850, 20))

    def spawn_mob(self):
        panier = Panier(self)