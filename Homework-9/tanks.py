import math
from random import randint
import numpy as np
from random import choice

import pygame
from pygame.constants import K_LEFT, K_RIGHT, K_a, K_d

pygame.font.init() #для надписей
myfont = pygame.font.SysFont('Comic Sans MS', 30) #шрифты для надписи


FPS = 30

RED = 0xFF0000
RED2 = pygame.Color(255, 0, 0, 255)
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
BLACK2 = pygame.Color(0, 0, 0, 255)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D

GAME_COLORS = [RED, BLUE, YELLOW, MAGENTA]

WIDTH = 800
HEIGHT = 600

def options(x0, y0, alpha, surface, screen_0):
    #Поворачивает surface на alpha, переводит размеры в w*h, отражает
    #относительно игрек, если стоит флаг, ставит в (x0, y0)
    #(левый верхний угол, везде и далее левый верхний угол, если не оговорено
    #обратное) screen_0 и его возвращает
    #(Вставляет в screen_0 surface)
    
    surface = pygame.transform.rotate(surface, alpha) #Поворот на угол alpha
    screen_0.blit(surface, (x0, y0)) #Размещает surface на screen_0 в (x0, y0)
    return screen_0 #Возвращает картинку screen_0, на которой теперь уже наложен surface

class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 100

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        g = 5
        k = 0.7
        l = 0.9
        if self.live == 0:
          self.r = 0
        if self.y >= 530:
            self.vy = (-1) * k * self.vy
            self.vx = l * self.vx     
        if self.x >= 800:
            self.vx = (-1) * self.vx

        self.x += self.vx
       
        if self.y < 530:
            self.y -= self.vy - 0.5 * g
            self.vy -= g
        self.live -= 1

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (np.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) <= self.r + obj.r):
            return True
        else:
            return False
    
    def hittest_c(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (np.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) <= self.r + obj.a):
            return True
        else:
            return False

class Bomb:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = WHITE
        self.live = 100

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        g = 5
        k = 0.7
        l = 0.9
        if self.live == 0:
          self.r = 0
        if self.live > 0 and self.live < 25:
            self.r = 25
        if self.y >= 530:
            self.vy = (-1) * k * self.vy
            self.vx = l * self.vx     
        if self.x >= 800:
            self.vx = (-1) * self.vx

        self.x += self.vx
       
        if self.y < 530:
            self.y -= self.vy - 0.5 * g
            self.vy -= g
        self.live -= 1

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (np.sqrt((self.x - (obj.x + obj.r)) ** 2 + (self.y - (obj.y + obj.r)) ** 2) <= self.r + obj.r):
            return True
        else:
            return False

    def hittest_c(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (np.sqrt((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) <= self.r + obj.a):
            return True
        else:
            return False


class Gun:
    def __init__(self, screen, number):
        self.screen = screen
        self.f2_power = 70
        self.f2_on = 0
        self.x = randint(40, 500)
        self.y = 530
        self.w = 100
        self.h = 30
        self.r = 30
        self.an = 1
        self.vx = 5
        self.color = BLACK2
        self.an2 = 0
        self.number = number

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end_balls(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        new_ball.x = self.x + 50
        new_ball.y = self.y - 10
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 70
    
    def fire2_end_bombs(self, event):
        """Выстрел бомбой (не тот, что из ДМБ).

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_bomb = Bomb(self.screen)
        new_bomb.r += 5
        self.an = math.atan2((event.pos[1]-new_bomb.y), (event.pos[0]-new_bomb.x))
        new_bomb.vx = self.f2_power * math.cos(self.an)
        new_bomb.vy = - self.f2_power * math.sin(self.an)
        new_bomb.x = self.x + 50
        new_bomb.y = self.y - 10
        balls.append(new_bomb)
        self.f2_on = 0
        self.f2_power = 70

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event and event.pos[0] - 20 != 0:
            self.an = -math.atan((event.pos[1]-450) / (event.pos[0]-20))
            if self.an < np.pi * 0.5 and self.an >= 0:
             self.an2 = (self.an * 180 / np.pi) 
        if self.f2_on:
            self.color = RED2
        else:
            self.color = BLACK2

    def draw(self):
        surface = pygame.Surface([100, 100], pygame.SRCALPHA)
        #surface.fill(WHITE)
        pygame.draw.rect(
            surface,
            self.color,
            (50, 0, self.f2_power, 10)
        )
        surface = options(self.x + 10, self.y - 30, self.an2, surface, self.screen)
        pygame.draw.rect(
            self.screen,
            BLACK,
            (self.x, self.y, self.w, self.h)
        )
        pygame.draw.circle(
            self.screen,
            BLACK,
            (self.x + 50, self.y),
            self.r
        )

    def move(self, event):
        if self.x > 10 and self.x < 790:
            if event.type == pygame.KEYDOWN:
                if event.key == K_LEFT or event.key == K_a:
                    self.x -= self.vx
                    #self.draw()
                elif event.key == K_RIGHT or event.key == K_d:
                    self.x += self.vx
                    #self.draw()
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED2
        else:
            self.color = BLACK2#GREY


class Target:
    def __init__(self, screen):
        self.screen = screen
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        global UFO_1x, UFO_2x, UFO_y, cords
        self.live = 1
        self.points = 0
        self.vy = randint(1, 4)
        self.x = choice(cords)
        self.y = UFO_y + 42.5
        self.r = randint(20, 35)
        self.color = RED
        #self.draw()

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
     pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
      )
    def move(self):
        if ( self.y > 635):
            self.r = 0
            self.new_target()
        self.y += self.vy

class Cargo:
    def __init__(self, screen):
        self.screen = screen
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        global UFO_1x, UFO_2x, UFO_y, cords
        self.live = 1
        self.points = 0
        self.vy = randint(1, 4)
        self.x = choice(cords)
        self.y = UFO_y + 42.5
        self.a = randint(20, 25)
        self.color = BLACK
        #self.draw()

    def hit(self, points=5):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
     pygame.draw.rect(
            self.screen,
            self.color,
            (self.x - self.a, self.y, self.a, self.a),
      )
    def move(self):
        if ( self.y > 635):
            self.r = 0
            self.new_target()
        k = 1.01
        self.y += self.vy
        self.vy = k * self.vy


def UFO (x, y):
    pygame.draw.ellipse(
        screen,
        BLUE,
        (x, y, 200, 50)
    )
    pygame.draw.ellipse(
        screen,
        BLACK,
        (x + 60, y + 35, 80, 15)
    )


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []
tanks = []
enemies = []
cargoes = []
enemy = 4
cargo = 3
tank = 2
points = 0
UFO_1x = 200
UFO_2x = 500
UFO_y = -25
cords = [UFO_1x + 100, UFO_2x + 100]

clock = pygame.time.Clock()

for i in range(0, enemy):
 new_enemy = Target(screen)
 enemies.append(new_enemy)

for i in range(0, cargo):
 new_cargo = Cargo(screen)
 cargoes.append(new_cargo)

for i in range(0, tank):
 new_tank = Gun(screen, i)
 tanks.append(new_tank)
finished = False

while not finished:
    screen.fill(CYAN)
    pygame.draw.rect(
        screen,
        GREEN,
       (0, 530, 800, 70)
    )
    UFO (200, -25)
    UFO (500, -25)
    #gun.draw()
    for b in balls:
        b.draw()
    for a in enemies:
        a.draw()
    for c in tanks:
        c.draw()
    for d in cargoes:
        d.draw()
    
    textsurface = myfont.render('Points:', False, (0, 0, 0))  #надпись в углу экрана
    level = str(points) #перевод данных об очках в строку для вывода на экран
    textsurface1 = myfont.render(level, False, (0, 0, 0))
    screen.blit(textsurface,(0,0)) 
    screen.blit(textsurface1,(100,0)) #собственно, вывод надписи
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x = randint(0, 1)
            for c in tanks:
                if event.button == 1 and c.number:
                    c.fire2_start(event)
                elif event.button == 3 and (c.number == 0):
                    c.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            for c in tanks:
              if x and event.button == 1 and (c.number == 1):
                   c.fire2_end_balls(event)
              elif x == 0 and event.button == 1 and (c.number == 1):
                   c.fire2_end_bombs(event)
              elif x and event.button == 3 and (c.number == 0):
                   c.fire2_end_balls(event)
              elif x == 0 and event.button == 3 and (c.number == 0):
                   c.fire2_end_bombs(event)
        elif event.type == pygame.MOUSEMOTION:
            for c in tanks:
               c.targetting(event)
        if event.type == pygame.KEYDOWN:
            for c in tanks:
                if (event.key == K_LEFT or event.key == K_RIGHT) and c.number:
                 c.move(event)
                elif (event.key == K_a or event.key == K_d) and (c.number == 0):
                 c.move(event)

    for b in balls:
        b.move()
        for a in enemies:
           if b.hittest(a) and a.live and b.live > 0:
               a.live = 0
               a.hit()
               points += a.points
               a.new_target()
        for d in cargoes:
           if b.hittest_c(d) and d.live and b.live > 0:
               d.live = 0
               d.hit()
               points += d.points
               d.new_target()
    
    for a in enemies:
        a.move()
    
    for d in cargoes:
        d.move()

    for c in tanks:
        c.power_up()

pygame.quit()
