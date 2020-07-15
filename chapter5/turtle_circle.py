import turtle

## 전역 변수 선언부 ##
swidth, sheight = 500, 500

## 메인 코드부 ##
if __name__ == "__main__":
    turtle.title('거북이 무지개색 원그리기')
    turtle.shape('turtle')
    turtle.setup(width=swidth+50, height=sheight+50)
    turtle.screensize(swidth,sheight)
    turtle.penup()
    turtle.goto(0,-sheight/2)
    turtle.pendown()
    turtle.speed(10)                # 10은 빠르게, 1은 느리게, 0은 보이지 않을정도로 빠름

    for radius in range(1, 250):
        if radius % 7 == 1:
            turtle.pencolor('red')
        elif radius % 7 == 2:
            turtle.pencolor('orange')
        elif radius % 7 == 3:
            turtle.pencolor('yellow')
        elif radius % 7 == 4:
            turtle.pencolor('green')
        elif radius % 7 == 5:
            turtle.pencolor('blue')
        elif radius % 7 == 6:
            turtle.pencolor('navyblue')
        else :
            turtle.pencolor('purple')

        turtle.circle(radius)       # radius 만큼의 반지름의 원을 그림

turtle.done()