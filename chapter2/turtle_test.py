import turtle

## 함수 선언부 ##

## 변수 선언부 ##
myT = None

## 메인 코드부 ##
myT = turtle.Turtle()
myT.shape('turtle')

for i in range(0,4):
    T = myT.pos()                       ## turtle.pos()는 vector2D를 return하는데 이는 tuple을 의미
    print("%.2f . %.2f" % (T[0],T[1]))  ## 이동시 X,Y를 출력
    myT.forward(200)
    myT.right(90)

turtle.done()