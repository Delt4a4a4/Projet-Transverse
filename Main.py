import pygame
import time
from Game import Game
from Panier import Panier
from Background import Fondecran
from Ballon import Ballon
map = 0
pygame.init()
game = Game()
fondecran = Fondecran(game)
window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("SuperBasketBall ver1.22 474 487 139")
pygame_icon = pygame.image.load("Image/Ballon.png")
pygame.display.set_icon(pygame_icon)
font = pygame.font.SysFont('Helvetica', 20)
ballon = Ballon(game)
balloon_group = pygame.sprite.Group()  # Créez un groupe de sprites
panier_group = pygame.sprite.Group()
panier = Panier(game)
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
def map1():

    background("Image/terrain2.png", 0, 0)

    game.score_affichage(window)
    ballon.gravity = -9.8
    Panier.spawn_panier(panier)
    panier_group.add(panier)
    panier_group.draw(window)
    balloon_group.add(ballon)

def map2():
    background("Image/terrain2.png", 0, 0)

def map3():
    background("Image/terrain2.png", 0, 0)

def menu2():
    run = True
    button_clicked = [False]  # Liste des boutons cliqués
    map1_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(70, 100, 225, 125))
    map2_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(515, 100, 225, 125))
    map3_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(285, 260, 225, 125))
    quit_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(725, 0, 75, 80))
    background("Image/menu2.png", 0, 0)

    while run:
        global map
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
                    map = 1
                elif not button_clicked[0] and map2_bouton.collidepoint(pygame.mouse.get_pos()):
                    map2()
                    button_clicked[0] = True  # Mettre à jour le drapeau du bouton 2
                    map = 2
                elif not button_clicked[0] and map3_bouton.collidepoint(pygame.mouse.get_pos()):
                    map3()
                    button_clicked[0] = True  # Mettre à jour le drapeau du bouton 3
                    map = 3
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                if event.key == pygame.K_SPACE:
                    score = ballon.deplacement(window,panier_group,game)
                    if score == 1 and map == 1 :
                        map1()




                    print("TIRE!")
                if event.key == pygame.K_z:
                    game.puissance_game +=1
                    game.score_affichage(window)
                    ballon.vitesse_initiale = game.puissance_game
                    print("up puissance")
                    print(game.puissance_game)
                if event.key == pygame.K_s:
                    game.puissance_game -=1
                    game.score_affichage(window)
                    ballon.vitesse_initiale =game.puissance_game
                    print("down puissance")
                    print(game.puissance_game)
                if event.key == pygame.K_q:
                    game.angle_de_tir_game +=1
                    game.score_affichage(window)
                    ballon.angle_de_tir = game.angle_de_tir_game
                    print("up angle de tir")
                    print(game.angle_de_tir_game)
                if event.key == pygame.K_d:
                    game.angle_de_tir_game -=1
                    game.score_affichage(window)
                    ballon.angle_de_tir = game.angle_de_tir_game
                    print("down angle de tir")
                    print(game.angle_de_tir_game)
        balloon_group.draw(window) ##
        pygame.display.update()


if __name__ == "__main__":
    main_menu()
