import turtle
turtle.penup()
turtle.goto(-300,0)
turtle.pendown()
a=10
Vx=20
Vy=55
k=0.8
ty=0
turtle.speed(0)
for t in range(0,500):
    x=Vx*t/10
    y=Vy*ty/10-(a*ty**2)/200
    turtle.goto(x-300,y)
    if(y==0 or y<0):
        Vy=Vy*k
        ty=0
        y=Vy*ty/10-a*ty**2/200
    ty=ty+1

turtle.exitonclick()
