# Chapter03_1

#숫자형
# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : boolean
str : 문자열 (시퀀스)
list : 리스트 (시퀀스)
tuple : 튜플 (시퀀스)
set : 집합
dict : 사전 java Map 과 같은거 같음
"""


# 데이터 타입
str1 = 'Python'
bool = True
str2 = 'Anaconda'
float = 10.0 # 10 == 10.0 은 다름
int = 7
list = [str1, str2]
dict = {
    "name" : "Machine Learning",
    "version" : 2.0
}
list = [str1, str2]
tuple = (7,8,9)
set = {3,5,7}


# 데이터 타입 출력
print(type(str1))
print(type(bool))
print(type(str2))
print(type(float))
print(type(int))
print(type(list))
print(type(dict))

# 숫자형 연산자

"""
+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x,y) : x의 y제곱 x ** y
"""
i = 77
i2 = -14
big_int = 7777777777778888888888888888888888889999999999999999

# 정수 출력
print(i)
print(i2)
print(big_int)
print()

f = 0.999
f2 = 3.141592
f3 = -3.9
f4 = 3 / 9 

print(f)
print(f2)
print(f3)
print(f4)


# 연산 실습

i1 = 39
i2 = 939
big_int = 7777777777777777777888888888888888888888
big_int2 = 1238843920589403254237580347583027540392
f1 = 1.234
f2 = 3.456

print(">>>>>>> +  ")
print("i1 + i2 : ", i1 + i2)

print("f1 + f2 : ", f1 + f2)

print(big_int + big_int2)

print(">>>>>>> *  ")
print("i1 + i2 : ", i1 * i2)

print("f1 + f2 : ", f1 * f2)

print(big_int * big_int2)

# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7

del float
print(float(b))
del int
print(int(c))
print(int(d))
print(int(True))
print(float(False))
print(complex(3))
print(complex('3'))
print(complex(False))


print(abs(-3))

x, y = divmod(100, 8) # 몫 나머지
print(x, y)

print(pow(5,3), 5 ** 3)

# 외부 모듈
import math
print(math.ceil(5.1))
print(math.pi)










