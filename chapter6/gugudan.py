## 전역 선언부 ##
i, j, guguLine = 0,0,""

## 메인 함수부 ##
for i in range(2,10,1):
    guguLine = guguLine + "# %d단 #" % i

print(guguLine)

for i in range(1,10,1):
    guguLine = ""
    for j in range(2,10,1):
        guguLine = guguLine + str("%2dX %2d = %2d" % (j,i, j*i))
    print(guguLine)
