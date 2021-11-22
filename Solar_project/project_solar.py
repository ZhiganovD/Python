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
    def __init__(self, x, y, Vx, Vy, radius, mass, color, screen, type):
        self.x = x
        self.y = y
        self.Vx = Vx
        self.Vy = Vy
        self.color = color
        self.r = radius
        self.m = mass
        self.screen = screen
        self.type = type
    
    def move (self, m, x, y):
        l = lenght (x, y, self.x, self.y)
        a = SH.G * m / (l ** 2)
        V = np.sqrt (a * l)
        self.Vy += a * ((y - self.y) / l)
        self.Vx += a * ((x - self.x) / l)
        self.x += self.Vx
        self.y += self.Vy

    def hit( self, x, y, r, type, m):
        l = lenght (x, y, self.x, self.y)
        if l < r + self.r:
            if type < self.type:
                self.r = 0
                return 0
            elif type == self.type:
                if m <= self.m:
                    self.m += m
                    self.r += r
                    return 1
                else:
                    return 2
            else:
                self.m += m
                self.r += r
                return 1

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
    new_star = HeavObj(SH.sun_x, SH.sun_y, SH.sun_Vx, SH.sun_Vy, SH.sun_r, SH.sun_m, SH.sun_c, screen, SH.sun_type)
    stars.append(new_star)

planets = []
for i in range(0, SH.planet_num):
    new_planet = HeavObj(SH.par[i][0], SH.par[i][1], SH.par[i][2], SH.par[i][3], SH.par[i][4], SH.par[i][5], SH.par[i][6], screen, SH.par[i][7])
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

    for b in planets:
        for a in stars:
            if b.hit(a.x, a.y, a.r, a.type, a.m) == 0:
                a.m += b.m
            elif b.hit(a.x, a.y, a.r, a.type, a.m) == 1:
                a.r = 0
            elif b.hit(a.x, a.y, a.r, a.type, a.m) == 2:
                a.r += b.r
                a.m += b.m
                b.r = 0


pygame.quit()
