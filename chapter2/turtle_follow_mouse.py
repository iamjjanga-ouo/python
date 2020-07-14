import turtle
import random

## 변수 선언부 ##
pSize = 10
tSize = 1
r,g,b = 0.0, 0.0, 0.0

## 함수 선언부 ##
def screenLeftClick(x,y):
    global r,g,b            ## 마우스 왼클릭시 랜덤 선 만듦
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r,g,b))
    turtle.pendown()
    turtle.goto(x,y)

def screenRightClick(x,y):
    turtle.penup()
    turtle.goto(x,y)

def screenMidClick(x,y):
    global r,g,b,tSize
    tSize = (tSize + 1) % 10 ## 휠클릭마다 크기 1씩증가
    turtle.shapesize(tSize)
    

## 메인 코드부 ##
turtle.Turtle()
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()