'''
딕셔너리란?
: 대응관계 / "이름" = "홍길동", "생일" = "19940119"

key - value 한 쌍으로 갖는 자료형

{key1:Value1, Key2:Value2, Key3:Value3}

Key -> 변하지 않는 값
Value -> 변하는 값 or 변하지 않는 값
'''

## 기본형태
dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}

a = {1:'hi'}        # Key(정수값) : Value(문자열)
a = {'a':[1,2,3]}   # Key(문자열) : Value(리스트)

# 딕셔너리 쌍 추가, 삭제하기

## 딕셔너리 쌍 추가
a = {1:'a'}
a[2] = 'b'          # >>> {1: 'a', 2: 'b'}
a['name'] = 'pey'   # >>> {1: 'a', 2: 'b', 'name': 'pey'}
a[3] = [1,2,3]      # >>> {1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}

## 딕셔너리 요소 삭제
del a[1]            # >>> {2: 'b', 'name': 'pey', 3: [1, 2, 3]}

## 딕셔너리 만들 때 주의할 사항
a = {1:'a', 1:'b'}  # {1:'b'} <--- 동일 key 사용은 이전 값을 덮어쓰게된다.


# 딕셔너리 관련 함수들
## Key 리스트 만들기 (keys)
a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
a.keys()            # >>> dict_keys(['name', 'phone', 'birth'])

'''
python 2.7 까지는 List 형태로 반환  ['name', 'phone', 'birth']
python 3.0 이후에는 객체를 반환 dict_keys(['name','phone','birth'])

객체 반환 값을 리스트로 변환하고자 할때 : list(a.keys())
'''

### dict_keys 객체는 for문 사용가능. 하지만 append,insert,pop,remove,sort는 사용 X
for k in a.keys():
    print(k)

## Value 리스트 만들기 (values)
a.values()          # >>> dict_values(['pey', '0119993323', '1118'])

## Key,Value 쌍 얻기 (items)
a.items()           # >>> dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])

## key로 Value얻기 (get)
a.get('name')       # >>> 'pey'
a.get('phone')      # >>> '0119993323'

    ### a['nokey']와 a.get('nokey')의 차이
    print(a.get('nokey'))
    # >>> None
    print(a['nokey'])
    # Keyerror

### default 값 설정
a.get('foo', 'bar')  # >>> 'bar'    <--- 'foo'가 없을 경우 'bar'를 대신 가져옴

## 해당 key가 딕셔너리 안에 있는지 조사 (in)
'name' in a          # >>> True
'email' in a         # >>> False

## Key: Value 쌍 모두 지우기 (clear)
a.clear()
