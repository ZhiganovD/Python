import math
import numpy as np
import pygame
import sys

from pygame.constants import VIDEOEXPOSE
import solar_helper as SH
from pygame.draw import *
pygame.init()

pygame.font.init() #для надписей
myfont = pygame.font.SysFont('Comic Sans MS', 30) #шрифты для надписи

FPS = 30
screen = pygame.display.set_mode((SH.a_sc, SH.b_sc)) #создание экрана

#background = pygame.image.load("C:\\Users\\User\\Desktop\\python3\\Universal_sandbox\\Images\\Star-Sky.jpg")
#screen.blit(background,(0,0))


class HeavObj:
    def __init__(self, x, y, Vx, Vy, radius, mass, color, screen):
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.color = color
        self.r = radius
        self.m = mass
        self.screen = screen
    
    def move (self, m, x, y):
        l = lenght (x, y, self.x, self.y)
        a = SH.G * m / (l ** 2)
        V = np.sqrt (a * l)
        if self.y > y :
         self.Vx = V * (np.abs(y - self.y) / l)
        elif self.y <= y :
         self.Vx =(-1) * V * (np.abs(y - self.y) / l)
        if self.x < x :
         self.Vy = V * (np.abs(x - self.x) / l)
        elif self.x > x :
         self.Vy =(-1) * V * (np.abs(x - self.x) / l)
        self.x += self.Vx
        self.y += self.Vy

    def move_start (self):
        self.x += self.Vx

    def draw (self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r )

def lenght (x1, y1, x2, y2):
    l = np.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2)
    return l

pygame.display.update()
clock = pygame.time.Clock()
finished = False
finished0 = False
screen.fill(SH.WHITE)

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
             screen.fill(SH.WHITE)
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

pygame.init()

stars = []
for i in range(0, SH.star_num):
    new_star = HeavObj(SH.sun_x, SH.sun_y, SH.sun_Vx, SH.sun_Vy, SH.sun_r, SH.sun_m, SH.sun_c, screen)
    stars.append(new_star)

planets = []
for i in range(0, SH.planet_num):
    new_planet = HeavObj(SH.e_x, SH.e_y, SH.e_Vx, SH.e_Vy, SH.e_r, SH.e_m, SH.e_c, screen)
    planets.append(new_planet)

while not finished:
    screen.fill(SH.WHITE)
    
    for a in stars:
        a.draw()
    
    for b in planets:
        b.draw()

    clock.tick(FPS)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
    
    for b in planets:
        b.move(SH.sun_m, SH.sun_x, SH.sun_y)

pygame.quit()
