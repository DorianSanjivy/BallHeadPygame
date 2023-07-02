import pygame
pygame.init()

from Class import Player1
from Class import Player2
from Class import Cage1
from Class import Cage2
from Class import Ball
from Class import Score
from Class import Fleche
from Class import Tuto

# intitialisation des positions de base
ground = 350
P1 = Player1(260, ground)
P2 = Player2(660, ground)
Balle = Ball(460, ground)
Cage_1 = Cage1(860, 220)
Cage_2 = Cage2(0, 220)
Score = Score()
Fleche = Fleche(100, 170)
Tuto = Tuto(0, 0)