# test6.py
# 클래스

# class 클래스이름:
#     멤버변수
#     멤버함수

# 클래스 정의
class Simple:
    pass

# 클래스 사용 => 객체생성
s=Simple()

# 클래스 정의  Service클래스 이름  
# 변수 a=10
# 함수 prn(self) "함수정의"출력
# 함수 sum2(self, a,b) 두수받아서 두수합리턴
class Service:
    a=10
    def prn(self):
        print("함수정의")
    def sum2(self,a,b):
        return a+b

# 객체생성
s=Service()
# 멤버변수, 메서드호출
print(s.a)
s.prn()
print(s.sum2(10,20))

#클래스 정의 Shape
# 멤버함수 CircleArea(r)  원의면적구해서 리턴
# 멤버함수 RectangleArea(w,h) 사각형의 면적구해서 리턴
class Shape:
    def CircleArea(self,r):
        return r*r*3.14
    def RectangleArea(self,w,h):
        return w*h

#객체생성
s=Shape()
# CircleArea 메서드 호출  반지름 10
print(s.CircleArea(10))
# RectangleArea 메서드 호출 너비 10  높이 20
print(s.RectangleArea(10,20))

#초기값  설정 함수
class Person:
    def __init__(self,name,age):
        # 인스턴스 변수 self.name
        self.name=name
        self.age=age
    def intro(self):
        print("이름",self.name,"나이",self.age)

# 객체생성
# TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
p=Person("홍길동",20)
p.intro()

#클래스 FourCal  초기값 a,b 받아서 self.a  self.b 변수 설정 저장
# sum() 두수 합구해서 리턴
# sub() 두수 차 리턴
# mul() 두수 곱 리턴
# div() 두수 나누기해서 리턴
class FourCal:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sum(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b
# 객체생성
f=FourCal(10,20)
# 메서드 호출
print(f.sum())
print(f.sub())
print(f.mul())
print(f.div())


#  클래스 상속
class Parent:
    def parent_prn(self):
        print("부모클래스 prn() 함수")

class Child(Parent):  # Parent클래스 상속
    def child_prn(self):
        print("자식클래스 prn() 함수")
    #메서드 오버라이딩 : 부모함수 재정의   
    def parent_prn(self):
        print("자식클래스가 재정의한 부모클래스 prn() 함수")

c=Child()
c.parent_prn()
c.child_prn()

#  부모클래스  Bicycle
#  초기값 color   => self.color 저장
#  move(speed) 메서드정의 speed받아서  출력  color 자전거 시속 speed 킬로 전진
#  stop()  메서드정의 출력 color 자전거 정지
class Bicycle:
    def __init__(self,color):
        self.color=color
    def move(self,speed):
        print(self.color,"자전거 시속",speed,"킬로 전진")
    def stop(self):        
        print(self.color,"자전거 정지")
#  자식클래스 FoldBicycle  상속 Bicycle
#  fold() 메서드 정의  출력 color 자전거 접기
#  stop() 메서드 오버라이딩  출력  color 폴더 자전거 정지
class FoldBicycle(Bicycle):
    def fold(self):
        print(self.color,"자전거 접기")
    def stop(self):
        # 부모의 메서드 호출
        super().stop()
        print(self.color,"폴더 자전거 정지")
# FoldBicycle 객체생성   move(speed) fold()  stop() 메서드 호출
f=FoldBicycle("노란색")
print(f.color)
f.move(10)
f.fold()
f.stop()

#  __add__   __sub__
# 부모클래스 HousePark
# 멤버변수  lastname="박"
# 초기값 name받아서  self.fullname 변수 <= self.lastname+name
# 메서드 travel(where)  출력 fullname이 where 여행가다

# HousePark 객체생성
# travel메서드호출

# 자식클래스 HouseKim   상속 HousePark
# 멤버변수 lastname="김"
# travel(where,day) 메서드 오버라이딩  출력 fullname where에 day일 여행가다 

#HouseKim 객체생성
#travel 메서드 호출



















