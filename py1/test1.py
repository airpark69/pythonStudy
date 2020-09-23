# test1.py 주석 ctrl /
print("Hello")
#  처음실행 파일선택 alt shift f10
print("안녕")
#  두번째 실행 shift f10
a=10
b=20
print(a+b)
"""
여러줄
주석
"""
'''
주석
주석
'''
a=3.4
a=0x11

# 연산자
#  + - * /  **(제곱)  //(몫)   %(나머지)
a=2**3
print(a)
a=5/2
print(a)  #2.5
a=5//2
print(a)  #2
a=5%2
print(a) #1

# 연산자 우선순위
# 1.괄호
# 2. ** 제곱
# 3. - 음수
# 4. * / // %
# 5. + -
a=10
a+=1
print(a)

# 여러변수 할당
a,b=20,100
print(a)
print(b)

# 자료형 확인
print(type(a)) # <class 'int'>
a=4
b=2
print(a/b) #2.0
print(type(a/b))   #<class 'float'>

#형변화
a=3.4
print(int(3.4)) #3

# 문자열
a='aa'
a="bbb"
a="""cccc"""
a='''dddd'''
print(type(a))  #<class 'str'>

# 문자열 연결  문자+문자   숫자+숫자    숫자+문자(에러)
a="kim"
b="gil dong"
print(a+b)
print(50+100)
# print(a+b+100)  에러발생

# * 반복   문자열반복   리스트반복
print("="*100)
# 문자열 길이
print(len(b))

# 문자열 순서부여
a="hello~~, python"
print(a[0]) #h
print(a[-1]) #n 뒤에서 첫번째
print(a[9:15]) # python
print(a[9:]) # python
print(a[:9])  #hello~~,
# 문자열 수정 -> 에러
# a[0]="a" #'str' object does not support item assignment

# 문자열 내장함수
a="hello~~, python"
# 찾는 문자열 개수
print(a.count('h')) #2
# 찾는 문자열 위치
print(a.find('y')) #10
print(a.find('x')) #-1
print(a.index('y')) #10
# print(a.index('x')) #에러발생
# 문자열.join() 문자열 삽입
b=","
print(b.join('abcd'))  #a,b,c,d
#  upper()  lower()   대문자 소문자  
#  lstrip() rstrip()  strip()  왼쪽여백 지우기
#  문자열 바꾸기 replace('python','java')

#문자열 나누기
b="a:b:c:d"
print(b.split(':'))

#  출력
print("a="+a)
print("a=",100)
# 문자열 포맷 이용해서 출력
# %d 정수 %s 문자열 %f실수 %c 문자1개  %o 8진수 %x 16진수 %%
a=10
b="apple"
print("%d+%s" % (a,b))
print("바구니에 %s이 %%있다" % b)
# 바구니에 apple이 10개 있다
print("바구니에 %s이 %d개 있다" % (b,a))

print("%10s" % "hi")  #        hi
print("%-10s" % "hi")  #hi

print("%f" % 3.42134234)  #3.421342
print("%0.4f" % 3.42134234)  #3.4213
print("%10.4f" % 3.42134234)
print("%-10.4f" % 3.42134234)

print("바구니에 %s이 있다" % b)
print("바구니에 {0}이 있다.".format(b))





