import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))
rect(screen, (255, 255, 255), (0,0,400,400)) #фон, а то на черном ничего не видно
def draw_leye(x,y,r,colour): #левый глаз
    circle(screen, colour, (x,y), r+20),
    circle(screen, (0, 0, 0), (x,y), r)
def draw_reye(x,y,r,colour): #правый глаз
    circle(screen, colour, (x,y), r+15),
    circle(screen, (0, 0, 0), (x,y), r)
def draw_mouth(x,y,l,h,colour): #рот
    rect(screen, colour, (x,y,l,h))
def draw_lbrush(x1,y1,x2,y2,h,colour): #левая бровь
    line(screen,colour,(x1,y1),(x2,y2),h)
def draw_rbrush(x1,y1,x2,y2,h,colour): #правая бровь
    line(screen,colour,(x1,y1),(x2,y2),h)
def draw_smile(x,y,r,colour):
    circle(screen, colour, (x, y), r), #самый большой круг
    draw_leye(130,150,10,(255, 0, 0)),
    draw_reye(270,150,10,(255, 0, 0)),
    draw_mouth(100,260,200,25,(0,0,0)),
    draw_lbrush(75,55,190,155,25,(0,0,0)),
    draw_rbrush(210,140,325,85,20,(0,0,0))
draw_smile(200,200,150,(255,255,0)) #и рисуем

#не судите строго, с таким углом у бровей он выглядит еще более злобно
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
