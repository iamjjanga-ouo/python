# 랜덤 함수
# from random import random
# from random import randint
# from random import randrange

'''
a = random()            0.0 ~ 1.0 미만
a = random() * 10       0.0 ~ 10.0 미만
a = int(random() * 10) 
a = randint(10,10)      10 ~ 20 미만
'''

# from random import random
# num = int(random() * 100)
# if num > 50:
#     print("50보다 크다.")
# if num <= 50:
#     print("50보다 작거나 같아요.")

# if num % 2 == 0:
#     print("num은 짝수 입니다.")
# elif num % 2 != 0:
#     print("num은 홀수 입니다.")

# forecast = int(input("오늘 비가올 확률은 몇%인가요? : "))
# if forecast >= 50:
#     print("우산을 준비하세요.")
# else:
#     print("친구를 만나세요.")

# weather = input("오늘 날씨어때요? : ")
# if weather in ('눈, 비'):
#     print("우산을 준비하세요.")
# elif weather in ('안개, 미세먼지'):
#     print("마스크를 준비하세요.")
# elif weather == '화창':
#     print("친구를 만나세요.")
# else:
#     print("stay home")

'''
계정 생성 프로그램

1. 사용자로 부터 계정을 생헝하기 위한 ID와 PW를 입력 받습니다.
2. PW의 경우 한번 더 사용자 입력을 받아서 이전에 입력한 PW와 일치하는 PW를 입력하였는지를 확인하여
   일치한 경우에만 "계정 생성 완료" 메시지를 출력하고, 그렇지 않은 경우에는 "계정 생성 실패" 메시지를
   출력하게 하세요.
'''
# import re

# ## global ##
# id, pw = '',[None,None]
# regex = re.compile(r'[%$#@!]{2}\d{5,10}')

# ## function ## 
# def matchtxt(text):
#     matchobj = regex.search(text)
#     if matchobj != None:
#         return 1
#     else:
#         return 0

# ## main ##
# print("## 계정 생성 ##")
# id = input("생성할 ID 입력 : ")
# while True:
#     pw[0] = input("비밀번호 입력(특수문자[!@#$]2자리 + 숫자 5~10자리) : ")
#     if matchtxt(pw[0]) == 0:
#         print("비밀번호 규칙을 따라주세요.")
#         continue

#     pw[1] = input("비밀번호 재입력 : ") 
#     if pw[0] == pw[1]:
#         print("계정 생성 완료")
#         break
#     else:
#         print("계정 생성 실패")

'''
사용자로부터 체중과 키를 입력받아서, 비만도를 구하세요.
비만도범위: 저체중 ( ~ 100 미만) / 정상(100~110미만) / 과체중(110-120미만) / 비만(120 ~ 130 미만), 고도비만(130 ~)
을 구분하여 출력 하세요.

표준체중 = (키-100)*0.9
비만도(%) = 현재 체중 / 표준 체중 * 100

'''
user_h = int(input("키를 입력하세요. : "))
user_w = int(input("체중을 입력하세요. : "))

std_w = (user_h - 100) * 0.9
print("표준체중은 : ", std_w)

obesity = user_w/std_w * 100

if obesity < 100:
    print("저체중입니다.")
elif obesity < 110:
    print("정상입니다.")
elif obesity < 120:
    print("과체중입니다.")
elif obesity < 130:
    print("비만입니다.")
else:
    print("고도비만입니다.")
