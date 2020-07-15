## 변수 선언부 ##
select, answer, numStr, num1, num2 = 0,0,"",0,0

## 메인 코드부 ##
select = int(input("1. 입력한 수식 계산 2. 두 수 사이의 합계 : "))

if select == 1:
    numStr = input("*** 수식을 입력하세요. : ")
    answer = eval(numStr)
    print("%s 결과는 %5.1f입니다." %(numStr, answer))
elif select == 2:
    num1 = int(input("*** 첫번째 숫자 입력 : "))
    num2 = int(input("*** 두번째 숫자 입력 : "))
    for i in range(num1,num2+1):                ## range 함수의 stop은 exclusive이므로 +1을 해줘야한다.
        answer = answer + i
    print("%d와 %d 사이의 합계는 %d입니다." % (num1,num2, answer))
else:
    print("1 or 2만 입력...")