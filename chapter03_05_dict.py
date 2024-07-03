#Chapter03-5
#파이썬 딕셔너리
# 범용적으로 가장 많이 사용 (Json)형식
# 딕셔너리 자료형 ( 순서 x (무작위), 중복 허용 x, 수정o, 삭제o) Java에서 map 과 같은거 같음

# 선언
a = {'name': 'Kim'
    ,'phone' : '01012345678'
    ,'birth' : '881212' 
}
b = {0 : 'Hello Python'}
c = {'arr' : [1, 2, 3, 4]}
d = {
    'Name': 'NickMan',
    'City': 'Seoul',
    'Age': 33,
    'Grage': 'A',
    'Status': True
}
e = dict([
    ('Name', 'NickMan'),
    ('City', 'Seoul')
])

f = dict(
    Name = 'NiceMan',
    City = 'Seoul',
    Age = 33,
    Grage = 'A',
    Status = True
)

print(type(a), a)

print(type(b), b)
print(type(c), c)
print(type(d), d)
print(type(e), e)
print(type(f), f)
print()

# 출력 
#print(a['name1']) #Kim  key 없을 떄는 Error 발생
print(a.get('name1')) # key 없을 때 None 출력, 안정적임
print(b)
print(b[0]) # Hello Python
print(b.get(0)) # Hello Python

print()
print(f.get('City')) # Seoul
print(f.get('Age')) # 33

# 딕셔너리 추가
a['address'] = 'seoul' # key 가 같으면 수정해버림 동적으로
print(a)

a['rank'] = [1,2,3]
# dict length
print(a)
print(len(a)) # key의 갯수를 셈
print(len(b))
print(len(c))
print(len(d))

# dict_keys, dict_values, dict_items : 반복문(__iter__)에서 사용 가능

print(a.keys()) # 키 값만 가져옴
print(b.keys())
print(c.keys())
print(d.keys())

print(list( a.keys())) # list로 형변환 가능 ['name', 'phone', 'birth', 'address', 'rank']

print(a.values()) # 값만 가져옴

print(b.values())
print(c.values())

print(list(a.values())) # ['Kim', '01012345678', '881212', 'seoul', [1, 2, 3]]

print()
print()
print()

print(a.items())
"""
키와 벨류가 하나의 튜플 한쌍으로 나옴
dict_items([('name', 'Kim'), ('phone', '01012345678'), ('birth', '881212'), ('address', 'seoul'), ('rank', [1, 2, 3])])
"""
print()
print()
print()
print(list(a.items()))

""" list 형변환
[('name', 'Kim'), ('phone', '01012345678'), ('birth', '881212'), ('address', 'seoul'), ('rank', [1, 2, 3])]
"""

print(a.pop('name')) # pop으로 꺼내오고
print(a) # 꺼내온 값을 제외하고 딕셔너리 출력

print(f.popitem()) # 아무거나 임의로 하나를 꺼내옴
print(f)
#딕셔너리는 순서 보장을 안하기 떄문에 무작위 꺼내옴

print()

print('birth' in a)  # 있으면 True 없으면 False
#키를 포함하고있는지 조회 할 수 있음

# 수정
a['test'] = 'test_dict' # insert
print(a)

a['address'] = 'dj' #update
print(a)

a.update(birth='121212') # update Method
print(a)

temp = {'address': 'Busan'} # update
a.update(temp)
print(a)



































