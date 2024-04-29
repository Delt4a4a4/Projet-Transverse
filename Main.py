import pygame
import math
from Game import Game
import Ballon
pygame.init()
from Ballon import Ballon
from Panier import Panier
from Background import Fondecran

#pygame_icon = pygame.image.load("chemin")
pygame.display.set_mode((800,500))
#pygame.display.set_icon(pygame_icon)
game = Game()
pygame.display.set_caption("SuperBasketBall ver1.22 474 487 139")
fondecran = Fondecran(game)
screen = pygame.display.set_mode((1520,800))

if fondecran.niveau == 0 :
    background = pygame.image.load("Image/EcJikeZU8AA42Jq.jpg")
elif fondecran.niveau == 1 :
    background = pygame.image.load("Image/EcJikeZU8AA42Jq.jpg")
elif fondecran.niveau == 2 :
    background = pygame.image.load("Image/EcJikeZU8AA42Jq.jpg")
else :
    background = pygame.image.load("Image/EcJikeZU8AA42Jq.jpg")

running = True

'''Welcome_logo = pygame.image.load("chemin")
start_button = pygame.image.load("chemin")
start_button_rect = start_button.get_rect()
start_button_rect.x = math.ceil(screen.get_width() / 3.33)
start_button_rect.y = math.ceil(screen.get_height() / 2)'''


while running:
    background = pygame.image.load("Image/EcJikeZU8AA42Jq.jpg")
    pygame.display.flip()
    background=background.convert_alpha()
    background=pygame.transform.smoothscale(background,screen.get_size())
    screen.blit(background, (0, 0))

    screen.blit(game.ballon.image, game.ballon.rect)

    if game.is_playing:
        # déclencher les instructions du jeu
        game.update(screen)
        Panier.spawn_panier(Panier)

    for action in pygame.event.get():
        # fermeture de la fenetre
        if action.type == pygame.QUIT:
            running = False
            pygame.quit()