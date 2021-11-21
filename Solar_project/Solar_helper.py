a_sc = 700 #длина экрана
b_sc = 700 #ширина экрана
G = 5 #gravity constant

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

star_num = 1
#Sun parameteres
sun_x = a_sc / 2
sun_y = b_sc / 2
sun_Vx = 0 
sun_Vy = 0
sun_r = 50
sun_m = 100 
sun_c = YELLOW

planet_num = 1
#Earth parameteres
e_x = a_sc / 2 + 10
e_y = b_sc / 2 + 150
e_Vx = 10
e_Vy = 10
e_r = 5
e_m = 10 
e_c = GREEN
