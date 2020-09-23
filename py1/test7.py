# test7.py
# 예외처리 : 논리적오류, 물리적 오류 발생  처리

print("프로그램 시작")
a=4
b=0
if b!=0:
    print(a/b)  #ZeroDivisionError: division by zero
else:
    print("0으로 나눔")
print("프로그램 끝")

print("프로그램 시작")
try:
    print(a/b)
except ZeroDivisionError as e:
    print(e)
finally:
    print("예외상관없이 마무리")
print("프로그램 끝")

print("프로그램 시작2")
a=[1,2,3]
try:
    print(a[3])  # IndexError: list index out of range
except IndexError as e:
    # print(e)
    # 오류발생 => 회피  pass
    pass
finally:
    print("생략가능")
print("프로그램 끝2")

# 오류 일부러 발생시키기
class Bird:
    def fly(self):
        raise NotImplementedError # 오류 일부러 발생
# b=Bird()
# b.fly()  #raise NotImplementedError # 오류 일부러 발생

#  클래스 Eagle Bird상속
#  fly() 메서드오버라이딩  출력 "fly() 메서드 오버라이딩"
class Eagle(Bird):
    def fly(self):
        print("fly() 메서드 오버라이딩")
#  Eagle 객체 생성 
#  fly() 메서드 호출
e=Eagle()
e.fly()