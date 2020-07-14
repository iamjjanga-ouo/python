import sys

## 변수 선언부 ##
intVar, floatVar, boolVar, strVar, listVar, tupleVar, dictVar, setVar = [None]*8

## 메인 코드부 ##
if __name__ == "__main__":
    intVar = 0
    floatVar = 0.0
    boolVar = True
    strVar = ''
    listVar = []
    tupleVar = ()
    dictVar = {}
    setVar = set()

print('int size ->', sys.getsizeof(intVar))
print('float size ->', sys.getsizeof(floatVar))
print('bool size ->', sys.getsizeof(boolVar))
print('str size ->', sys.getsizeof(strVar))
print('list size ->', sys.getsizeof(listVar))
print('tuple size ->', sys.getsizeof(tupleVar))
print('dictionary size ->', sys.getsizeof(dictVar))
print('set size ->', sys.getsizeof(setVar))