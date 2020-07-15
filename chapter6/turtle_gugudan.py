import turtle

## global ##
i, j, tX, tY = [0] * 4
swidth, sheight = 800, 450

## main ##
if __name__ == "__main__":
    turtle.title('거북이 구구단')
    turtle.shape('turtle')
    turtle.setup(width=swidth+50, height=sheight+50)
    turtle.screensize(swidth,sheight)
    turtle.penup()
    turtle.speed(3)
    tX, tY = -500, 250
    turtle.goto(tX,tY)

    for i in range(1,10):
        for j in range(2,10):
            turtle.goto(tX + 80*j, tY - 40*i)
            gugu = str(j) + ' x ' + str(i) + ' = ' + str(j*i)
            turtle.write(gugu, font=('Arial',12, 'bold'))

turtle.done()