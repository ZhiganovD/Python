import pygame
import sys
from pygame.draw import *
from random import randint
pygame.init()
pygame.font.init() #для надписей
myfont = pygame.font.SysFont('Comic Sans MS', 30) #шрифты для надписи

FPS = 30 #FPS
a_sc = 700 #длина экрана
b_sc = 700 #ширина экрана
screen = pygame.display.set_mode((a_sc, b_sc)) #создание экрана

balls = [[]] #параметры balls
k = 0 #количество balls за все время
k_n = 0 #их количество сейчас
sn_x = 0 #количество снитчей по горизонтали
sn_y = 0 #количество снитчей по вертикали
sn = [[]] * 2 #множество данных снитчей с 2мя элементами в виде списков
sn[0] = [0]
sn[1] = [0] 
point = 0 # количество очков
level = str(point)
sign_x = 1 #знак движения по x
sign_y = 1 #знак движения по y

top = 5 #сколько игроков в топе
win = [] #массив строк с именами рекордсменов
pts = [] #массив строк их рекордов
rec = [] #массив их рекордов численно

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN] #перечень цветов
screen.fill(WHITE) #заполнить экран белым

def new_ball(): #рисует шарик
    global x, y, r, color, p
    x = randint(50, a_sc - 50) #он рандомен по х
    y = randint(50, b_sc - 50) #и по у
    r = randint(10, 30) #и даже по r
    p = 75 - r #очки за него, чем меньше шарик, тем больше очков
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def snitch(): #а вот и козырь
    global x, y, w, h, color, p
    x = randint(50, a_sc - 50) #он рандомен по х
    y = randint(50, b_sc - 50) #и по у
    w = randint(10, 50) #и даже по w
    h = randint (10, 50) #и по h
    p = 500 #очки за него
    color = BLACK
    rect(screen, color, (x, y, w, h))

def dr_ball(x, y, r, color): #рисует шарик (вместо обычного circle)
    circle(screen, color, (x,y), r)

def dr_snitch(x, y, w, h, color): #рисует снитч (вместо обычного rect)
    rect(screen, color, (x, y, w, h))

def delete_sn_x(): #удаление горизонтального снитча
    sn[0][0] = 0
    sn[0][1] = 0
    sn[0][2] = 0
    sn[0][3] = 0

def delete_sn_y(): #удаления вертикального снитча
    sn[1][0] = 0
    sn[1][1] = 0
    sn[1][2] = 0
    sn[1][3] = 0

def delete(l): #удаление круга обнулением координат и радиуса
    balls[l][0] = 0
    balls[l][1] = 0
    balls[l][2] = 0

def reading(win, pts, rec): #чтение файла с рекордсменами
    g = open( 'winners.txt', 'r')
    line = g.readlines()
    for i in range(0, top):
        name, score = line[i].split(' ', 2)
        win.append(name)
        pts.append(score)
        rec.append(int(score))
    g.close() #закрыть файл
    return win, pts, rec

pygame.display.update()
clock = pygame.time.Clock()
finished = False
finished0 = False
finished1 = False

while not finished0:
    clock.tick(FPS)
    rect(screen, WHITE, (0, 0, a_sc, b_sc)) #заливаем экран белым
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
    for click in pygame.event.get():
        if click.type == pygame.MOUSEBUTTONDOWN: #нажата кнопка мыши
         if click.button == 1 and click.pos[0] < (x1 + l1) and click.pos[0] > (x1) and click.pos[1] < (y1 + h) and click.pos[1] > (y1 - h): 
             finished0 = True
         if click.button == 1 and click.pos[0] < (x2 + l2) and click.pos[0] > (x2) and click.pos[1] < (y2 + h) and click.pos[1] > (y2 - h):
             reading(win, pts, rec)
             while not finished1:
                 clock.tick(FPS)
                 rect(screen, WHITE, (0, 0, a_sc, b_sc)) #заливаем экран белым
                 textsurface_1 = myfont.render('Top 5', False, (0, 0, 0))  #надпись в центре экрана
                 screen.blit(textsurface_1,(330, y1 - 200))
                 textsurface_2 = myfont.render( win[0] + ' ' + pts[0], False, (0, 0, 0))  #надпись в центре экрана
                 screen.blit(textsurface_2,(300 - 20, y1 - 100))
                 textsurface_3 = myfont.render( win[1] + ' ' + pts[1], False, (0, 0, 0))  #надпись в центре экрана
                 screen.blit(textsurface_3,(300 - 20, y1 - 20))
                 textsurface_4 = myfont.render( win[2] + ' ' + pts[2], False, (0, 0, 0))  #надпись в центре экрана
                 screen.blit(textsurface_4,(300 - 20, y1 + 60))
                 textsurface_5 = myfont.render( win[3] + ' ' + pts[3], False, (0, 0, 0))  #надпись в центре экрана
                 screen.blit(textsurface_5,(300 - 20, y1 + 140))
                 textsurface_6 = myfont.render( win[4] + ' ' + pts[4], False, (0, 0, 0))  #надпись в центре экрана
                 screen.blit(textsurface_6,(300 - 20, y1 + 220))
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

while not finished:
    clock.tick(FPS)
    if point > 10000:
       break
    for click in pygame.event.get():
        if click.type == pygame.QUIT:
            finished = True
        if click.type == pygame.MOUSEBUTTONDOWN: #нажата кнопка мыши
            if click.button == 1: #если нажал ЛКМ
                d = 0 #количество удалений
                for i in range(k - 1, 0, -1): #проверка на расстояние от центра круга до точки нажатия и сравнение с радиусом (начинаем с последнего)
                    if( (balls[i][0] - click.pos[0]) ** 2 + (balls[i][1] - click.pos[1]) ** 2 < (balls[i][2])**2 and d ==0): #удаляем за раз только одного
                        delete(i)
                        k_n = k_n - 1 #общее количество balls уменьшилось
                        point += balls[i][4] #прибавление очков
                        d += 1 #счетчик удалений
                if (d ==0):
                        point -= 10 #карательная система, минус за промахи
                if( click.pos[0] < (sn[0][0] + sn[0][2]) and click.pos[0] > (sn[0][0] - sn[0][2]) and click.pos[1] < (sn[0][1] + sn[0][3]) and click.pos[1] > (sn[0][1] - sn[0][3])):
                    #нажатие в границах квадрата
                    delete_sn_x()
                    sn_x -= 1 #уменьшается количество снитчей по x
                    point += sn[0][4] #прибавление очков
                if( click.pos[0] < (sn[1][0] + sn[1][2]) and click.pos[0] > (sn[1][0] - sn[1][2]) and click.pos[1] < (sn[1][1] + sn[1][3]) and click.pos[1] > (sn[1][1] - sn[1][3])):
                    #нажатие в границах квадрата
                    delete_sn_y()
                    sn_y -= 1 #уменьшается количество снитчей по y
                    point += sn[1][4] #прибавление очков
                pygame.display.update()
            if click.button == 3: #выключение при нажатии ПКМ
                    finished = True
    for i in range(randint(0,1)): #с вероятностью 0,5 появится шарик
        if(k_n < 50): #ограничим количество до 49
            new_ball() 
            balls.append([x, y, r, color, p, sign_x, sign_y]) #добавим параметры k-го шарика
            k = k + 1 #количество шариков в массиве
            k_n = k_n + 1 #количество шариков на экране 
    if (sn_x == 0): #так как горизонтальный снитч только один
        snitch()
        sn_x += 1
        sn[0] = [x, y, w, h, p, sign_x, color] #передадим параметры снитча
    if (sn_y == 0): #так как вертикальный снитч только один
        snitch()
        sn_y += 1
        sn[1] = [x, y, w, h, p, sign_y, color] #передадим параметры снитча
    rect(screen, WHITE, (0, 0, a_sc, b_sc)) #заливаем экран белым
    for j in range(1, k, 1):
        if(balls[j][1] - balls[j][2] < 20 ): #проверяем приближение ко всем 4м границам экрана сменой направления
            balls[j][6] = balls[j][6] * (-1)
        if(balls[j][1] + balls[j][2] > b_sc - 20 ):
            balls[j][6] = balls[j][6] * (-1)
        if(balls[j][0] + balls[j][2] > a_sc - 20 ):
            balls[j][5] = balls[j][5] * (-1)
        if(balls[j][0] - balls[j][2] < 20 ):
            balls[j][5] = balls[j][5] * (-1)
        balls[j][0] -= balls[j][5] * 5 #изменение координат
        balls[j][1] -= balls[j][6] * 5
        dr_ball(balls[j][0], balls[j][1], balls[j][2], balls[j][3]) #рисуем шарик с новыми параметрами
    if (sn_x == 1): #если снитч вообще есть
        if(sn[0][0] > a_sc + 290):
            sn[0][5] = sn[0][5] * (-1)
        if(sn[0][0] < (-1) * a_sc - 290):
            sn[0][5] = sn[0][5] * (-1)
        sn[0][0] -= sn[0][5]*25
        dr_snitch(sn[0][0], sn[0][1], sn[0][2], sn[0][3], sn[0][6]) #записываем его параметры
    if (sn_y == 1): #если снитч вообще есть
        if(sn[1][1] > b_sc + 290):
            sn[1][5] = sn[1][5] * (-1)
        if(sn[1][1] < (-1) * b_sc - 290):
            sn[1][5] = sn[1][5] * (-1)
        sn[1][1] -= sn[1][5]*18
        dr_snitch(sn[1][0], sn[1][1], sn[1][2], sn[1][3], sn[1][6]) #записываем его параметры
    textsurface = myfont.render('Points:', False, (0, 0, 0))  #надпись в углу экрана
    level = str(point) #перевод данных об очках в строку для вывода на экран
    textsurface1 = myfont.render(level, False, (0, 0, 0))
    screen.blit(textsurface,(0,0)) 
    screen.blit(textsurface1,(100,0)) #собственно, вывод надписи
    pygame.display.update()

while not finished:
    clock.tick(FPS)
    if point > 10000:
       rect(screen, WHITE, (0, 0, a_sc, b_sc)) #заливаем экран белым
       textsurface = myfont.render('You win!', False, (0, 0, 0))  #надпись в углу экрана
       screen.blit(textsurface,(280,350))
       textsurface1 = myfont.render('Your score:' + level, False, (0, 0, 0))  #надпись в углу экрана
       screen.blit(textsurface1,(240,380))
       pygame.display.update()
    for click in pygame.event.get():
        if click.type == pygame.MOUSEBUTTONDOWN: #нажата кнопка мыши
         if click.button == 3: #выключение при нажатии ПКМ
             finished = True
        if click.type == pygame.QUIT:
            finished = True
        
pygame.quit()

print('Write down your name') #а теперь запишем имя игрока
a = input()
level = level + '\n'
reading(win, pts, rec)
for i in range(0, top - 1): #добавление нового элемента и выстраивание списка по возрастанию
 if((point >= rec[i + 1]) and (point < rec[i])):
      for j in range(top - 1, i, -1):
          win[j] = win[j - 1]
          pts[j] = pts[j - 1]
      win[i+1] = a
      pts[i+1] = level
      break
 if(point >= rec[0]):
      for j in range(top - 1, 0, -1):
          win[j] = win[j - 1]
          pts[j] = pts[j - 1]
      win[0] = a
      pts[0] = level
      break
f = open('winners.txt', 'w') #открыть файл
for i in range(0, top): #sacred Jedi texts!
    f.write(win[i] + ' ' + pts[i])
#записать в файл данные игрока
f.close() #закрыть файл
