'''
600kg 제한의 화물용 엘리베이터가 있다. 2개의 물건에 대한 무게를 실수로 입력 받아
현재 엘리베이터에 적재할 수 있는 무게를 구하고 출력하시오.
    입력 양식
        첫 번째 물건의 무게 : 200.5
        두 번째 물건의 무게 : 78.56

    출력 양식
        화물 엘리베이터의 허용 무게 320.94kg 남았습니다.
'''
## global ##
item1_w, item2_w = 0,0
limit_w = 600

## main
if __name__ == "__main__":
    item1_w = float(input("첫 번째 물건의 무게 : "))
    item2_w = float(input("두 번째 물건의 무게 : "))

    if item1_w + item2_w <= limit_w:
            print(f'화물 엘리베이터의 허용 무게 {limit_w - (item1_w + item2_w)}kg 남았습니다.')
    else:
        print('허용 무게를 초과하였습니다.')





'''
현재 원달러 환율이 1,121.3원 일 때 n원을 달러로 환전하는 경우 몇 달러가 되는지 구하는 코드를 작성하시오.
'''

## global ##
kor_currency = 1121.3

## main ##
won = int(input("환전할 원을 입력하세요. : "))
print("dollar($) : %.2f달러" % (won / 1121.3))