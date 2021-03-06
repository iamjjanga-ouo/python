'''
f 문자열 포매팅
'''

name = '홍길동'
age = 30
print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')

## 표현식도 지원
print(f'나는 내년이면 {age+1}살이 된다.')       # >>> 31살로 출력됨

## 딕셔너리 가능
d = {'name':'홍길동', 'age':30}
print(f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.')

## 정렬 가능
print(f'{"hi":<10}')    # 왼쪽 정렬
print(f'{"hi":>10}')    # 오른쪽 정렬
print(f'{"hi":^10}')    # 가운데 정렬

print(f'{"hi":=^10}')   # 가운데 정렬하고 '=' 문자로 공백 채우기
print(f'{"hi":!<10}')   # 왼쪽 정렬하고 '!' 문자로 공백 채우기

## 소수점 표현
y = 3.42134234
print(f'{y:0.4f}')
print(f'{y:10.f}')


