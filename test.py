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

int('1008',8)