import random

## 변수 선언부 ##
d1, d2, d3, d4, d5, d6 = [0]*6
throwCount = 0

## 메인 코드부 #3
if __name__ == "__main__":
    while True:
        throwCount += 1

        d1 = random.randrange(1,7)
        d2 = random.randrange(1,7)
        d3 = random.randrange(1,7)
        d4 = random.randrange(1,7)
        d5 = random.randrange(1,7)
        d6 = random.randrange(1,7)
    
        if d1 == d2 == d3 == d4 == d5 == d6:
            print('6개 주사위 모두 동일한 숫자 -->', d1, d2, d3, d4, d5, d6)
            break

print(throwCount)