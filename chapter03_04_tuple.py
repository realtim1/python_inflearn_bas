# Chapter03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형 (순서 O, 중복 O, 수정x, 삭제x) # 불변

# 선언

a = ()

b = (1,) # 원소가 하나 일때는 ,로 끝나야한다. 아니면 int 형임

c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captine')
e = (100, 1000, ('Ace', 'Base', 'Captine'))

print('>>>>>>>>>>>>')
print('d - ', d[1])
print('d - ', d[0]+ d[1] + d[1])
print(d[-1])
print(e[-1])
print(e[-1][1])

print( list(e[-1][1]))

# 수정 x
# d[0] = 1500

# 슬라이싱
print('>>>>>>')
print(' d- ' , d[0:3])
print(d[2:])
print(e[2][1:3])

# 튜플 연산
print('>>>>>>>>')
print('c + d ', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 2)
print('a - ', a)
print(a.index(3))
print(a.count(2))

# 팩킹, 언팩킹 매우 중요

# 팩킹 선언과 같은 개념
t = ('foo', 'bar', 'baz', 'qux')
print(t)
print(t[0])


#언팩킹
(x1, x2, x3, x4) = t # 괄호가 없어도 언팩킹 가능, 하지만 괄호가 있는게 관례
print(type(x1), type(x2), type(x3), type(x4))
print(x1, x2, x3, x4)


# 팩킹 & 언팩킹
t2 = 1, 2, 3 #괄호가 없어도 튜플
t3 = 4, # 하나는 마지막에 , 붙힘
x1, x2, x3 = t2

x4, x5, x6 = 4, 5 ,6

print(t2)
print(t3)
print(x1,x2,x3)
print(x4,x5,x6)

# 튜플의 특징 수정과 삭제는 허용 안되고, 연산은 가능하다.
# 슬라이싱 가능, 함수는 index, count가 존재
# 패킹 언팩킹


















