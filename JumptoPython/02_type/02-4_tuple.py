'''
튜플?
- 튜플은 몇 가지 점을 제외하고 리스트와 거의 비슷
    다른점:
        - 리스트는 [], 튜플은 ()
        - 리스트는 그 값의 생성, 삭제, 수정이 가능 / 튜플은 값 변경 X
'''

t1 = ()
t2 = (1,)                   # 단지 1개의 요소만을 가질 때에도 콤마(,)를 반드시 붙여야함
t3 = (1,2,3)
t4 = 1,2,3                  # 괄호()를 생략해도 무방
t5 = ('a','b',('ab','cd'))

'''
튜플의 요소값을 지우거나 변경하려고 하면 어떻게 될까?
'''

## 1. 튜플 요솟값을 삭제하려 할 때
t1 = (1,2,'a','b')
# del t1[0]                       # Typeerror : 'tuple' object doesn't support item deletion

## 2. 튜플 요소값을 변경하려 할 때
t1 = (1,2,'a','b')
# t1[0] = 'c'                     # # Typeerror : 'tuple' object doesn't support item assignment


# unpacking
t = (1,2,3)
t1,t2,t3 = t
t1

####################################################3

'''
1. 튜플 함수의 count 함수와 동일한 기능을 수행할 수 있는 코드를 작성 하시오.
count 함수를 사용하지 않고도 튜플 자료의 요소 수를 카운트하는 코드를 작성하시오.
'''

t = (1,2,3,4,5)
cnt = 0
find = 1
for x in t:
    if x == find:
        cnt = cnt + 1
print(cnt)

'''
2. 튜플 함수의 index 함수와 동일한 기능을 수행할 수 있는 코드를 작성하시오.
    index 함수를 사용하지 않고도 튜플 자료의 index 번호를 알아낼 수 있는 코드를
    작성하시오.
'''
t = (1,2,3,4,1,2,3,1,2,1)
idx = 2
find = 2
for x in t[idx:]:
    if x == find:
        print(idx)
        break
    idx = idx + 1

'''
3. index함수는 오직 하나의 index 번호만을 알아낼 수 있는 함수이다.
    위 기능을 하나의 index 번호만을 알아내는 것이 아닌 모든 index 번호를 알아낼 수 있는
    코드를 작성하시오.
'''
t = (1,2,3,4,1,2,3,1,2,1)
idx = 0
find = 2
for x in t:
    if x == find:
        print(idx,end=" ")
    idx = idx + 1