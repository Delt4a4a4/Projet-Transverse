import pygame
import time
from Game import Game
from Panier import Panier
from Background import Fondecran
from Ballon import Ballon

pygame.init()
game = Game()
fondecran = Fondecran(game)
window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("SuperBasketBall ver1.22 474 487 139")
pygame_icon = pygame.image.load("Image/Ballon.png")
pygame.display.set_icon(pygame_icon)
font = pygame.font.SysFont('Helvetica', 20)

def background(lien, pos_x, pos_y):
    fond = pygame.image.load(lien)
    fond = fond.convert_alpha()
    fond = pygame.transform.smoothscale(fond, window.get_size())
    window.blit(fond, (pos_x, pos_y))
    pygame.display.flip()

def main_menu():
    start_bouton = pygame.draw.circle(window, (255, 0, 0), (400, 250), 30)
    quit_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(725, 0, 75, 80))
    while True:
        background("Image/terrain3.png", 0, 0)
        time.sleep(0.5)
        background("Image/terrain4.png", 0, 0)
        time.sleep(0.5)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_bouton.collidepoint(pygame.mouse.get_pos()):
                    menu2()
                elif quit_bouton.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()

        pygame.display.update()

def menu2():
    run = True
    button_clicked = [False]  # Liste des boutons cliqués
    map1_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(70, 100, 225, 125))
    map2_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(515, 100, 225, 125))
    map3_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(285, 260, 225, 125))
    quit_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(725, 0, 75, 80))
    background("Image/menu2.png", 0, 0)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_bouton.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif not button_clicked[0] and map1_bouton.collidepoint(pygame.mouse.get_pos()):
                    map1()  # Appeler map1 sans créer de nouveau ballon
                    button_clicked[0] = True  # Mettre à jour le drapeau du bouton 1
                elif not button_clicked[0] and map2_bouton.collidepoint(pygame.mouse.get_pos()):
                    map2()
                    button_clicked[0] = True  # Mettre à jour le drapeau du bouton 2
                elif not button_clicked[0] and map3_bouton.collidepoint(pygame.mouse.get_pos()):
                    map3()
                    button_clicked[0] = True  # Mettre à jour le drapeau du bouton 3
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                if event.key == pygame.K_SPACE:
                    game.ballon.deplacement()
                    print("TIRE!")

        pygame.display.update()

def map1():
    background("Image/terrain2.png", 0, 0)
    panier = Panier(game)
    ballon = Ballon(game)
    ballon.panier()
    Panier.spawn_panier(panier)
    window.blit(panier.image, panier.rect)
    window.blit(ballon.image, ballon.rect)


def map2():
    background("Image/terrain2.png", 0, 0)

def map3():
    background("Image/terrain2.png", 0, 0)

if __name__ == "__main__":
    main_menu()
