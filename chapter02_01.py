# Chapter02-1
# 파이썬 완전 기초
# print 사용법

print('1python start!')

print()
print("2python start!\n")

print('''3python start!''')
print("""4python start!""")

print('P','Y','T','H','O','N',sep='    ')
print('010','7777','1234',sep='-')
print('python', 'google.com', sep='@')



print()


# end 옵션
print('Welcome to' , end='  ')
print('IT News', end=' ')
print('Web Site')
print()

#file 옵션
# 특정한 파일에 작성함
import sys

print('Learn Python', file=sys.stdout)

print()

#format 사용 (d,s,f) 그외는 많지만 기초만 사용
# d는 정수, s는 문자열, f는 실수(소수)
print('%s %s' % ('one', 'two'))

print('{} {}'.format('one', 'two'))
print('{1} , {0}'.format('one', 'two'))


print()

print('%10s' % ('niee')) #       niee
print('{:>10}'.format('niee'))#       niee


print('%-10s' % ('niee')) #niee     
print('{:10}'.format('niee'))#niee      

print('{:_>10}'.format('niee'))#______niee

print('{:^10}'.format('niee'))#   niee    중앙 정렬

print('%.5s' % ('nice')) #nice 
print('%.5s' % ('python study'))#pytho


print('{:10.5}'.format('pythonstudy'))# 총 10글자를 확보했는데 5글자만 나와라, 공간은 10개


# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))

print('{:4d}'.format(42))


# %f
print('%.18f' % (3.14123213213123))
print('{:f}'.format(3.14123213213123))

print('%06.2f' % (3.141592123456789))#003.14

print('{:06.2f}'.format(3.141592123456789)) #003.14

print()





















