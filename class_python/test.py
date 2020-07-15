a = 5
b = 5

print(a+b)
print(id(a))        ## a 변수와
print(id(b))        ## b 변수는 동일한 값으로 id가 같다. 즉, 같은 값을 가리킨다. a -> 5 <- b

print("100 + 100")
print(100+100)
print("%d" % (100+100))

print("%d %5d %05d" % (123, 123, 123))
print("{0:d} {1:5d} {2:05d}".format(123,123,123))
print("{2:d} {1:d} {0:d}".format(100,200,300))

print("%d / %d = %5.1f" % (10,4,10/4))
print("%7.1f" % 123.45)

# 자료형 타입
p1, p2, p3 = '010', '8888', '9999'
pp1 = int(p1)
print(type(p1))
print(type(pp1))

pp1 = pp1 + 10
print(pp1)

#
num1,num2 = 1,2
print('{:d} + {:d} = {:d}'.format(num1,num2,num1+num2))

name,age = '이시형', 28
print('이름 : {}\n나이 : {}'.format(name, age))

eng,kor,math = 100,80,50
tot = eng+kor+math
avg = tot/3
print('합계 : {}\n평균 : {:.2f}'.format(tot, avg))

# input 함수
'''
m1 = input("Message : ")
## m1 = int(input("Message : "))
print(m1)
print(type(m1))
'''






