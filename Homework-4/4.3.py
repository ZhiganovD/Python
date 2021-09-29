import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((700, 625))
rect(screen, (255, 204, 153), (0,0,700,140))
rect(screen, (255, 204, 204), (0,140,700,140))
def brline(x1,y1,x2,y2,x3,y3,l):
    polygon(screen,(255,128,0),[(x1,y1),(x2,y2),(x1,l)]),
    polygon(screen,(255,128,0),[(x3,y3),(x2,y2),(x3,l)]),
    polygon(screen,(255,128,0),[(x1,l),(x2,y2),(x3,l)])
brline(5,280,8,250,160,130,280)
brline(160,130,175,135,190,155,280)
brline(190,155,300,240,350,230,280)
brline(350,230,375,243,425,210,280)
brline(425,210,455,220,465,210,280)
brline(465,210,565,120,585,120,280)
brline(585,120,615,150,635,145,280)
brline(635,145,665,170,680,155,280)
brline(665,170,680,155,700,175,280)
polygon(screen,(255, 204, 204),[(210,280),(700,175),(700,280)])
circle(screen,(255,128,0),(572,121),12.99)
circle(screen,(255, 204, 204),(10,100),150)
circle(screen,(255, 204, 204),(490,130),70)
rect(screen, (255, 204, 153), (0,0,160,140))
rect(screen, (255, 204, 153), (420,0,140,140))
polygon(screen,(255,128,0),[(159,130),(160,140),(154,140)])
circle(screen,(255,255,0),(375,140),50)

rect(screen, (255, 204, 153), (0,280,700,140))

polygon(screen,(255,128,0),[(210,280),(3,320),(5,280)])
polygon(screen,(153,0,0),[(50,420),(0,320),(0,420)])
ellipse(screen, (153,0,0),(12,270,124,270))
polygon(screen,(153,0,0),[(50,420),(0,320),(0,420)])
rect(screen, (153,0,0), (0,400,700,20))
polygon(screen,(153,0,0),[(136,400),(156,330),(196,350)])
polygon(screen,(153,0,0),[(196,350),(216,290),(256,300)])
polygon(screen,(153,0,0),[(256,300),(296,340),(136,400)])
polygon(screen,(153,0,0),[(296,340),(356,320),(296,420)])
circle(screen,(153,0,0),(450,300),40)
polygon(screen,(153,0,0),[(356,320),(414,281),(390,420)])
polygon(screen,(153,0,0),[(50,420),(296,340),(296,420)])
polygon(screen,(153,0,0),[(296,420),(356,320),(390,420)])
polygon(screen,(153,0,0),[(484,280),(490,420),(550,330)]) #6
polygon(screen,(153,0,0),[(550,420),(490,420),(550,330)])
polygon(screen,(153,0,0),[(550,330),(590,290),(550,420)]) #5
polygon(screen,(153,0,0),[(590,290),(590,420),(550,420)])
polygon(screen,(153,0,0),[(590,290),(590,420),(620,300)]) #4
polygon(screen,(153,0,0),[(620,420),(590,420),(620,300)])
polygon(screen,(153,0,0),[(620,300),(620,420),(650,285)]) #3
polygon(screen,(153,0,0),[(650,420),(620,420),(650,285)])
polygon(screen,(153,0,0),[(650,285),(650,420),(670,290)]) #2
polygon(screen,(153,0,0),[(670,420),(650,420),(670,290)])
polygon(screen,(153,0,0),[(670,290),(700,210),(670,420)]) #1
polygon(screen,(153,0,0),[(700,420),(700,210),(670,420)])
rect(screen, (153,0,0), (386,305,120,100))


rect(screen, (159, 100, 159), (0,420,700,280))
def brline1(x1,y1,x2,y2,x3,y3,l):
    polygon(screen,(92,28,92),[(x1,y1),(x2,y2),(x1,l)]),
    polygon(screen,(92,28,92),[(x3,y3),(x2,y2),(x3,l)]),
    polygon(screen,(92,28,92),[(x1,l),(x2,y2),(x3,l)])
brline1(0,320,100,350,250,575,625)
brline1(250,575,375,600,490,540,625)
brline1(490,540,555,560,650,420,625)
circle(screen,(159, 100, 159),(322,545),76)
polygon(screen,(92,28,92),[(555,560),(535,555),(580,515)])
circle(screen,(159, 100, 159),(540,515),40)
circle(screen,(92,28,92),(676,425),25)
rect(screen,(92,28,92),(651,425,50,200))
polygon(screen,(92,28,92),[(676,400),(700,398),(700,425)])
def rotate(self,angle):
    self = pygame.transform.rotate(self, angle)
def bird(x,y): #я честно пытался создать поверхность, нарисовать эллипс и повернуть
    height=20,
    width=10,
    wing=pygame.Surface(width, height),
    pygame.draw(ellipse(screen,(0,0,0),(x-5,y-10,10,20))), #но это не сработало
    wing=rotate(wing,45) #оно отказывается принимать мою плоскость за плоскость
def smth(x,y,l,w): #поэтому я сделал через линии, поскольку работать с предыдущей конструкцией совсем не выходит
    line(screen,(0,0,0),(x,y),(x-(l+15),y-l),w),
    line(screen,(0,0,0),(x,y),(x+(l+15),y-l),w)
smth(300,220,10,10)
smth(370,228,10,10)
smth(370,265,10,10)
smth(270,295,10,10)
smth(450,430,10,10)
smth(480,470,7,7)
smth(540,510,20,15)
smth(570,460,7,7)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
