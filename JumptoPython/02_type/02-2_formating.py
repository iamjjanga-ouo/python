'''
format 함수를 사용한 포매팅
'''

# 숫자 바로 대입
print("I eat {0} apples".format(3))

# 문자열 바로 대입
print("I eat {0} apples".format("five"))

# 숫자 값을 가진 변수로 대입
number = 3
print("I eat {0} apples".format(number))

# 왼쪽 정렬
print("{0:<10}".format("Hi"))

# 오른쪽 정렬
print("{0:>10}".format("Hi"))

# 가운데 정렬
print("{0:^10}".format("Hi"))

# 공백 채우기
print("{0:=^10}".format("Hi"))
print("{0:!<10}".format("Hi"))

# { 또는 } 문자 표현하기
print("{{ and }}".format())

