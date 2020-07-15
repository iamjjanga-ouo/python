import turtle

## 전역 변수부 ##
num = 0
swidth, sheight = 1000, 300
curX, curY = 0,0

## 메인 함수부 ##
if __name__ == "__main__":
    turtle.title('거북이 이진수 표현하기')
    turtle.shape('turtle')
    turtle.setup(width=swidth+50, height=sheight+50)
    turtle.screensize(swidth,sheight)
    turtle.penup()
    turtle.left(90)                             ## 거북이가 '북쪽'을 바라보게

    num=int(input("숫자를 입력하시오 : "))        # 5 입력시
    binary = bin(num)
    curX = swidth/2                             # 0.0에서 오른쪽 X=1500에서 시작하게
    curY = 0

    # print(binary)                             # 0b101
    # print("len(binary) : %d" % len(binary))   # len(binary) : 5

    for i in range(len(binary) - 2):            # 0 ~ 3
        turtle.goto(curX, curY)
        if num&1:                               # binary == 1
            turtle.color('red')
            turtle.turtlesize(2)
        else:                                   # binary == 0
            turtle.color('blue')
            turtle.turtlesize(1)
        turtle.stamp()
        curX -= 50                              # 거북이 찍을 X좌표 좌로 50이동
        num >>= 1                               # binary 숫자 우로 1bit shift

turtle.done()