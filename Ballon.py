import pygame
from Panier import Panier
import numpy as np

class Ballon(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        # Paramètres du ballon
        self.image = pygame.image.load("Image/Ballon.png")
        self.image = pygame.transform.scale(self.image, (30, 30))  # taille de l'image du ballon à remplir
        self.rect = self.image.get_rect()
        self.rect.x = 100   # meme valeur que hauteur_initiale
        self.rect.y = 400   # meme valeur que hauteur_initiale
        self.y_position_initiale = 400  #changer pour mettre la position du ballon au départ
        self.x_position_initiale = 100  #changer pour mettre la position du ballon au départ
        self.vitesse_initiale = 70
        self.angle_de_tir = 330
        self.balloon = pygame.sprite.Group()
        self.balloon.add(self)
        self.gravity = -9.8
        self.panier = Panier
        self.x_trajectoire = []
        self.y_trajectoire = []
        '''self.rect.x_trajectoire = 0  # changer pour mettre la position du ballon au départ
        self.rect.y_trajectoire = 0  # changer pour mettre la position du ballon au départ'''
        self.temps_total_trajectoire = 4
        self.intervalle_temps_trajectoire = 0.1

        self.temps_total_tir = 2000
        self.intervalle_temps = 0.25


    def deplacement(self,window,panier_group,game):

        clock = pygame.time.Clock()
        angle = np.radians(self.angle_de_tir)
        v0x = self.vitesse_initiale * np.cos(angle)
        v0y = self.vitesse_initiale * np.sin(angle)
        temps_total = self.temps_total_tir
        intervalle_temps = self.intervalle_temps
        affichage = window.copy()
        for t in np.arange(0, temps_total, intervalle_temps):
            x = int(self.x_position_initiale + v0x * t)
            y = int(self.y_position_initiale + v0y * t - 0.5 * self.gravity * t ** 2)
            self.rect.x = x
            self.rect.y = y
            window.blit(affichage, (0, 0))
            self.balloon.draw(window)
            pygame.display.flip()

            if self.rect.x >800  or self.rect.y >500:
                window.blit(affichage, (0, 0))
                self.rect.x = self.x_position_initiale
                self.rect.y = self.y_position_initiale
                print("raté !")
                return 0
            collisions = pygame.sprite.spritecollide(self, panier_group, False)
            for panier in collisions:
                game.score += 1
                window.blit(affichage, (0, 0))
                self.rect.x = self.x_position_initiale
                self.rect.y = self.y_position_initiale
                game.score_affichage(window)
                print("score !")
                return 1
            clock.tick(60)  # Limite le jeu à 60 images par seconde (FPS)

    ''' Mets à jour la trajectoire du ballon à chaque frames
    
    def update(self):
        self.deplacement()'''

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)  # sprite, group, dokill,(hitbox)collide


    '''créer de petit trait pour dire la trajectoire
    
    def trajectoire_fleche(self,surface):
        back_color = (60, 60, 60)
        angle_position = [self.angle_de_tir]
        for i in self.x_trajectoire :
            pygame.draw.rect(surface, back_color, (self.x_trajectoire[i], self.y_trajectoire[i]), (self.x_trajectoire[i]+5, self.y_trajectoire[i]), 3)

    '''
    '''Calcule la trajectoire du ballon  
    '''
    def trajectoire(self,window):
        point_surface = pygame.Surface((800, 500), pygame.SRCALPHA)
        trajectoire_x = []
        trajectoire_y = []
        clock = pygame.time.Clock()
        angle = np.radians(self.angle_de_tir)
        v0x = self.vitesse_initiale * np.cos(angle)
        v0y = self.vitesse_initiale * np.sin(angle)
        temps_total = self.temps_total_tir
        intervalle_temps = self.intervalle_temps_trajectoire
        affichage = window.copy()
        for t in np.arange(0, temps_total, intervalle_temps):
            x = int(self.x_position_initiale + v0x * t)
            y = int(self.y_position_initiale + v0y * t - 0.5 * self.gravity * t ** 2)

            trajectoire_x.append(x)
            trajectoire_y.append(y)
        for loop in range (1,20) :
            self.trajectoire_x = trajectoire_x[loop]
            self.trajectoire_y = trajectoire_y[loop]
            point_surface.fill((0, 0, 0, 0))
            pygame.draw.rect(point_surface, (255, 0, 0), (self.trajectoire_x+15, self.trajectoire_y+15, 5, 5))
            window.blit(point_surface, (0, 0))
            pygame.display.flip()


