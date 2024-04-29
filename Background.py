import pygame

class Fondecran(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.niveau = 0
        self.image = pygame.image.load('Image/EcJikeZU8AA42Jq.jpg')


    def change_background(self):
        if self.niveau == 0:
            self.image = pygame.image.load("Image/EcJikeZU8AA42Jq.jpg")
        elif self.niveau == 1:
            self.image = pygame.image.load("chemin du 2e background")
        elif self.niveau == 2:
            self.image = pygame.image.load("chemin du 3e background")
        else:
            self.image = pygame.image.load("chemin du 4e background")

