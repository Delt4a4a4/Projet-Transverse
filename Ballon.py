import pygame
import Panier
import numpy as np

class Ballon(pygame.sprite.Sprite):
    def __init__(self,Game):
        super().__init__()
        # Paramètres du ballon
        self.rect.x = 100    # meme valeur que hauteur_initiale
        self.rect.y = 100    # meme valeur que hauteur_initiale
        self.y_position_initiale = 100  #changer pour mettre la position du ballon au départ
        self.x_position_initiale = 100  #changer pour mettre la position du ballon au départ
        self.image = pygame.image.load("chemin")
        self.image = pygame.transform.scale(self.image, (?, ?))  # taille de l'image du ballon à remplir
        self.rect = self.image.get_rect()
        self.vitesse_initiale = 20
        self.angle_de_tir = 45


        self.x_trajectoire = []
        self.y_trajectoire = []
        '''self.rect.x_trajectoire = 0  # changer pour mettre la position du ballon au départ
        self.rect.y_trajectoire = 0  # changer pour mettre la position du ballon au départ'''
        self.temps_total_trajectoire = 4
        self.intervalle_temps_trajectoire = 1

        self.temps_total_tir = 20
        self.intervalle_temps = 0.01



    '''créer de petit trait pour dire la trajectoire
    '''
    def trajectoire_fleche(self,surface):
        back_color = (60, 60, 60)
        angle_position = [self.angle_de_tir]
        for i in self.x_trajectoire :
            pygame.draw.rect(surface, back_color, (self.x_trajectoire[i], self.y_trajectoire[i]), (self.x_trajectoire[i]+5, self.y_trajectoire[i]), 3)

    '''Calcule la trajectoire du ballon  
    '''
    def trajectoire(self):
        trajectoire_x = []
        trajectoire_y = []
        angle = np.radians(self.angle_de_tir)
        v0x = self.vitesse_initiale * np.cos(angle)
        v0y = self.vitesse_initiale * np.sin(angle)
        temps = np.arange(0, self.temps_total_trajectoire, self.intervalle_temps_trajectoire)  #donne la position du ballon tout les "intervalles_temps" sur "temps total"
        for i in temps:
            x = int(self.x_position_initiale + v0x * i)
            y = int(self.y_position_initiale + v0y * i - 0.5 * 9.8 * i ** 2)
            trajectoire_x.append(x)
            trajectoire_y.append(y)
        self.trajectoire_x = trajectoire_x
        self.trajectoire_y = trajectoire_y


        '''self.rect.x_trajectoire = int(v0x * temps)
        self.rect.y_trajectoire = int(self.hauteur_initiale + v0y * temps - 0.5 * 9.8 * temps ** 2)'''


    def deplacement (self):
        angle = np.radians(self.angle_de_tir)
        v0x = self.vitesse_initiale * np.cos(angle)
        v0y = self.vitesse_initiale * np.sin(angle)
        temps = np.arange(0, self.temps_total_tir,self.intervalle_temps)  # donne la position du ballon tout les "intervalles_temps" sur "temps total"
        """for i in temps:"""
            self.rect.x = int(self.x_position_initiale + v0x * temps)
            self.rect.y = int(self.y_position_initiale + v0y * temps - 0.5 * 9.8 * temps ** 2)



    ''' Mets à jour la trajectoire du ballon à chaque frames
    '''
    def update(self):
        self.deplacement()

    ''' calcule si le ballon est a une distance du panier pour marquer, si oui le ballon disparait et le score augmente 
    
    "Panier.rect.x", "Panier.rect.y" et "Game.score" sont totalement inventé faudra changer en fonction des autres codes 
    '''
    def panier (self,):
        if self.rect.x - Panier.rect.x < 5 and self.rect.x - Panier.rect.x > -5 and self.rect.y - Panier.rect.y < 5 and self.rect.y - Panier.rect.y > -5:
            self.kill()
            self.Game.score += 1

'''creation d'une classe Fleche 
'''
class Fleche(pygame.sprite.Sprite):
    def __init__(self,Game):
        super().__init__()
        self.rect.x = Ballon.rect.x
        self.rect.y = Ballon.rect.y
        self.image = pygame.image.load("chemin")
        self.image = pygame.transform.scale(self.image, (?, ?))  # taille de l'image du ballon à remplir
        self.rect = self.image.get_rect()
        self.angle_de_tir = Ballon.angle_de_tir
        self.origin_image = self.image

    '''fait tourner l'image de la fleche par rapport au bas gauche de l'image
    '''
    def fleche_tourne(self):
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle_de_tir,1)
        self.rect = self.image.get_rect(center=self.rect.bottomleft)
