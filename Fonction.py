import pygame
pygame.init()

from Constant import dt
from Constant import mass
from Constant import restit
from Constant import P_image_w
from Constant import P_image_h
from Constant import C_max_hitbox_x
from Constant import C_max_hitbox_y
from Constant import B_max_hitbox_x
from Constant import B_max_hitbox_y
from Constant import P_max_hitbox_x
from Constant import P_max_hitbox_y

from Init import ground
from Init import P1
from Init import P2
from Init import Balle
from Init import Cage_1
from Init import Cage_2
from Init import Score
from Init import Fleche
from Init import Tuto

from Graphics import win
from Graphics import fond


#print et change le score
font_name = pygame.font.match_font('arial')
def draw_text(surface, texte, taille, x, y):
    font = pygame.font.Font(font_name, taille)
    text_surface = font.render(texte, True, (0,0,0))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    surface.blit(text_surface, text_rect)

# permet de remettre les personnages dans une bonne position une fois un point marqué
def fin_du_game():
    Balle.x = 460
    Balle.y = ground

    P1.isJump = False
    P1.jumpCount = 6
    P1.x = 260
    P1.y = ground

    P2.isJump = False
    P2.jumpCount = 6
    P2.x = 660
    P2.y = ground

#fonction force appliquer sur la balle constament
def force(fx, fy):

    ax = fx / mass
    ay = fy / mass
    Balle.vx += ax * dt
    Balle.vy += ay * dt

#fonction force a appliquer lorsque la balle rentre en contact avec le sol ou les mur notament
def forcecontact(nx, ny):
    vNormal = Balle.vx * nx + Balle.vy * ny
    fNormal = -(restit + 1) * vNormal * mass / dt

    fx = fNormal * nx
    fy = fNormal * ny

    force(fx, fy)

# permet les collisions entre la balle et les différents éléments
def collision_balle(Objet_x, Objet_y, Max_hitbox_x, Max_hitbox_y, velocity):
    if (Balle.x + (B_max_hitbox_x/2)> Objet_x + (Max_hitbox_x) / 2):
        if (Balle.vx <= 0):
            Balle.vx = 0
            Balle.vx += velocity
        Balle.vx += velocity

    if (Balle.x + (B_max_hitbox_x/2)< Objet_x + (Max_hitbox_x) / 2):
        if (Balle.vx >= 0):
            Balle.vx = 0
            Balle.vx -= velocity
        Balle.vx -= velocity

    if (Balle.y + (B_max_hitbox_y/2)> Objet_y + (Max_hitbox_y)):
        if (Balle.vy <= 0):
            Balle.vy = 0
            Balle.vy += velocity
        Balle.vy += velocity

    if (Balle.y + (B_max_hitbox_y/2)< Objet_y + (Max_hitbox_y)):
        if (Balle.vy >= 0):
            Balle.vy = 0
            Balle.vy -= velocity
        Balle.vy -= velocity
    return (Balle.vx, Balle.vy)

#permet de rafraichir la page
def redrawGameWindow():
    win.blit(fond, (0, 0))

    # Si dans le tuto
    if Score.tuto == 1:
        Tuto.draw(win)
        draw_text(win, "PRESS W TO RETURN", 20, 990 / 2, 500)

    #Si dans le menu
    if Score.menu == 0:
        draw_text(win, "BALL HEAD", 150, 990 / 2, 10)
        draw_text(win, "PLAY", 100, 990 / 2, 200)
        draw_text(win, "TUTORIAL", 100, 990 / 2, 330)
        draw_text(win, "PRESS A TO CONTINUE", 20, 990 / 2, 500)
        Fleche.draw(win)

    # Si dans le jeu
    if Score.menu == 1:
        P1.draw(win)
        P2.draw(win)
        Balle.draw(win)
        Cage_1.draw(win)
        Cage_2.draw(win)
        draw_text(win, (str(Score.scoreP1)+" : "+str(Score.scoreP2)), 70, 990/2, 10)

        # Si il y a un gagnant
        if Score.wining == 1:
            draw_text(win, "PRESS A TO RESTART", 20, 990 / 2, 220)
            if (Score.scoreP1 > 4):
                draw_text(win, "P1 WIN", 100, 990 / 2, 100)
            if (Score.scoreP2 > 4):
                draw_text(win, "P2 WIN" , 100, 990 / 2, 100)

    pygame.display.update()

#permet de finir une partie
def resetGame():
    if ((Score.scoreP1 > 4) or (Score.scoreP2 > 4)):
        Score.wining = 1

    fin_du_game()
    Balle.vx = 0
    Balle.vy = 0

#permet le mouvement des joueurs
def PlayerMouv(PlayerX, PlayerY, OPlayerX, OPlayerY, PlayerV, OPlayerV, CageX, CageY, PL, PR, OPlayeron, OPlayerjump, direction):
    # On vérifie que le player n'est pas dans la hitbox des cages
    if not ((PlayerX > CageX - P_image_w) and (PlayerX < CageX + C_max_hitbox_x) and (PlayerY > CageY - P_image_h) and (PlayerY < CageY + C_max_hitbox_y)):

        # On vérifie si le player va a vers la gauche(-1)
        if direction<0:
            PL = True
            PR = False

            # On vérifie si Player est en contact direct avec OPlayer
            if ((PlayerX + P_image_w > OPlayerX) and (PlayerX < OPlayerX + P_image_w) and (PlayerY + (P_image_h - 10) > OPlayerY) and (PlayerX > OPlayerX) and (OPlayeron == False)):

                # On vérifie si OPlayer saute et si Player et OPlayer se touche
                if ((OPlayerjump == True) and (PlayerY - (P_image_h - 10) < OPlayerY)):
                    if OPlayerX > 0:
                        PlayerX -= PlayerV / 2
                        OPlayerX -= OPlayerV / 2 + 0.1

                # On vérifie si OPlayer saute et si Player et OPlayer se touche
                if ((OPlayerjump == True) and (PlayerY > OPlayerY + (P_image_h - 10))):
                    PlayerX -= PlayerV

                # On vérifie si OPlayer est au sol
                if (OPlayerjump == False):
                    if OPlayerX > 0:
                        PlayerX -= PlayerV / 2
                        OPlayerX -= OPlayerV / 2 + 0.1
            else:
                PlayerX -= PlayerV

        # Quasiment pareil que pour la gauche mais en inversant
        if direction>0:
            PL = False
            PR = True

            if ((PlayerX + P_image_w > OPlayerX) and (PlayerX < OPlayerX + P_image_w) and (PlayerY + (P_image_h - 10) > OPlayerY) and (PlayerX < OPlayerX) and (OPlayeron == False)):

                if ((OPlayerjump == True) and (PlayerY - (P_image_h - 10) < OPlayerY)):
                    if OPlayerX < 900:
                        PlayerX += PlayerV / 2
                        OPlayerX += OPlayerV / 2 + 0.1

                if ((OPlayerjump == True) and (PlayerY > OPlayerY + (P_image_h - 10))):
                    PlayerX += PlayerV

                if (OPlayerjump == False):
                    if OPlayerX < 900:
                        PlayerX += PlayerV / 2
                        OPlayerX += OPlayerV / 2 + 0.1
            else:
                PlayerX += PlayerV

    # On retourne la position X et actualisation de Player et de OPlayer ainsi que la direction actuelle de Player
    return(PlayerX, OPlayerX, PL, PR)