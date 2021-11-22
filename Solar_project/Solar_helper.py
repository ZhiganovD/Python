import numpy as np

a_sc = 700 #длина экрана
b_sc = 700 #ширина экрана
G = 0.005 #gravity constant

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

def V (x1, y1, x2, y2, m):
    l = np.sqrt( (x2 - x1) ** 2 + (y2 - y1) ** 2)
    a = G * m / (l ** 2)
    V = np.sqrt (a * l)
    return V


star_num = 1
#Sun parameteres
sun_x = a_sc / 2
sun_y = b_sc / 2
sun_Vx = 0 
sun_Vy = 0
sun_r = 20
sun_m = 333000 
sun_c = YELLOW
sun_type = 0 #type 'star'

planet_num = 5
#Mercury parameteres
mercury = [a_sc / 2 + 40, #x
b_sc / 2 , #y
0, #Vx
V(sun_x, sun_y, a_sc / 2 + 40, b_sc / 2, sun_m), #Vy
2, #r of planet
0.055, #mass
MAGENTA, #color
1 #type 'planet'
]
#Venus parameteres
venus = [a_sc / 2 + 70,
b_sc / 2,
0,
V(sun_x, sun_y, a_sc / 2 + 70, b_sc / 2, sun_m),
4,
0.815,
RED,
1
]
#Earth parameteres
earth = [ a_sc / 2 + 100, 
b_sc / 2,
0,
V(sun_x, sun_y, a_sc / 2 + 100, b_sc / 2, sun_m),
5,
1,
GREEN,
1
]
#MARS parameteres
mars = [a_sc / 2 + 150, 
b_sc / 2,
0,
V(sun_x, sun_y, a_sc / 2 + 150, b_sc / 2, sun_m),
5,
0.107,
RED,
1
]
#Jupiter parameteres
jupiter = [a_sc / 2 + 320,
b_sc / 2,
0,
V(sun_x, sun_y, a_sc / 2 + 320, b_sc / 2, sun_m),
10,
318,
MAGENTA,
1
]
par = [mercury, venus, earth, mars, jupiter]
