'''
리스트
'''
# aa = [10,20,30,40]

# aa[0:3]     #>>> [10,20,30] ## a[3]은 포함하지 않음
# aa[2:4]     #>>> [30,40]

# aa[:2]      #>>> [10,20]
# aa[2:]      #>>> [30,40]

'''
리스트 간 덧셈 곱셉 가능
'''

# aa = [10,20,30]
# bb = [40,50,60]
# aa + bb     #>>> [10,20,30,40,50,60]
# aa * 3      #>>> [10,20,30,10,20,30,10,20,30]

'''
::[number]은 리스트를 [number]만큼 뛰어서 호출
'''
# aa = [10,20,30,40,50,60,70]
# aa[::2]     #>>> [10,30,50,70]
# aa[::-2]    #>>> [70,50,30,10]
# aa[::-1]    #>>> [70,60,50,40,30,20,10] ## 역순 출력

'''
리스트 값 변경
'''
# aa = [10,20,30]
# aa[1] = 200 #>>> [10,200,30]

# aa = [10,20,30]
# aa[1:2] = [100,101] #>>> [10,100,101] -> [1:2]는 1번째부터 다음 1번째(2-1=1)를 의미

# aa = [10,20,30]
# aa[1] = [100,101] #>>> [10,[100,101],30] -> 리스트 안의 리스트


'''
리스트 삭제
'''
# aa = [10,20,30]
# del(aa[1])      #>>> [10,30]

# aa = [10,20,30,40,50]
# aa[1:4] = []    #>>> [10,50] -> 1~3까지 삭제

# aa = [10,20,30]; aa=[]; aa      #>>> []                 -> 빈리스트로 만들기
# aa = [10,20,30]; aa=None; aa    #>>> 아무것도 출력안됨   -> 빈 변수 만들기
# aa = [10,20,30]; del(aa); aa    #>>> 오류               -> 변수 삭제

'''
리스트 조작 함수
'''
myList = [30,10,20]
print("현재 리스트 : %s" % myList)

myList.append(40)
print("append(40) 후의 리스트 : %s" % myList)

print("pop()으로 추출한 값 : %s" % myList.pop())
print("pop() 후의 리스트", myList)

myList.sort()
print("sort() 후의 리스트 : ", myList)

print("20값의 위치 : %d" % myList.index(20))

myList.insert(2,222)
print("insert(2,222) 후의 리스트 : %s" % myList)

myList.remove(222)
print("remove(222) 후의 리스트 : %s" % myList)

myList.extend([77,88,77])
print("extend([77,88,77] 후의 리스트 : %s" % myList)

print("77의 개수 : %d" % myList.count(77))
