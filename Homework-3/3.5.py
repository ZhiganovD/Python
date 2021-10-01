from random import randint
import turtle

turtle.tracer(False)
k=340
turtle.penup()
turtle.goto(k,k)
turtle.pendown()
turtle.goto(-k,k)
turtle.goto(-k,-k)
turtle.goto(k,-k)
turtle.goto(k,k)
turtle.tracer(True)

number_of_turtles = 100
steps_of_time_number = 100000
turtle.tracer(50)


pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(10)
    unit.shape('circle')
    unit.goto(randint(-200, 200), randint(-200, 200))
    unit.left(randint(0,360))


for i in range(steps_of_time_number):
    for unit in pool:
        r=2
        x=unit.xcor()
        y=unit.ycor()
        if(x<k-r and x>r-k and y<k-r and y>r-k):
            unit.forward(r)
        else:
            if(y>=k-r):
                if(unit.heading()<=90):
                    unit.right(2*unit.heading())
                    unit.forward(r)
                if(unit.heading()>90 and unit.heading()<180):
                    unit.left(2*(180-unit.heading()))
                    unit.forward(r)
            if(y<=-k+r):
                if(unit.heading()>=270):
                    unit.left(2*(360-unit.heading()))
                    unit.forward(r)
                if(unit.heading()<270 and unit.heading()>180):
                    unit.right(2*(unit.heading()-180))
                    unit.forward(r)
            if(x>=k-r):
                if(unit.heading()>270):
                    unit.right(2*(unit.heading()-270))
                    unit.forward(r)
                if(unit.heading()<90 and unit.heading()>=0):
                    unit.left(2*(90-unit.heading()))
                    unit.forward(r)
            if(x<=r-k):
                if(unit.heading()>=180 and unit.heading()<270):
                 unit.left(2*(-unit.heading()+270))
                 unit.forward(r)
                if(unit.heading()>90 and unit.heading()<180):
                  unit.right(2*(-90+unit.heading()))
                  unit.forward(r)
            if(k-r<x<k+r and k-r<y<k+r):
                unit.left(225)
                unit.forward(2*r)
            if(-k+r>x>-k-r and k-r<y<k+r):
                unit.left(315)
                unit.forward(2*r)
            if(-k-r<x<-k+r and -k-r<y<-k+r):
                unit.left(45)
                unit.forward(2*r)
            if(-r+k<x<r+k and -r-k<y<r-k):
                unit.left(135)
                unit.forward(2*r)
