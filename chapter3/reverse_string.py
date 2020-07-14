'''
입력받은 문자열 거꾸로 출력하기
'''

## 변수 선언부 ##
str = None

## 메인 함수부 ##
if __name__ == "__main__":
    str = input("문자열 입력 :")
    
    for i in range(len(str)-1, -1, -1):
        print('%c' % str[i], end='')
