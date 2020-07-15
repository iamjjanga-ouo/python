# 함수 사용
# max, min
print(max(1,3,5,7,9))
print(min(1,3,5,7,9))
print(sum([1,3,5,7,9]))
print(pow(2,2)) # print(2**2) 
print(divmod(9,4)) # print(5/4) , print(5%4)
print(round(2.567))

print(bin(10))
print(bin(0o12))
print(bin(0xA))

## example
# 32 45 48 57 84 중 가장 큰 값과 작은 값
print("min : %d" % min(32,45,48,57,84))
print("max : %d" % max(32,45,48,57,84))

# 29 95 15 85 66 의 총 합
print("sum : %d" % sum([29,95,15,85,66]))

# 29 95 15 85 66 의 평균
print("avg : %.2f" % (sum([29,95,15,85,66]) / 5))

# 3,4,8,5 중 큰 값에서 작은 값의 거듭제곱
a = [3,4,8,5]
print("double : %d" % (max(a) ** min(a)))

# 16진수 값 305F의 10진수 값
print(int('305F',16))

# 10진수 1024의 16진수 값
print(hex(1024))

# 0x35의 2진수 값
print(bin(0x35))

# 0o35의 16진수 값
print(hex(0o35))

# 3452 + 5785 16진수 값
print(hex(3452+5785))

# 0xAC + 200의 2진수 값
print(bin(0xAC + 200))