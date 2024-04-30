import pygame
import time

pygame.init()

window = pygame.display.set_mode((800, 500))
pygame.display.set_caption("Menu")


font = pygame.font.SysFont('Helvetic', 20)

def background (lien,pos_x,pos_y) :
    fond = pygame.image.load(lien)
    fond = fond.convert_alpha()
    fond = pygame.transform.smoothscale(fond, window.get_size())
    window.blit(fond, (pos_x, pos_y))
    pygame.display.flip()

"""def Boutton_image (lien,pos_x,pos_y,taille_x,taille_y) :

    Bouton_menu = pygame.image.load(lien)
    Bouton_menu = Bouton_menu.convert_alpha()
    Bouton_menu = pygame.transform.smoothscale(Bouton_menu, (taille_x, taille_y))
    window.blit(Bouton_menu, (pos_x, pos_y))
    pygame.display.flip()
    Bouton_menu_rect = pygame.draw.circle(window,(255,0,0),(200,100),50)
    return Bouton_menu_rect"""

def main_menu():
    #play_button = Boutton_image("Start1.png", 300, 100, 200, 150)
    #quit_button = Boutton_image("Exit.png", 300, 250, 200, 150)
    start_bouton = pygame.draw.circle(window, (255, 0, 0), (400, 250), 30)
    quit_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(725, 0, 75, 80))


    while True:

        background("terrain3.png", 0, 0)
        time.sleep(0.5)
        background("terrain4.png", 0, 0)
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

    map1_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(70, 100, 225, 125))
    map2_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(515, 100, 225, 125))
    map3_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(285, 260, 225, 125))
    quit_bouton = pygame.draw.rect(window, (255, 0, 0), pygame.Rect(725, 0, 75, 80))
    background("menu2.png", 0, 0)
    while run:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if quit_bouton.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                if map1_bouton.collidepoint(pygame.mouse.get_pos()):
                    map1()
                if map2_bouton.collidepoint(pygame.mouse.get_pos()):
                    map2()
                if map3_bouton.collidepoint(pygame.mouse.get_pos()):
                    map2()


        pygame.display.update()

def map1 () :
    #choisis le background que tu veux et tu codes les choses spécifiques a la map ici
    background("terrain2.png", 0, 0)
def map2 () :
    # choisis le background que tu veux et tu codes les choses spécifiques a la map ici
    background("terrain2.png", 0, 0)

def map3 () :
    # choisis le background que tu veux et tu codes les choses spécifiques a la map ici
    background("terrain2.png", 0, 0)


if __name__ == "__main__":
    main_menu()
