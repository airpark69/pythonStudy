# test9.py

# 모듈: 파이썬 파일(변수, 함수, 클래스 들을 모아 놓은 파일)

def sum(a,b):
    return a+b

# cmd
# d:
# cd D:\Shared\JSP\workspace_py5\py1
# dir
# python
# print(sum(10,20))  TypeError: 'int' object is not iterable
# import 모듈이름(파일이름)
# import test9
# print(test9.sum(10,20))

# from 모듈이름 import sum
# from test9 import sum
# sum(10,20)

# safe_sum 함수 정의  두수를 받아서  
# if 두수의 타입  type() 이 다르면  리턴 "더할수 없는 데이터"
#                         같으면  리턴  두수를 더해서 리턴
def safe_sum(a,b):
    if type(a)!=type(b):
        return  "더할수 없는 데이터"
    else:
        return sum(a,b)

# import 모듈이름(파일이름)  as 애칭
# import test9 as t
# print(t.sum(10,20))
# print(t.safe_sum(10,'a'))

# from 모듈이름 import 함수이름,함수이름
# from test9 import sum,safe_sum
# from test9 import *
# sum(10,20)
# safe_sum(10,20)
# safe_sum(10,'a')

# 변수 정의
PI=3.141592
# Math 클래스 정의
#  solv 함수 정의  반지름 받아서  원면적구해서 리턴
class Math:
    def solv(self,r):
        return r*r*PI

# 테스트 용으로 파일 실행 할때 동작
# import 할때는 동작 안됨
if __name__=="__main__":
    # Math객체 생성
    m=Math()
    # solv 함수 호출
    print(m.solv(10))
    # sum함수 호출
    print(sum(10,20))
    # safe_sum 함수 호출
    print(safe_sum(10,"a"))
