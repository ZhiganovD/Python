import math
import numpy as np
import pygame
import sys
from pygame.draw import *
pygame.init()

pygame.font.init() #для надписей
myfont = pygame.font.SysFont('Comic Sans MS', 30) #шрифты для надписи

FPS = 30
a_sc = 700 #длина экрана
b_sc = 700 #ширина экрана
screen = pygame.display.set_mode((a_sc, b_sc)) #создание экрана

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class HeavObj:
    def __init__(self, x, y, Vx, Vy, radius, mass, color):
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.color = color
        self.r = radius
        self.m = mass



pygame.display.update()
clock = pygame.time.Clock()
finished = False
finished0 = False
finished1 = False
screen.fill(WHITE)

x1 = 260
y1 = 300
l1 = 200
x2 = 250
y2 = 370
l2 = 100
x3 = 270
y3 = 440
l3 = 150
h = 30

textsurface = myfont.render('Start game', False, (0, 0, 0))  #надпись в центре экрана
screen.blit(textsurface,(x1, y1))
textsurface1 = myfont.render('Leaderboard', False, (0, 0, 0))  #надпись в центре экрана
screen.blit(textsurface1,(x2, y2))
textsurface2 = myfont.render('Exit game', False, (0, 0, 0))  #надпись в центре экрана
screen.blit(textsurface2,(x3, y3))
pygame.display.update()

while not finished0:
    clock.tick(FPS)
    for click in pygame.event.get():
        if click.type == pygame.MOUSEBUTTONDOWN: #нажата кнопка мыши
         if click.button == 1 and click.pos[0] < (x1 + l1) and click.pos[0] > (x1) and click.pos[1] < (y1 + h) and click.pos[1] > (y1 - h): 
             finished0 = True
         if click.button == 1 and click.pos[0] < (x2 + l2) and click.pos[0] > (x2) and click.pos[1] < (y2 + h) and click.pos[1] > (y2 - h):
             screen.fill(WHITE)
             if click.type == pygame.MOUSEBUTTONDOWN: #нажата кнопка мыши
                  if click.button == 3: #если нажал ПКМ
                       sys.exit() #выключение программы
             if click.type == pygame.QUIT:
                   sys.exit() #выключение программы
             pygame.display.update()
         if click.button == 1 and click.pos[0] < (x3 + l3) and click.pos[0] > (x3) and click.pos[1] < (y3 + h) and click.pos[1] > (y3 - h):
             sys.exit() #выключение программы
        if click.type == pygame.QUIT:
             sys.exit() #выключение программы

