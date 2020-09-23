# test23.py
# 데이터 시각화
# matplotlib 패키지 설치
# https://matplotlib.org/
# 선그래프, 산점도, 히스토그램, 파이그래프, 막대그래프

import matplotlib.pyplot as plt
import numpy as np
# 선그래프 : 순서가 있는 숫자(변하는 숫자) 데이터를 시각화
data1=[10,14,19,20,25]
# plt.plot(data1)
# plt.show()

x=np.arange(-4.5,5,0.5)
print(x)
y=2*x**2
# plt.plot(x,y)
y2=5*x+30
# plt.plot(x,y2)
y3=4*x**2+10
# plt.plot(x,y3)

# plt.figure(1)
# plt.plot(x,y)
# plt.figure(2)
# plt.plot(x,y2)
# plt.clf()
# plt.plot(x,y3)

# plt.subplot(2,2,1)
# plt.plot(x,y)
# plt.subplot(2,2,2)
# plt.plot(x,y2)
# plt.subplot(2,2,3)
# plt.plot(x,y3)
# plt.show()

# 그래프 꾸미기
# b 파란색  g녹색  r빨강  c청록색 m 자홍색  y노란색  k 검은색  w 흰색
# -실선  --파선 :점선  -.파선점선 혼합
# o원모양 ^위쪽  v아래쪽 < 왼쪽  >오른쪽
# s사각형 p오각형 h,H 육각형  * 별모양  +더하기모양 x X모양 D d 다이아몬드

x=np.arange(0,5,1)
y1=x
y2=x+1
y3=x+2
y4=x+3
# plt.plot(x,y1,'r',x,y2,'b',x,y3,'y',x,y4,'g')
# plt.plot(x,y1,'-',x,y2,'--',x,y3,':',x,y4,'-.')
# plt.plot(x,y1,'>-r',x,y2,'s-g',x,y3,'d:b',x,y4,'-Xc')
# plt.xlabel('X')
# plt.ylabel('Y')
# fontInfo = {'fontname': 'Malgun Gothic'}
# plt.title('제목',fontInfo)
# plt.grid(True)
# 그래프에서 한글처리
import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus']=False
# plt.legend(['데이터1','data2','data3','data4'],loc='lower right')
# plt.legend(['데이터1','data2','data3','data4'],loc='best')
# plt.text(2,2,'데이터1')
# plt.show()

# 산점도 : 두 요소(데이터) 집합관계
height=[165,177,160,180,185]
weight=[62,67,55,74,90]
colors=['r','g','b','c','m']
# plt.scatter(height,weight,s=500,c=colors)
# plt.show()

# 히스토그램 : 정해진 간격으로 나눈후 그 간격안에 들어간 데이터 개수를 막대로 표시한 그래프
#           : 데이터가 분포 되어있는지 확인할때 사용
math=[76,82,84,83,90,86,85,92,72,71,100,87,76,94,78,81,60,79,74,87,82,68,79]
# plt.hist(math,bins=8)
# plt.xlabel('시험점수')
# plt.show()

# 파이그래프 : 원그래프 원안에 각항목별로 비율만큼 부채꼴 크기 영역
fruit=['사과','바나나','딸기','오렌지','포도']
result=[7,6,3,2,2]
# plt.pie(result,labels=fruit)
# 그래프 파일 저장
# plt.savefig('fruit.pdf')
# plt.show()

#막대그래프 : 값 막대의 높이 , 여러항목의 수량이 많고 적음 항목데이터 비교
id=['m1','m2','m3','m4']
# 운동전  윗몸일으키기 개수
before_ex=[27,35,40,33]
# 운동후  윗몸일으키기 개수
after_ex=[30,38,42,37]

# x축 index값
num=len(id)
index=np.arange(num)

# plt.bar(index,before_ex,width=0.4,label='before',color='r')
# plt.bar(index+0.4,after_ex,width=0.4,label='after',color='g')
# plt.xticks(index+0.2,id)
# plt.legend()
# plt.xlabel('회원ID')
# plt.ylabel('윗몸일을키기 횟수')
# plt.title('운동 시작 전 후 비교')
# plt.show()

import numpy as np
import pandas as pd

# 선그래프  move_P.csv 파일 읽어오기  => 선그래프  'b-'
#  서울 전입인구수
# "시점",서울특별시,부산광역시,세종특별자치시,제주특별자치도
# "2013",1520090,478451,23805,88851
# "2014",1573594,485710,56526,92508
# "2015",1589431,507031,83994,97580
# "2016",1515602,459015,65052,106825
# "2017",1472937,439073,82073,105027
# "2018",1439707,416095,86433,104202
pmove=pd.read_csv('move_P.csv',encoding='cp949')
print(pmove)
x=pmove['시점']
# print(x)
y1=pmove['서울특별시']
# print(y1)
# plt.plot(x,y1,'b-',label='서울')
# y2=pmove['부산광역시']
# plt.plot(x,y2,'g--',label='부산')
# plt.legend()
# plt.xlabel("전입인구수")
# plt.show()

# 온라인쇼핑몰 산점도 online.csv 읽어오기 => 산점도
online=pd.read_csv('online.csv',encoding='cp949')
print(online)
x=online['시점']
y1=online['컴퓨터 및 주변기기']
y2=online['가 방']
# plt.scatter(x,y1,s=300,label='컴퓨터', c='r')
# plt.scatter(x,y2,s=500,label='가 방', c='g')
# plt.legend()
# plt.show()

# 막대그래프   출생아수 birth.csv   기준-0.4 기준  기준_0.4
birth=pd.read_csv('birth.csv',encoding='cp949')
print(birth)
x=birth['시점']
# index
index=np.arange(len(x))
print(index)  #[0 1 2]
y1=birth['서울특별시']
y2=birth['부산광역시']
y3=birth['대구광역시']
plt.bar(index-0.3,y3,color='b',width=0.3,label='대구')
plt.bar(index,y2,color='g',label='부산',width=0.3)
plt.bar(index+0.3,y1,color='r',label='서울',width=0.3)
plt.xticks(index,x)
plt.show()





