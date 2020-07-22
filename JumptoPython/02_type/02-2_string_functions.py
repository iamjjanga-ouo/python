'''
문자열 관련 함수들
'''

## 문자 개수 세기(count)
a = "hobby"
print(a.count("b"))

## 위치 알려주기1(find)
a = "Python is the best choice"
print(a.find('b'))      # 14
print(a.find('k'))      # -1(존재 X)

## 위치 알려주기2(index)
a = "Life is too short"
print(a.index('t'))     # 8
# print(a.index('k'))     # error

## 문자열 삽입(join)
print(",".join("abcd"))     # 'a,b,c,d'

## 소문자->대문자(upper)
a = "hi"
print(a.upper())

## 소문자<-대문자(lower)
a = "HI"
print(a.lower())

## 왼쪽 공백 지우기(lstrip)
a = " hi "
print(a.lstrip())

## 오른쪽 공백 지우기(rstrip)
a = " hi "
print(a.rstrip())

## 양쪽 공백 지우기(strip)
a = " hi "
print(a.strip())

## 문자열 바꾸기(replace)
a = "Life is too short"
a.replace("Life","Your leg")        # 'Your leg is too short'

## 문자열 나누기(split)
a = "Life is too short"
a.split()                           # ['Life', 'is', 'too', 'short']

b = "a:b:c:d"
b.split(":")                        # ['a', 'b', 'c', 'd']

