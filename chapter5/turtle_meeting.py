import turtle
import math
import random

## 전역 변수부 ##
t1, t2, t3 = [None] * 3
t1_X, t1_Y, t2_X, t2_Y, t3_X, t3_Y = [0] * 6
swidth, sheight = 300, 300

## 메인 함수부 #3
if __name__ == "__main__":
    turtle.title('거북이 만나기')
    turtle.setup(width=swidth+50, height=sheight+50)
    turtle.screensize(swidth,sheight)

    t1 = turtle.Turtle('turtle'); t1.color('red'); t1.penup()
    t2 = turtle.Turtle('turtle'); t2.color('blue'); t2.penup()
    t3 = turtle.Turtle('turtle'); t3.color('green'); t3.penup()

    t1.goto(-100,-100); t2.goto(0,0); t3.goto(100,100)

    while True:
        angle = random.randrange(0,360)
        dist = random.randrange(1,50)
        t1.left(angle); t1.forward(dist)

        angle = random.randrange(0,360)
        dist = random.randrange(1,50)
        t2.left(angle); t2.forward(dist)

        angle = random.randrange(0,360)
        dist = random.randrange(1,50)
        t3.left(angle); t3.forward(dist)

        t1_X = t1.xcor(); t1_Y = t1.ycor()
        t2_X = t2.xcor(); t2_Y = t2.ycor()
        t3_X = t3.xcor(); t3_Y = t3.ycor()

        if(t1_X > 150 or t1_Y > 150):
            t1.goto(0,0)
            t1_X, t1_Y = 0,0
        elif(t2_X > 150 or t2_Y > 150):
            t2.goto(0,0)
            t2_X, t2_Y = 0,0
        elif(t3_X > 150 or t3_Y > 150):
            t3.goto(0,0)
            t3_X, t3_Y = 0,0
        
        if (math.sqrt(pow(t1_X - t2_X, 2) + pow(t1_Y - t2_Y,2)) <= 20 or \
           math.sqrt(pow(t1_X - t3_X,2) + pow(t1_X - t3_Y,2)) <= 20 or \
           math.sqrt(pow(t2_X - t3_X,2) + pow(t2_Y - t3_Y,2)) <= 20):
                t1.turtlesize(3); t2.turtlesize(3); t3.turtlesize(3)
                break
        
turtle.done()