import turtle

## 함수 선언부 ##

## 변수 선언부 ##
myT = None

## 메인 코드부 ##
myT = turtle.Turtle()
myT.shape('turtle')

for i in range(0,4):
    myT.forward(200)
    myT.right(90)

turtle.done()