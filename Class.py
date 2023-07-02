import pygame

from Graphics import walkP1
from Graphics import walkP2
from Graphics import idleP1
from Graphics import idleP2
from Graphics import cage1
from Graphics import cage2
from Graphics import ball
from Graphics import fleche
from Graphics import tuto

from Constant import hitbox
from Constant import P_mouv_speed
from Constant import P_max_hitbox_x
from Constant import P_max_hitbox_y
from Constant import C_max_hitbox_x
from Constant import C_max_hitbox_y
from Constant import B_max_hitbox_x
from Constant import B_max_hitbox_y

pygame.init()

# création Player
class Player(object):
    def __init__(self, x, y):
        # initialisation
        self.x = x
        self.y = y

        # velocité/vitesse
        self.vel = P_mouv_speed

        # condition
        self.isJump = False
        self.beginJump = True
        self.isonP2 = True
        self.isonP1 = True
        self.left = False
        self.right = False
        self.walk = False

        # permet de savoir quel frame afficher
        self.walkCount = 0
        # puissance saut
        self.jumpCount = 6


# création P1
class Player1(Player):
    def draw(self, win):
        # Reset la boucle de l'animation (frame 16 à frame 1)
        if self.walkCount + 1 >= 32:
            self.walkCount = 0
        if self.walkCount + 1 <= -1:
            self.walkCount = 31

        # Animation de marche
        if self.right:
            win.blit(walkP1[self.walkCount // 2], (self.x, self.y))
            self.walkCount += 1

        elif self.left:
            win.blit(walkP1[self.walkCount // 2], (self.x, self.y))
            self.walkCount -= 1

        # Animation de IDLE (non marche/non saut)
        else:
            win.blit(idleP1, (self.x, self.y))

        if hitbox == 1:
            # dessiner la hitbox
            self.hitbox = (self.x - 5, self.y, P_max_hitbox_x, P_max_hitbox_y)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


# création P2
class Player2(Player):
    def draw(self, win):
        # Reset la boucle de l'animation (frame 16 à frame 1)
        if self.walkCount + 1 >= 32:
            self.walkCount = 0
        if self.walkCount + 1 <= -1:
            self.walkCount = 31

        # Animation de marche
        if self.right:
            win.blit(walkP2[self.walkCount // 2], (self.x, self.y))
            self.walkCount -= 1

        elif self.left:
            win.blit(walkP2[self.walkCount // 2], (self.x, self.y))
            self.walkCount += 1

        # Animation de IDLE (non marche/non saut)
        else:
            win.blit(idleP2, (self.x, self.y))

        if hitbox == 1:
            # dessiner la hitbox
            self.hitbox = (self.x + 5, self.y, P_max_hitbox_x, P_max_hitbox_y)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)


# création Cage
class Cage(object):
    def __init__(self, x, y):
        # initialisation
        self.x = x
        self.y = y


# création Cage1
class Cage1(Cage):
    def draw(self, win):
        # Animation
        win.blit(cage1, (self.x, self.y))

        if hitbox == 1:
            # dessiner la hitbox
            self.hitbox = (self.x, self.y, C_max_hitbox_x, C_max_hitbox_y)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        if hitbox == 1:
            # dessiner la GOAL box
            self.goalbox = (self.x + 30, self.y + 10, 100, 230)
            pygame.draw.rect(win, (0, 255, 0), self.goalbox, 2)


# création Cage2
class Cage2(Cage):
    def draw(self, win):
        # Animation
        win.blit(cage2, (self.x, self.y))

        if hitbox == 1:
            # dessiner la hitbox
            self.hitbox = (self.x, self.y, C_max_hitbox_x, C_max_hitbox_y)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

        if hitbox == 1:
            # dessiner la GOAL box
            self.goalbox = (self.x, self.y + 10, 100, 230)
            pygame.draw.rect(win, (0, 255, 0), self.goalbox, 2)


# création Ball
class Ball(object):
    def __init__(self, x, y):
        # initialisation
        self.x = x
        self.y = y

        # limite dans l'écrant
        self.vel = 5
        self.direction = 1

        # paramètre balle
        self.vx = 0
        self.vy = 10
        self.angle = 0

    def draw(self, win):
        # Animation
        win.blit(ball, (self.x, self.y))

        if hitbox == 1:
            # dessiner la hitbox
            self.hitbox = (self.x, self.y, B_max_hitbox_x, B_max_hitbox_y)
            pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

# création Score
class Score(object):
    def __init__(self):
        self.scoreP1 = 0
        self.scoreP2 = 0
        self.wining = 0
        self.menu = 0
        self.tuto = 0

#Création Fleche
class Fleche(object):
    def __init__(self, x, y):
        # initialisation
        self.x = x
        self.y = y
        self.position = 0

    def draw(self, win):
        # Animation
        win.blit(fleche, (self.x, self.y))

#Création Tuto
class Tuto(object):
    def __init__(self, x, y):
        # initialisation
        self.x = x
        self.y = y

    def draw(self, win):
        # Animation
        win.blit(tuto, (self.x, self.y))
