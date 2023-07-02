import pygame

from Constant import P_max_hitbox_x
from Constant import P_max_hitbox_y
from Constant import C_max_hitbox_x
from Constant import C_max_hitbox_y
from Constant import B_max_hitbox_x
from Constant import B_max_hitbox_y
from Constant import P_image_w
from Constant import P_image_h

from Constant import g
from Constant import radius
from Constant import dt
from Constant import mass
from Constant import screen_lenght

from Init import ground
from Init import P1
from Init import P2
from Init import Balle
from Init import Cage_1
from Init import Cage_2
from Init import Score
from Init import Fleche

from Fonction import force
from Fonction import forcecontact
from Fonction import collision_balle
from Fonction import redrawGameWindow
from Fonction import resetGame
from Fonction import PlayerMouv


from pygame import mixer
pygame.init()

#nom du screen
pygame.display.set_caption("Ball Head")

#Charger les sons
mixer.music.load('sons/ost.wav')
pygame.mixer.music.set_volume(0.05)
#jouer la musique
mixer.music.play(-1)

# création du "temps"
clock = pygame.time.Clock()

#loop principale
run = True
while run:
    # création du "temps" 2
    clock.tick(64)

    for event in pygame.event.get():
        # permet la fermeture de la page sans crash
        if event.type == pygame.QUIT:
            run = False

    # initialisation de la reconnaisance des touches
    keys = pygame.key.get_pressed()

    #////////// On allume le jeu ////////

    # ////// On est dans le tuto /////
    if (Score.menu == 2):
        if (Score.tuto == 1) and keys[pygame.K_w]:
            Score.tuto = 0
            Score.menu = 0

    # ////// On est dans le menu /////
    if (Score.menu == 0) :

        if keys[pygame.K_a] and (Fleche.position == 0):
            Score.menu = 1
        if keys[pygame.K_a] and (Fleche.position == 1):
            Score.tuto = 1
            Score.menu = 2

        # Gestion du mouvement de la fleche
        if keys[pygame.K_UP] and (Fleche.position == 1):
            Fleche.position = 0
            Fleche.y = 170
        if keys[pygame.K_DOWN] and (Fleche.position == 0):
            Fleche.position = 1
            Fleche.y = 300

    # ////////// On passe au jeu ////////
    if Score.menu == 1:
        # ////////// les resultats //////////
        if Score.wining == 1:
            if keys[pygame.K_a]:
                # Si "a" est pressé: on reset la partie
                Score.wining = 0
                Score.scoreP1 = 0
                Score.scoreP2 = 0


        # /////////// en jeu /////////////
        if Score.wining == 0:
            # ///// mouvement P1 /////

            # /// gauche ///
            if keys[pygame.K_q] and P1.x > P1.vel:
                (P1.x, P2.x, P1.left, P1.right) = PlayerMouv(P1.x, P1.y, P2.x, P2.y, P1.vel, P2.vel, Cage_2.x, Cage_2.y, P1.left,P1.right, P2.isonP1, P2.isJump, -1)

            # /// droite ///
            elif keys[pygame.K_d] and P1.x < (screen_lenght - P_image_w + P1.vel):
                (P1.x, P2.x, P1.left, P1.right) = PlayerMouv(P1.x, P1.y, P2.x, P2.y, P1.vel, P2.vel, Cage_1.x, Cage_1.y,P1.left, P1.right, P2.isonP1, P2.isJump, 1)

            # /// pas de mouvement ///
            else:
                P1.right = False
                P1.left = False
                P1.walkCount = 0

            # /// saut ///

            # On vérifie si P1 est en plein saut
            if not (P1.isJump):
                # On vérifie si la touche z est enfoncé
                if keys[pygame.K_z]:
                    P1.isJump = True
                    P1.right = False
                    P1.left = False
                    P1.walkCount = 0
            else:
                # On vérifie si le début du saut est enclencher
                if P1.beginJump == True:
                    P1.y-=1

                # On vérifie si le P1 est au niveau du sol (350)
                if P1.y < ground:
                    # On vérifie si le P1 a commencer a sauter
                    if P1.beginJump == True:
                        P1.y += 1
                        P1.beginJump = False

                    neg = 0
                    # on vérifie si le P1 rentre dans la hitbox de la cage
                    if ((P1.x > Cage_1.x - P_image_w+10) and (P1.x < Cage_1.x + (C_max_hitbox_x)) and (P1.y > Cage_1.y - P_image_h) and (P1.y < Cage_1.y + C_max_hitbox_y)):
                        # Si P1 rentre dans la hitbox de la cage on le fait redecendre
                        P1.jumpCount = -2
                    if ((P1.x > Cage_2.x - P_image_w) and (P1.x < Cage_2.x + (C_max_hitbox_x-10)) and (P1.y > Cage_2.y - P_image_h) and (P1.y < Cage_2.y + C_max_hitbox_y)):
                        P1.jumpCount = -2

                    # on vérifie si le P1 est en train de monter/ descendre
                    if P1.jumpCount > 0:
                        neg = -1
                    else :
                        neg = +1

                    # Ici on met a jour la hauteur de P1 et de P2 si il est sur P1
                    P1.y += (P1.jumpCount ** 2) * 0.5 * neg
                    if (P2.isonP1 == True):
                        P2.y += (P1.jumpCount ** 2) * 0.5 * neg
                    P1.jumpCount -= 0.25

                # on vérifie si le P1 est au sol (350)
                if P1.y >= ground:
                    P1.y = ground
                    P1.beginJump = True
                    P1.isJump = False
                    P1.jumpCount = 6

                # on vérifie si P1 se situe sur de P2
                if ((P1.x + (P_image_w-6) > P2.x) and (P1.x -(P_image_w-6)< P2.x) and (P1.y + P_image_h > P2.y) and (P2.y- P_image_h<P1.y) and (P2.isonP1 == False) and (P1.isonP2 == False) and (P1.y<P2.y)):
                    P1.isonP2 = True
                    P1.beginJump = True
                    P1.isJump = False
                    P1.jumpCount = 6

            # on vérifie si P1 se situe sur de P2
            if not ((P1.x + (P_image_w-6) > P2.x) and (P1.x - (P_image_w-6)< P2.x) and (P1.y + P_image_h > P2.y) and (P2.y- P_image_h<P1.y)):
                if (P1.isonP2 == True) and (P1.isJump == False):
                    P1.isonP2 = False
                    P1.isJump = True
                    P1.jumpCount = -1
                if (P1.isonP2 == True) and (P1.isJump == True):
                    P1.isonP2 = False




            # mouvement P2
            # gauche
            if keys[pygame.K_LEFT] and P2.x > P2.vel:
                (P2.x, P1.x, P2.left, P2.right) = PlayerMouv(P2.x, P2.y, P1.x, P1.y, P2.vel, P1.vel, Cage_2.x, Cage_2.y,P2.left, P2.right, P1.isonP2, P1.isJump, -1)

            # droite
            elif keys[pygame.K_RIGHT] and P2.x < (screen_lenght - P_image_w + P2.vel):
                (P2.x, P1.x, P2.left, P2.right) = PlayerMouv(P2.x, P2.y, P1.x, P1.y, P2.vel, P1.vel, Cage_1.x, Cage_1.y,P2.left, P2.right, P1.isonP2, P1.isJump, 1)

            # pas de mouvement
            else:
                P2.right = False
                P2.left = False
                P2.walkCount = 0

            # saut (pareil que pour P1 mais en inversant les deux)
            if not (P2.isJump):
                if keys[pygame.K_UP]:
                    P2.isJump = True
                    P2.right = False
                    P2.left = False
                    P2.walkCount = 0
            else:
                if P2.beginJump == True:
                    P2.y -= 1

                if P2.y < ground:
                    if P2.beginJump == True:
                        P2.y += 1
                        P2.beginJump = False
                    neg = 0
                    if ((P2.x > Cage_1.x - P_image_w+10) and (P2.x < Cage_1.x + (C_max_hitbox_x-10)) and (P2.y > Cage_1.y - P_image_h) and (P2.y < Cage_1.y + C_max_hitbox_y)):
                        P2.jumpCount = -2
                    if ((P2.x > Cage_2.x - P_image_w) and (P2.x < Cage_2.x + (C_max_hitbox_x-10)) and (P2.y > Cage_2.y - P_image_h) and (P2.y < Cage_2.y + C_max_hitbox_y)):
                        P2.jumpCount = -2
                    if P2.jumpCount > 0:
                        neg = -1
                    else:
                        neg = +1
                    P2.y += (P2.jumpCount ** 2) * 0.5 * neg
                    if (P1.isonP2 == True):
                        P1.y += (P2.jumpCount ** 2) * 0.5 * neg
                    P2.jumpCount -= 0.25

                if P2.y >= ground:
                    P2.y = ground
                    P2.beginJump = True
                    P2.isJump = False
                    P2.jumpCount = 6

                if ((P2.x + (P_image_w-6) > P1.x) and (P2.x - (P_image_w-6)< P1.x) and (P2.y + P_image_h > P1.y) and (P1.y- P_image_h<P2.y) and (P1.isonP2 == False) and  (P2.isonP1 == False) and (P2.y<P1.y)):
                    P2.isonP1 = True
                    P2.beginJump = True
                    P2.isJump = False
                    P2.jumpCount = 6

            if not ((P2.x + (P_image_w-6) > P1.x) and (P2.x - (P_image_w-6)< P1.x) and (P2.y + P_image_h > P1.y) and (P1.y- P_image_h<P2.y)):
                if (P2.isonP1 == True) and (P2.isJump == False):
                    P2.isonP1 = False
                    P2.isJump = True
                    P2.jumpCount = -1
                if (P2.isonP1 == True) and (P2.isJump == True):
                    P2.isonP1 = False


            # mouvement de la balle
            force(0, mass * g)
            Balle.x += Balle.vx * dt
            Balle.y += Balle.vy * dt
            Balle.angle = Balle.angle+Balle.vy

            #reduction du mouvement au cours du temps
            if (Balle.vx > 0):
                Balle.vx -= 0.05
            if (Balle.vx < 0):
                Balle.vx += 0.05
            if (Balle.vx < 1) and (Balle.vx > -1):
                Balle.vx = 0

            # On verifie si la balle touche le sol ou les murs
            if (Balle.x <= B_max_hitbox_x - radius):
                Balle.x = B_max_hitbox_x - radius
                forcecontact(1, 0)
            if Balle.x >= (990 - radius):
                Balle.x = 990 - radius
                forcecontact(-1, 0)
            if Balle.y <= B_max_hitbox_y - radius:
                Balle.y = B_max_hitbox_y - radius
                forcecontact(0, 1)
            if Balle.y >= (460 - radius):
                Balle.y = 460 - radius
                forcecontact(0, -1)


            # if Balle.hitbox == P1.hitbox :
            if ((Balle.x > P1.x- B_max_hitbox_x) and (Balle.x < P1.x+ P_max_hitbox_x) and (Balle.y > P1.y- B_max_hitbox_y) and (Balle.y < P1.y+ P_max_hitbox_y)):
                (vx, vy) = collision_balle(P1.x, P1.y,P_max_hitbox_x, P_max_hitbox_y, 2)

            # if Balle.hitbox == P2.hitbox :
            if ((Balle.x > P2.x-B_max_hitbox_x) and (Balle.x < P2.x+ P_max_hitbox_x) and (Balle.y > P2.y- B_max_hitbox_y) and (Balle.y < P2.y+ P_max_hitbox_y)):
                (vx, vy) = collision_balle(P2.x, P2.y, P_max_hitbox_x, P_max_hitbox_y, 2)

            # if Balle.hitbox == Cage1.hitbox :
            if ((Balle.x > Cage_1.x - B_max_hitbox_x) and (Balle.x < Cage_1.x + C_max_hitbox_x) and (Balle.y > Cage_1.y - B_max_hitbox_y) and (Balle.y < Cage_1.y + C_max_hitbox_y)):
                (vx, vy) = collision_balle(Cage_1.x, Cage_1.y, C_max_hitbox_x, C_max_hitbox_y, 2)

            # if Balle.hitbox == Cage2.hitbox :
            if ((Balle.x > Cage_2.x - B_max_hitbox_x) and (Balle.x < Cage_2.x + C_max_hitbox_x) and (Balle.y > Cage_2.y - B_max_hitbox_y) and (Balle.y < Cage_2.y + C_max_hitbox_y)):
                (vx, vy) = collision_balle(Cage_2.x, Cage_2.y, C_max_hitbox_x, C_max_hitbox_y, 2)

            # if Balle.hitbox == Cage1.goalbox :
            if ((Balle.x > Cage_1.x - B_max_hitbox_x +30) and (Balle.x < Cage_1.x + 100+30) and (Balle.y > Cage_1.y - B_max_hitbox_y+10) and (Balle.y < Cage_1.y + 230+10)):
                Score.scoreP1 += 1
                resetGame()

            # if Balle.hitbox == Cage2.goalbox :
            if ((Balle.x > Cage_2.x - B_max_hitbox_x) and (Balle.x < Cage_2.x + 100) and (Balle.y > Cage_2.y - B_max_hitbox_y+10) and (Balle.y < Cage_2.y + 230+10)):
                Score.scoreP2 += 1
                resetGame()

    # On actualise la page (refresh)
    redrawGameWindow()

pygame.quit()