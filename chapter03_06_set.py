# Chapter03-6
# 집합(set) 특징
# 집합(set) 자료형( 순서x, 중복x)

# 선언
a = set()
b = set([1, 2, 3, 4,4])
c = set([1, 4, 5, 6])
d = set([1, 2, 'Pen', 'Cap', 'Plate'])

e = {'foo', 'bar', 'baz','foo','qux'} # key가 없이 원소만 나열되면 set이다.

f= {42, 'foo', (1,2,3), 3.141592}

print(a) # 중복은 제거함
print(b)
print(c)
print(d)
print(e)
print(f)

# 튜플 변환 ( set - > set)
t = tuple(b)
print(type(t), t) # 튜플로 변되었다는건 슬라이싱을 할 수 있다는 것
print(t[0], t[1:3])


# 리스트 변환 ( set -> List)
l = list(c)
l2 = list(e)

print('l - ' ,l)
print('l2 - ' ,l2)

print(len(a))
print(len(b))
print(len(c))
print(len(d))
print(len(e))



#집합 자료형 활용
s1 = set({1, 2, 3, 4, 5})
s2 = set([5,6,7,8,9])
print('s1 & s2', s1 & s2)
print( s1.intersection(s2)) # 교차

print(s1 | s2)
print('s1 | s2 합집합 : ', s1.union(s2))

print(s1 -s2)
print('s1 - s2 차집합', s1.difference(s2))

# 중복 원소 확인
print('s1 & s2 :', s1.isdisjoint(s2))# 교집합이 있으면 false, 없으면 True

# 부분 집합 확인
print(s1.issubset(s2))

print(s1.issuperset(s2))

# 추가 & 제거
s1 = set([1,2,3,4])
s1.add(5)
print('s1' , s1)
s1.remove(2) # 값이 없는 것을 삭제할떄 에러가 남

print(s1)


s1.discard(7) # 값이 없는 것을 삭제해도 에러가 나지 않음
print(s1)

s1.clear()
print(s1)

# set 은 집합이다










