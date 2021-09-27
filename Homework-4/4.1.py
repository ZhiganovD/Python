import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400)) 
rect(screen, (255, 255, 255), (0,0,400,400))
circle(screen, (255, 255, 0), (200, 200), 150)
rect(screen, (0, 0, 0), (100,260,200,25))
circle(screen, (255, 0, 0), (130,150), 30)
circle(screen, (255, 0, 0), (270, 150), 25)
circle(screen, (0, 0, 0), (130,150), 10)
circle(screen, (0, 0, 0), (270, 150), 10)
line(screen,(0,0,0),(75,55),(190,155),25)
line(screen,(0,0,0),(210,140),(325,85),20)
circle(screen, (0, 0, 0), (200, 200), 150,2)
circle(screen, (0, 0, 0), (130,150), 30,2)
circle(screen, (0, 0, 0), (270, 150), 25,2)
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
