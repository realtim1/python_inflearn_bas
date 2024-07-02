#Chapter03-3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형( 순서 O, 중복 O, 수정O, 삭제 O)

# 선언
a = []
b = list()
c = [70, 75, 80, 85] # len
d = [1000, 10000, 'Ace', 'Base', 'Captine']
e = [1000, 10000, ['Ace', 'Base', 'Captine']]
f = [21.42, 'foobar', 3, 4, False, 3.141592]


# 인텍싱
print('>>>>>>>>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] +d[1] +d[1])
print('d - ', d[-1])

print('d - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 슬라이싱

print('>>>>>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# 리스트 연산
print('>>>>>>>>>')
print('c + d ', c + d) # list + list = list
print('c * 3' , c * 3) # 순서 유지
print("Test + c[0]", "Test" + str(c[0])) # str + int 는 형변환이 필요 자바랑 다름

#값 비교
print( c == c[:3] + c[3:])
print()

# Identify (id)
temp = c
print( temp, c)
print(id(temp))
print(id(c)) # 같은 주소값이다.

#리스트 수정, 삭제
print(">>>>>>")
c[0] = 4
print("c : ", c)

print(c[1:2])
c[1:2] = ['a','b','c']
print("c : ", c) #[4, 'a', 'b', 'c', 80, 85]

c[1] = ['a','b','c']
print("c : ", c) # [4, ['a', 'b', 'c'], 'b', 'c', 80, 85]

c[1:3] = []
print(c)

del c[2]
print(c)
print()
print()
print()
print()

print('---------------------')


# 리스트 함수
a = [5, 2, 3, 1, 4]
print('a - ', a)
a.append(6) #뒤에 값 추가
a.sort()
print('a - ', a)

a.reverse()
print(a)
print(a.index(3), a[3])
a.insert(2,7) #위치에 값 삽입
print(a)

#del a[6]
#print(a)
a.remove(6)
print(a)

print(' a - > ' , a.pop()) # 마지막 값을 가져옴
print(a)    # 마지막 값을 빼고 리스트를 구성

print(' a - > ' , a.pop())
print(a) # [5, 7, 4, 3]

print(a.count(4)) # 4의 갯수가 1개 있음// 값 찾기

ex = [8, 9]
a.extend(ex)
print(a)

# remove, pop, del
# remove 원하는값 삭제

# 반복문 활용
while a:
    data = a.pop()
    print(data)















