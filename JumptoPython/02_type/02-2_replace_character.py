'''
문자열 "Pithon"이라는 문자열을 "Python"으로 바꾸려면?
'''

a = "Pithon"
a[1]        # 'i'

## 틀림
# a[1] = 'y'  # 문자열 자료형은 immutable하다.

## 맞음
a[:1]       # >>> 'P'
a[2:]       # >>> 'thon'

a[:1] + 'y' + a[2:] # >>> 'Python'



