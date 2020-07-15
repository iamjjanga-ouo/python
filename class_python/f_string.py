'''
F-string은 python 3.6이상에서 사용이 가능하다.
Literal String Interpolaton (f-string)

'''
# .format()을 대신하는 f-string
name = 'LeeSiHyung'
age = 10

## Use str.format()
print(".format : my name is {}, I'm {} years old.".format(name,age))
## Use f-string
print(f"f_string : my name is {name}, I'm {age} years old.")        # 소문자 f 또는
print(F"f_string : my name is {name}, I'm {age} years old.")        # 대문자 F


# %-formatting을 대신하는 f-string
x = 10
y = 3
## Use %-formatting
print('x+y = %d | x * y = %d' % (x+y, x*y)) #>>> 'x + y = 13 | x * y = 30'

## Use f-string
print(f'x + y = {x+y} | x * y = {x*y}')


tuple = ('Hi, I am', 'song', 123)
#print('tutple: %s' % (tuple)) --> Error(not all arguments converted during string formatting)
print('tutple: %s' %(str(tuple)))   #>>> "tuple: ('Hi, I am', 'song', 123)"

## Use f-string
print(f'tuple: {tuple}')            #>>> "tuple: ('Hi, I am', 'song', 123)"

## 출처 : https://bluese05.tistory.com/70