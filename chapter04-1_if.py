#Chapter04-1
# 파이썬 제어문
# if 실습

# 기본형식
print(type(True)) # 0이 아닌 수 "abc" [1,2,3....], (1,2,3...)
print(type(False)) # 0 ,"", (), {}, []

# 예1

if True:
    print('Good')

if False:
    print('Bad')

# 예2
if False:
    print('Bad!')
else:
    print('Good!')
print()

# 관계 연산자
# >, >=, <, <=, ==, !=
x = 15
y = 10
print(x == y)

print(x != y)

print(x > y)

print(x < y)

city = ""

if city:
    print("You are in: ", city)
else :
    print("plz entere your city")

 
city = "seoul"

if city:
    print("You are in: ", city)
else :
    print("plz entere your city")

# 논리연산자(중요)
# and or not
a = 75
b = 40
c = 10

print('and ', a > b and b > c)
print('or ', a > b or b < c)
print( 'not ' , not a> b)

# 산술, 관계, 논리 우선 순위
# 산술 > 관계 > 논리
print('e1 : ', 3+12 > 7+3)

print('e2 : ', 5 + 10 * 3 > 7 + 3 * 20)


























