'''
사용자로부터 이름, 키, 체중 값을 입력받아 비만도를 구하고 출력하는 코드를 작성하시오.
비만도 계산 식 : 비만도(%) = 현재 체중 / 표준 체중 * 100
표준 체중 계산 식 : 표준 체중 = (현재 키 - 100) * 0.9
출력 예제 : 홍길동님의 비만도는 112.15% 입니다.
'''

## 변수 선언부 ##
name, height, weight = '',0,0
f_weight, obesity = 0.0, 0.0

# 메인 함수부 ##
name = input("이름을 입력하시오 : ")
height = int(input("키를 입력하시오 : "))
weight = int(input("체중을 입력하시오 : "))

f_weight = (height - 100) * 0.9
obesity = (weight/f_weight) * 100
print("{:.2f}%".format(obesity))