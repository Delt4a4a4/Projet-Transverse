import pygame
import time
from Game import Game
from Panier import Panier
from Background import Fondecran
from Ballon import Ballon
from pygame import mixer

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

'''
Permet de jouer une musique 
Entrée : fichier mp3
Sortie : NULL
'''
def playsound(songName):
    mixer.init()
    mixer.music.load(songName)
    mixer.music.set_volume(0.5)
    mixer.music.play()

'''
Permet d'arrêter une musique 
Entrée : NULL
Sortie : NULL
'''
def stopsound():
    mixer.music.stop()

'''
Permet d'arrêter une musique 
Entrée : Int, Int 
Sortie : Int 
'''
def volume(vol,new_vol):
    if new_vol==0:
        vol=0
    elif new_vol==1 or new_vol==-1:
        vol+=0.1*new_vol
    elif new_vol==2:
        vol=0.5
    mixer.music.set_volume(vol)
    return vol

'''
Permet d'afficher un fond d'écran 
Entrée : Image, Int, Int 
Sortie : NULL
'''
def background(lien, pos_x, pos_y):
    fond = pygame.image.load(lien)
    fond = fond.convert_alpha()
    fond = pygame.transform.smoothscale(fond, window.get_size())
    window.blit(fond, (pos_x, pos_y))
    pygame.display.flip()

'''
Permet d'afficher le 1e écran
Entrée : NULL
Sortie : NULL
'''
def main_menu():
    playsound("Song\song.mp3")
    start_bouton = pygame.draw.circle(window, (255, 0, 0), (400, 250), 30)
    quit_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(725, 0, 75, 80))

    while True:
        background("Image/image.webp", 0, 0)
        time.sleep(0.5)
        background("Image/image2.webp", 0, 0)
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

'''
Permet d'afficher l'écran de victoire 
Entrée : NULL
Sortie : NULL
'''
def victoire ():
    background("Image/victoire.webp", 0, 0)

'''
Lance la 1ere map avec tout les sprites et l'affichage 
Entrée : NULL
Sortie : NULL
'''
def map1():

    background("Image/terrain_match.webp", 0, 0)
    game.score_affichage(window)
    ballon.gravity = -9.8
    ballon.trajectoire(window)
    Panier.spawn_panier(panier)
    panier_group.add(panier)
    panier_group.draw(window)
    balloon_group.add(ballon)

'''
Lance la 1ere map 
Entrée : NULL
Sortie : NULL
'''
def map1_bis():
    background("Image/terrain_match.webp", 0, 0)
    game.score_affichage(window)
    panier_group.draw(window)

'''
Lance la 2eme map avec tout les sprites et l'affichage 
Entrée : NULL
Sortie : NULL
'''
def map2():
    background("Image/Moon.webp", 0, 0)

    game.score_affichage(window)
    ballon.gravity = -1.62
    ballon.trajectoire(window)
    Panier.spawn_panier(panier)
    panier_group.add(panier)
    panier_group.draw(window)
    balloon_group.add(ballon)

'''
Lance la 2eme map 
Entrée : NULL
Sortie : NULL
'''
def map2_bis():
    background("Image/Moon.webp", 0, 0)
    game.score_affichage(window)
    panier_group.draw(window)

'''
Lance la 3eme map avec tout les sprites et l'affichage 
Entrée : NULL
Sortie : NULL
'''
def map3():
    background("Image/mars.webp", 0, 0)

    game.score_affichage(window)
    ballon.gravity = -3.71
    ballon.trajectoire(window)
    Panier.spawn_panier(panier)
    panier_group.add(panier)
    panier_group.draw(window)
    balloon_group.add(ballon)

'''
Lance la 3eme map
Entrée : NULL
Sortie : NULL
'''
def map3_bis():
    background("Image/mars.webp", 0, 0)
    game.score_affichage(window)
    panier_group.draw(window)

'''
Permet de jouer 
Entrée : NULL
Sortie : NULL
'''
def menu2():
    run = True
    button_clicked = [False]
    map1_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(70, 100, 225, 125))
    map2_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(515, 100, 225, 125))
    map3_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(285, 260, 225, 125))
    quit_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(725, 0, 75, 80))
    background("Image/menu2.png", 0, 0)
    start_time = pygame.time.get_ticks()
    while run:
        global map

        elapsed_time = pygame.time.get_ticks() - start_time
        seconds = elapsed_time // 1000
        game.chrono = seconds
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_bouton.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                elif not button_clicked[0] and map1_bouton.collidepoint(pygame.mouse.get_pos()):
                    map1()
                    button_clicked[0] = True
                    map = 1
                elif not button_clicked[0] and map2_bouton.collidepoint(pygame.mouse.get_pos()):
                    map2()
                    button_clicked[0] = True
                    map = 2
                elif not button_clicked[0] and map3_bouton.collidepoint(pygame.mouse.get_pos()):
                    map3()
                    button_clicked[0] = True
                    map = 3
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
                if event.key == pygame.K_SPACE:
                    score = ballon.deplacement(window,panier_group,game)
                    if score == 1 and map == 1 :
                        game.puissance_game = 60
                        ballon.vitesse_initiale = game.puissance_game
                        map1()
                        ballon.trajectoire(window)
                    if score == 1 and map == 2 :
                        game.puissance_game = 60
                        ballon.vitesse_initiale = game.puissance_game
                        map2()
                        game.puissance_game = 60
                        ballon.trajectoire(window)
                    if score == 1 and map == 3 :
                        game.puissance_game = 60
                        ballon.vitesse_initiale = game.puissance_game
                        map3()
                        ballon.trajectoire(window)
                    print("TIRE!")
                if event.key == pygame.K_z:
                    game.puissance_game +=2
                    game.score_affichage(window)
                    ballon.vitesse_initiale = game.puissance_game
                    if map == 1:
                        map1_bis()
                    if map == 2:
                        map2_bis()
                    if map == 3:
                        map3_bis()
                    ballon.trajectoire(window)
                    print("up puissance")
                    print(game.puissance_game)
                if event.key == pygame.K_s:
                    game.puissance_game -=2
                    game.score_affichage(window)
                    ballon.vitesse_initiale =game.puissance_game
                    if map == 1:
                        map1_bis()
                    if map == 2:
                        map2_bis()
                    if map == 3:
                        map3_bis()
                    ballon.trajectoire(window)
                    print("down puissance")
                    print(game.puissance_game)
                if event.key == pygame.K_q:
                    game.angle_de_tir_game -=2
                    game.score_affichage(window)
                    if map == 1:
                        map1_bis()
                    if map == 2:
                        map2_bis()
                    if map == 3:
                        map3_bis()
                    ballon.trajectoire(window)
                    ballon.angle_de_tir = game.angle_de_tir_game
                    print("up angle de tir")
                    print(game.angle_de_tir_game)
                if event.key == pygame.K_d:
                    game.angle_de_tir_game +=2
                    game.score_affichage(window)
                    if map == 1 :
                        map1_bis()
                    if map == 2 :
                        map2_bis()
                    if map == 3 :
                        map3_bis()
                    ballon.trajectoire(window)
                    ballon.angle_de_tir = game.angle_de_tir_game
                    print("down angle de tir")
                    print(game.angle_de_tir_game)
                    print (map)
        if game.chrono == 60 and map == 1 and game.score >=10 :
            token1 = 1
            game.score =0
            game.chrono=0
            game.puissance_game = 60
            map2()
            map=2
        elif game.chrono == 60 and map == 1 and game.score < 10 :
            main_menu()
            game.puissance_game = 60
            game.score =0
            game.chrono = 0
        if game.chrono == 120 and map == 2 and game.score >= 15:
            map3()
            token2 = 1
            game.score =0
            game.chrono = 0
            game.puissance_game = 60
            map = 3
        elif game.chrono == 120 and map == 2 and game.score < 15:
            main_menu()
            game.puissance_game = 60
            game.score =0
            game.chrono = 0
        if game.chrono == 180 and map == 3 and game.score >= 20:
            token3 = 1
            if token1 == 1 and token2 == 1 and token3 == 1:
                victoire()
        elif game.chrono == 180 and map == 3 and game.score <20 :
            game.puissance_game = 60
            main_menu()


            game.score =0
            game.chrono = 0

        balloon_group.draw(window)
        pygame.display.update()


if __name__ == "__main__":
    main_menu()
