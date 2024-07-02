# Chapter03_2
#파이썬 문자형
# 문자형 중요

# 문자형 생성
str1 = "I am Python"
str2 = 'Python'
str3 = """How are you"""
str4 = '''Thank you'''

print(len(str3))

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1), len(str1_t1))
print(type(str2_t2), len(str2_t2))

#이스케이프 문자 사용
# I'm Boy
print('I\'m Boy')

excape_str1 = "Do you hava a \"retro games\"?"
print(excape_str1)

t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check!"
print(t_s1)
print(t_s2)


#Raw String 
raw_s1 = r'D:\python\test'
print(raw_s1)

# 멀티라인 입력
multi_str = \
"""
문자열
멀티라인 입력
테스트
"""
print(multi_str)

# 문자열 연산

str_o1 = 'python'
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2)

#문자열 형 변환
print(str(66), type(str(66)))
print(str(10.1))
print(str(True), type(str(True)))

# 문자열 함수 upper isalnum startwith count endswith isalpha
print("Caplitalize  >  ", str_o1.capitalize())
print("endswith? >  " , str_o2.endswith("e"))
print("replace", str_o1.replace("thon", " Good"))
print("sorted : ", sorted(str_o1))
print("split :  ", str_o4.split(' '))

# 반복 시퀀스
im_str = "Good Boy!"

#print(dir(im_str))

for i in im_str:
    print(i)

# 슬라이싱 
str_s1 = "Nice Python"

print(len(str_s1))
# 슬라이싱 연습

print(str_s1[0:3]) # 0부터 3개 나와라 0은 index 3 은 3 - 1 ㄱ까지
print(str_s1[5:11])  # == print(str_s1[5:])
print(str_s1[:len(str_s1)])
print(str_s1[:len(str_s1)-1])
print(str_s1[1:9:2])  # 스킵의미 : 2칸 씩 띄어서
print(str_s1[-5:])
print(str_s1[1:-2])
print(str_s1[::2])

print(str_s1[::-1])


# 아스키 코드
a = 'Z'
print(ord(a)) # ord 함수 아스키 코드 출력
print(chr(122))










