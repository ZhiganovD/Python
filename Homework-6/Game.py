import pygame
from pygame.draw import *
from random import randint
pygame.init()
pygame.font.init() #для надписей
myfont = pygame.font.SysFont('Comic Sans MS', 30) #шрифты для надписи

FPS = 10 #FPS
screen = pygame.display.set_mode((700, 700)) #создание экрана

balls = [[]] #параметры balls
k = 0 #количество balls за все время
k_n = 0 #их количество сейчас
sn_x = 0 #количество снитчей по горизонтали
sn_y = 0 #количество снитчей по вертикали
sn = [[]] * 2 #множество данных снитчей с 2мя элементами в виде списков
sn[0] = [0]
sn[1] = [0] 
point = 0 # количество очков
sign_x = 1 #знак движения по x
sign_y = 1 #знак движения по y

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
    x = randint(50, 650) #он рандомен по х
    y = randint(50, 650) #и по у
    r = randint(10, 50) #и даже по r
    p = 10 #очки за него
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)

def snitch(): #а вот и козырь
    global x, y, w, h, color, p
    x = randint(50, 650) #он рандомен по х
    y = randint(50, 650) #и по у
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


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
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
        if(k_n < 30): #ограничим количество до 29
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
    rect(screen, WHITE, (0, 0, 700, 700)) #заливаем экран белым
    for j in range(1, k, 1):
        if(balls[j][1] - balls[j][2] < 20 ): #проверяем приближение ко всем 4м границам экрана сменой направления
            balls[j][6] = balls[j][6] * (-1)
        if(balls[j][1] + balls[j][2] > 680 ):
            balls[j][6] = balls[j][6] * (-1)
        if(balls[j][0] + balls[j][2] > 680 ):
            balls[j][5] = balls[j][5] * (-1)
        if(balls[j][0] - balls[j][2] < 20 ):
            balls[j][5] = balls[j][5] * (-1)
        balls[j][0] -= balls[j][5] * 10 #изменение координат
        balls[j][1] -= balls[j][6] * 10
        dr_ball(balls[j][0], balls[j][1], balls[j][2], balls[j][3]) #рисуем шарик с новыми параметрами
    if (sn_x == 1): #если снитч вообще есть
        if(sn[0][0] > 990):
            sn[0][5] = sn[0][5] * (-1)
        if(sn[0][0] < -990):
            sn[0][5] = sn[0][5] * (-1)
        sn[0][0] -= sn[0][5]*50
        dr_snitch(sn[0][0], sn[0][1], sn[0][2], sn[0][3], sn[0][6]) #записываем его параметры
    if (sn_y == 1): #если снитч вообще есть
        if(sn[1][1] > 990):
            sn[1][5] = sn[1][5] * (-1)
        if(sn[1][1] < -990):
            sn[1][5] = sn[1][5] * (-1)
        sn[1][1] -= sn[1][5]*50
        dr_snitch(sn[1][0], sn[1][1], sn[1][2], sn[1][3], sn[1][6]) #записываем его параметры
    textsurface = myfont.render('Points:', False, (0, 0, 0))  #надпись в углу экрана
    level = str(point) #перевод данных об очках в строку для вывода на экран
    textsurface1 = myfont.render(level, False, (0, 0, 0))
    screen.blit(textsurface,(0,0)) 
    screen.blit(textsurface1,(100,0)) #собственно, вывод надписи
    pygame.display.update()
pygame.quit()

print('Write down your name') #а теперь запишем имя игрока
a = input()
f = open('winners.txt', 'a') #открыть файл
f.write(a + ' ' + level + '\n') #записать в файл данные игрока
f.close() #закрыть файл
