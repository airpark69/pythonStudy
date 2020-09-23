# test5.py
# 함수 : 자주 사용하는 명령들을 모아서 정의
# 함수 이름 호출 사용
# def 함수이름(매개변수):
#     실행문1
#     실행문2
#     return
# 함수이름(값)

# 두수를 받아서 두수의 합을 구해서 리턴하는 함수  sum()
def sum(a,b):
    return a+b
# 함수 호출
print(sum(10,20))

# eng점수를 받아서 합을 구해서 리턴 sum2()
def sum2(eng):
    s=0
    for i in eng:
        s=s+i
    return s

eng=[90,80,70,50,60,100]
print(sum2(eng))

# eng점수를 받아서 최대값을 구해서 리턴 max2() 함수 정의
def max2(eng):
    m=0
    for e in eng:
        if m < e:
            m=e
    return m

print(max2(eng))

def sum3(*a):
    # *a 리스트 변수
    s=0
    for i in a:
        s=s+i
    return s

print(sum3(1,2,3))
print(sum3(1,2,3,4,5,6))
print(sum3(1,2,3,4,5,6,7,8,9,10))

# 함수 매개변수 초기값설정, 마지막인수 설정, 호출시 생략가능
def my(name,old,man=True):
    print(name)
    print(old)
    print(man)

my("홍길동",21) # 기본값 호출시 생략가능
my("유관순",18,False)

# lambda() 람다 함수  한줄 함수 정의
# 함수이름 = lambda 매개변수1,매개변수2 :실행문 변수1+변수2

# def sum(a,b):
#     return a+b

lsum=lambda a,b:a+b
print(lsum(10,20))

# square()  두수를 받아서    2**3    람다함수 정의
square=lambda a,b:a**b
print(square(2,3))

# mylist=[lambda 함수,lambda 함수]
mylist=[lambda a,b:a+b,lambda a,b:a**b]
# mylist[0](3,4)
print(mylist[0](3,4))
print(mylist[1](4,5))

# 내장함수 이용 map(), lambda 함수 
# map(람다함수,리스트자료)
# two_times 함수  - 리스트를 받아서  *2  => list에 저장
def two_times(numlist):
    result=[]
    for num in numlist:
        result.append(num*2)
    return result

print(two_times([1,2,3,4]))  # 2,4,6,8

# 람다 함수  하나의 수를 받아서  *2
ltwo_times=lambda num:num*2
# list(map(람다함수,리스트자료))
print(list(map(ltwo_times,[1,2,3,4])))  #[2, 4, 6, 8]
print(list(map(lambda num:num*2,[1,2,3,4])))  #[2, 4, 6, 8]

# list map 람수함수   리스트자료형
#  list *100 => list
li=[1.25,3.45,2.56,5.77,8.76]
print(list(map(lambda n:n*100,li)))

# filter(람다함수,리스트)  람다함수를 통해서 데이터 선택해서 결과
def pos(x):
    return x>0

print(list(filter(pos,[1,-3,2,0,-5,6])))  #[1, 2, 6]
# pos => 람다함수 변경
print(list(filter(lambda x:x>0,[1,-3,2,0,-5,6])))  #[1, 2, 6]

# 내장 함수
print(len("문자열")) # 길이
# max() min() type() int() float() str()  list() tuple()  set() abs()
print(divmod(7,3))   #(2, 1)
print(eval('1+2')) # 식 => 계산 해주는 함수
print(pow(2,3)) #2의3승
print(ord('a'))  #아스키코드값
print(oct(9)) #8진수
print(hex(17)) #16진수
print(sorted([3,1,2])) #정렬
# range(1,11,1) 
print(all([1,2,3,4,0]))   #모두 0이 아닌값  True 0하나라도 있으면 False
print(any([1,2,3,4,0]))   # 0하나라도 아닌값  True 모두0이면 False




