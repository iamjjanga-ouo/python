'''
변수?
'''

a = [1,2,3]
id(a)           # 2307957473672 <- id 함수는 객체의 주소 값


# 리스트 복사하고자 할때
b = a
id(a)           # 2307957473672
id(b)           # 2307957473672

a is b          # True

a[1] = 4
a               # [1, 4, 3]
b               # [1, 4, 3]

# b변수 생성 시 a변수의 값을 가져오면서 a와는 다른 주소를 가리키도록 하는 법?

## 1.[:] 이용
a = [1,2,3]
b = a[:]
a[1] = 4
a               # [1,4,3]
b               # [1,2,3]

## copy 모듈 이용
from copy import copy
b = copy(a)         # b = copy(a)는 b = a[:]와 동일

b is a          # False

# 변수를 만드는 여러가지 방법
## 튜플로 만들기
a,b = ('python', 'life')
(a,b) = 'python', 'life'

## 리스트로 만들기
[a,b] = ['python', 'life']

## 여러개 변수
a = b = 'python'

## 두 변수의 값을 아주 간단히 변경
a = 3
b = 5
a,b = b,a
a           # 5
b           # 3