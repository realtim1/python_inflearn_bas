# Chapter02-1
# 파이썬 완전 기초
# print 사용법
# print 사용법(2023년도)




### 3가지 format Pratices

x = 50
y = 100
text =308212345
n = 'Lee'


# 출력 1
ex1 = 'n = %s, s = %s, sum=%d' % (n, text,  (x+y))

print(ex1)


# 출력 2
ex2 = 'n = {n}, s = {s}, sum={sum}'.format(n=n, s=text,sum=x+y)

print(ex2)

# 출력 3

ex3 = f'n = {n}, s = {text}, sum={x+y}'

print(ex3)

# 구분기호

m = 100000000 

print(f'm : {m :,}') # m : 100,000,000

print()

print()
# 정렬
# ^ : 가운데, < : 왼쪽, > : 오른쪽 정렬
#t :         20
#t cendter :     20  
t = 20
print(f"t : {t:10}")
print(f"t : {t:^10}")
print(f"t : {t:<10}")
print(f"t : {t:>10}")

print()

print()

print(f"t : {t:*^10}") #t : ****20****
print(f"t : {t:#<10}") #t : 20########




