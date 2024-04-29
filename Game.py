import pygame
class Game:
    def __init__(self):
        self.is_playing= False
        self.pressed = {}
        # argent
        self.score = 0

    # fait apparraitre les "stats"
    def update(self, screen):
        font = pygame.font.SysFont("lato", 36)
        score_text = font.render(f" {self.score}", 1, (255, 255, 255))
        screen.blit(score_text, (850, 20))