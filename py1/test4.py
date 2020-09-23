# test4.py

# while  ,  for
# 초기값
# while 조건:
#     반복문
#     초기값 증가

#  1~ 10 출력
i=1
while i<=10:
    print(i,end=" ")
    i=i+1
print()
# 1~10 합 출력
sum=0
i=1
while i<=10:
    sum=sum+i
    i=i+1
print(sum)

# 1~10 짝수의 합 출력
sum=0
i=1
while i<=10:
    if i%2==0:
        sum=sum+i
    i=i+1
print(sum)

# break : 반복문 빠져나옴, continue 반복문 맨처음 이동

# list while
li=[85,95,90,80,75]
# 점수 출력   함목개수 출력  점수합계 출력   점수평균 출력
print(li[0])
print(li[1])
print(li[2])
print(li[3])
print(li[4])
print("배열크기",len(li))
i=0
sum=0
while i<len(li):
    print(li[i])
    sum=sum+li[i]
    i=i+1
print(sum)
print(sum/len(li))

# for 변수 in 리스트(튜플, 문자열):
#   반복할 명령
li2=[85,95,90,80,75]
# li2 점수 출력   for  점수합
sum=0
for a in li2:
    sum=sum+a
    print(a)
print(sum)

a="hello"  # for 출력
for i in a:
    print(i)
a=(1,3,5,7,9)  # for 출력
for i in a:
    print(i)

a=['hello','안녕']
for i in a:
    print(i)
a=[(1,2),(3,4),(5,6)]
for i in a:
    print(i)
for (i,j) in a:
    print(i,j)

# 1~10
# range(시작번호,끝번호,증가값)
for i in range(1,11,1):
    print(i)

# 2단 출력
# 2*1=2
# 2*2=4
# ..
# 2*9=18

for i in range(1,10,1):
    print(2,"*",i,"=",2*i)
    print("%d*%d=%d" % (2,i,2*i))

# 2~9 단
for dan in range(2,10,1):
    for i in range(1,10,1):
        print(dan, "*", i, "=", dan * i)

# 한줄  for  if
# [실행문 for 변수 in 리스트 if 조건 ]

li=[1,2,3,4]
result=[]
#  for  li리스트에 값에 3을 곱해서 result리스트에 저장
# for i in range(0,len(li),1):
#     result.append(li[i]*3)
# print(result)

for i in li:
    result.append(i*3)
print(result)

# 한줄 for [실행문 for 변수 in 리스트]
# result=[실행문 for 변수 in 리스트]
result=[ i*3  for i in li ]
print(result)  #[3, 6, 9, 12]

# 한줄 for if [실행문 for 변수 in 리스트 if 조건]
li=[1,2,3,4]
result=[]
# li에 내용 중에 2의 배수를 구해서 i*3 => result
result=[ i*3 for i in li if i%2==0]
print(result)  #[6, 12]

# 한줄 for if for if [실행문 for 변수1 in 리스트1 if 조건1 for 변수 in 리스트2 if 조건2]
# 구구단 결과값  [2 4 6 .... 81]
result=[]


















