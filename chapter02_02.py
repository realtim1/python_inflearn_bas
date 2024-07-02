# Chapter02-2

#기본 선언

n = 700


print(n)

print( type(n))
print()

# 동시 선언
x = y = z= 700

print(x,y,z)
print()
# 선언
var = 75

# 재선언
var = 'Change Value'

print(var)
print(type(var))
print()

# Object References
# 변수 값 할당 상태
# 1. 타입에 맞는 오브젝트 생성
# 2. 값 생성
# 3. 콘솔 출력

# 예1)
print(300)
print(int(300))

# 예2)
# n -> 777
n = 777

print(n, type(n))

m = n
# m -> 777 <- n

print(m, n)
print(type(m), type(n))

print()

m = 400

print(m, n)
print(type(m), type(n))

print()


# id( identity 확인) : 객체의 고유값 확인

m = 800
n = 655

print(id(m)) # java 주소값과 같은 거 같음
print(id(n))

print(id(m) == id(n))

m = 800
n = 800

print(id(m)) # 같은 값은 같은 주소값을 참조함
print(id(n))

print(id(m) == id(n))

# 변수 선언
# Camel Case : iLoveYou -> Method 에서 사용
# Pascal Case : ILoveYou -> Class 생성에서 사용
# Snake Case : i_love_you -> 변수 생성할 때 사용 (파이썬에서)

# 허용하는 변수 선언 법

age = 1
Age = 2
aGe = 3
AGE = 4
a_g_e = 5
_age = 6
age_ = 7
_AGE_ = 8

# 예약어는 변수명으로 불가능 ex for, class, False







