# test3.py
# list자료형   [] 표현
a=[1,2,3,4,5]
b=['a','b','c']
c=[1,2,'a','b']
d=[]

print(a)
print(a[0])
print(a[-1])
print(a[0:2])  #[1, 2]
print(a[:2])  #[1, 2]
print(a[2:]) #[3, 4, 5]
#배열 크기
print(len(a))  #5
a=[1,2,3]
b=[4,5,6]
print(a+b)   #[1, 2, 3, 4, 5, 6]
print(a*3)  #[1, 2, 3, 1, 2, 3, 1, 2, 3]

#수정 변경 삭제
a[2]=4
print(a)  #[1, 2, 4]
a[1:2]=['a','b','c']
print(a)  #[1, 'a', 'b', 'c', 4]
# 삭제
a[1:3]=[]
print(a)  #[1, 'c', 4]
del(a[1])
print(a)  # [1, 4]

# 값  in 리스트  : 리스트안에 값이 있으면 True, 없으면 False
pocket=['paper','phone','money']
print('money' in pocket)  #True
print('card' in pocket)   #False
# 주머니 'money'있으면 택시타라
#              없으면 걸어가라
if 'money' in pocket:
    print("택시타라")
else:
    print("걸어가라")

# 리스트 함수
# 리스트 추가
a=[1,2,3]
a.append(4)
print(a)  #[1, 2, 3, 4]

# 요소삽입  리스트 0번째 값 0 삽입
a.insert(0,0)  # [0, 1, 2, 3, 4]
print(a)

# 요소제거
a.remove(0)
print(a)  # [1, 2, 3, 4]

# 뒤집기
a.reverse()
print(a) #[4, 3, 2, 1]

# 오름차순 정렬
a.sort()
print(a) #[1, 2, 3, 4]

# 리스트안에 값의 위치
print(a.index(3))  #2위치

# .pop  리스트에서 끄집어 내기  - 마지막 요소 가져와서 삭제
print(a.pop())  #4
print(a)  #[1, 2, 3]

a=[1,2,3,4,[5,6,7],[8,[9,10]]]
# a[1차원순서][2차원순서][3차원순서]
# 6출력
print(a[4][1])
# 9출력
print(a[5][1][0])

# 수학점수
# list변수 jum 선언 90,75,30,100,85 저장
# 평균 출력
jum=[90,75,30,100,85]
print(len(jum))  #5
print((jum[0]+jum[1]+jum[2]+jum[3]+jum[4])/len(jum))

#튜플  tuple형 : list동일 값 변경 못함

t1=()
t2=(1,)
t3=(1,2,3)
print(t3[1])  #2
# 튜플형 값변경 못함
# t3[0]=0  #'tuple' object does not support item assignment
# del(t3[0])
print(t2+t3) #(1, 1, 2, 3)
print(t3*3) #(1, 2, 3, 1, 2, 3, 1, 2, 3)

# 딕셔너리 자료형  단어:뜻   키:값
#     {키1:값1,키2:값2}

# [
#     {"id":'kim',"pass":"p123"},
#     {"id":'lee',"pass":"p456"}
# ]

d={"id":'kim',"pass":"p123","name":"kimgil"}
print(d)  #{'id': 'kim', 'pass': 'p123', 'name': 'kimgil'}

print(d['id'])  #kim

# 딕셔너리 추가  1:'a'
d[1]='a'
print(d)  #{'id': 'kim', 'pass': 'p123', 'name': 'kimgil', 1: 'a'}
# 'n':'lee' 추가
d['n']='lee'
print(d)  #{'id': 'kim', 'pass': 'p123', 'name': 'kimgil', 1: 'a', 'n': 'lee'}

# 딕셔너리 수정   1:'aa'
d[1]='aa'
print(d)  #{'id': 'kim', 'pass': 'p123', 'name': 'kimgil', 1: 'aa', 'n': 'lee'}

# 딕셔너리 삭제
del(d['n'])
print(d)  #{'id': 'kim', 'pass': 'p123', 'name': 'kimgil', 1: 'aa'}

print(d[1])    #aa
print(d.get(1)) #aa

# 1키 삭제
del(d[1])
print(d)  # {'id': 'kim', 'pass': 'p123', 'name': 'kimgil'}

# 딕셔너리 함수
# 키값들만 가져오기
print(d.keys())  #dict_keys(['id', 'pass', 'name'])
print(type(d.keys()))  # <class 'dict_keys'>
#  dict_keys  => list 형변환
li=list(d.keys())
print(li)  # ['id', 'pass', 'name']

print(d.values())
# dict_values => list 형변환
li2=list(d.values())
print(li2)  #['kim', 'p123', 'kimgil']

print(d.items())  #dict_items([('id', 'kim'), ('pass', 'p123'), ('name', 'kimgil')])
# dict_items => list
li3=list(d.items())
print(li3)  #[('id', 'kim'), ('pass', 'p123'), ('name', 'kimgil')]
print(li3[0])  #('id', 'kim')
print(type(li3[0]))  #<class 'tuple'>
print(li3[0][0])  #id
print(li3[0][1])  #kim

# 딕셔너리 내용 전체 삭제
d.clear()
print(d) #{}

# 집합자료형
# set    순서없음   중복허용 하지 않음

s1=set([1,2,3])
print(s1)  # {1, 2, 3}

s2=set("Hello")
print(s2)  # {'o', 'l', 'e', 'H'}

# list, tuple 형변환
l=list(s1)
print(l)  #[1, 2, 3]
t=tuple(s1)
print(t)  #(1, 2, 3)

# 차집합, 교집합, 합집합
s1=set([1,2,3,4,5,6])
s2=set([4,5,6,7,8,9])
# 교집합
print(s1&s2)  #{4, 5, 6}
print(s1.intersection(s2))  #{4, 5, 6}
# 합집합
print(s1|s2)  #{1, 2, 3, 4, 5, 6, 7, 8, 9}
print(s1.union(s2))  #{1, 2, 3, 4, 5, 6, 7, 8, 9}
# 차집합
print(s1-s2)  #{1, 2, 3}
print(s1.difference(s2)) #{1, 2, 3}

# 추가
s1.add(10)
print(s1)  #{1, 2, 3, 4, 5, 6, 10}

# 여러개 추가
s1.update([11,12,13])
print(s1)  #{1, 2, 3, 4, 5, 6, 10, 11, 12, 13}

# 삭제
s1.remove(2)
print(s1)  #{1, 3, 4, 5, 6, 10, 11, 12, 13}

# 모든형 클래스 형
a=1
print(type(a))  #<class 'int'>
# a변수 주소값
print(id(a))  #140724597981456

# 리스트 복사(같은 주소 가리킴)
a=[1,2,3]
b=a
print(id(a))  # 2426476842312
print(id(b))  # 2426476842312

print(a is b)  # True  동일한 객체를 가리키고 있음

# a리스트 두번째 내용을  4로 변경
a[1]=4
print(a)  #[1, 4, 3]
print(b)  #[1, 4, 3]

# 리스트 복사(다른 주소 가리킴)
a=[1,2,3]
b=a[:] # 리스트 a 처음부터 끝요소 슬라이싱
print(a)  #[1, 2, 3]
print(b)  #[1, 2, 3]
print(id(a))  #2235149210120
print(id(b))  #2235154379592
print(a is b)  #False

# 리스트 복사(다른 주소 가리킴)  copy
from copy import copy
a=[1,2,3]
b=copy(a)  # 값 복사해 옴
print(a)  #[1, 2, 3]
print(b)  #[1, 2, 3]
print(id(a))  #2472931577736
print(id(b))  #2472926204424
print(a is b)  #False

a,b=10,20
print(a)  #10
print(b)  #20
a,b=('a','b')
print(a)  #'a'
print(b)  # 'b'
(a,b)='c','d'
print(a)  # 'c'
print(b)  # 'd'


























