import pygame
pygame.init()

from Constant import screen_lenght

# création du screen
win = pygame.display.set_mode((screen_lenght,540))

# Charger les images

# JEUX
idleP1 = pygame.image.load('graphisme/p1 walk-0.png')

walkP1 = [pygame.image.load('graphisme/p1 walk-0.png'), pygame.image.load('graphisme/p1 walk-1.png'),
          pygame.image.load('graphisme/p1 walk-2.png'), pygame.image.load('graphisme/p1 walk-3.png'),
          pygame.image.load('graphisme/p1 walk-4.png'), pygame.image.load('graphisme/p1 walk-5.png'),
          pygame.image.load('graphisme/p1 walk-6.png'), pygame.image.load('graphisme/p1 walk-7.png'),
          pygame.image.load('graphisme/p1 walk-8.png'), pygame.image.load('graphisme/p1 walk-9.png'),
          pygame.image.load('graphisme/p1 walk-10.png'), pygame.image.load('graphisme/p1 walk-11.png'),
          pygame.image.load('graphisme/p1 walk-12.png'), pygame.image.load('graphisme/p1 walk-13.png'),
          pygame.image.load('graphisme/p1 walk-14.png'), pygame.image.load('graphisme/p1 walk-15.png')]

idleP2 = pygame.image.load('graphisme/p2 walk-0.png')

walkP2 = [pygame.image.load('graphisme/p2 walk-0.png'), pygame.image.load('graphisme/p2 walk-1.png'),
          pygame.image.load('graphisme/p2 walk-2.png'), pygame.image.load('graphisme/p2 walk-3.png'),
          pygame.image.load('graphisme/p2 walk-4.png'), pygame.image.load('graphisme/p2 walk-5.png'),
          pygame.image.load('graphisme/p2 walk-6.png'), pygame.image.load('graphisme/p2 walk-7.png'),
          pygame.image.load('graphisme/p2 walk-8.png'), pygame.image.load('graphisme/p2 walk-9.png'),
          pygame.image.load('graphisme/p2 walk-10.png'), pygame.image.load('graphisme/p2 walk-11.png'),
          pygame.image.load('graphisme/p2 walk-12.png'), pygame.image.load('graphisme/p2 walk-13.png'),
          pygame.image.load('graphisme/p2 walk-14.png'), pygame.image.load('graphisme/p2 walk-15.png')]

fond = pygame.image.load('graphisme/fond.jpg')

ball = pygame.image.load('graphisme/ball.png')

cage1 = pygame.image.load('graphisme/goal_1.png')

cage2 = pygame.image.load('graphisme/goal_2.png')

# MENU
fleche = pygame.image.load('graphisme/fleche.png')

tuto = pygame.image.load('graphisme/Tuto.png')