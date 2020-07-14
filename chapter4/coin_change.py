## 변수 선언부 ##
money, c500, c100, c50, c10 = 0,0,0,0,0

## 메인 코드부 ##
money = int(input("교환할 돈 얼마? "))

c500 = money // 500
money %= 500
print("500won : %d개" % c500)

c100 = money // 100
money %= 100
print("100won : %d개" % c100)

c50 = money // 50
money %= 50
print("50won : %d개" % c50)

c10 = money // 10
money %= 10
print("10won : %d개" % c10)

print("remains : %dwon" % money)