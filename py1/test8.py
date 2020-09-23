# test8.py
#  화면 입력 출력 print()  input()
# a=input("숫자입력하세요 :")
# print("입력한 수 : ",a)

#  파일 읽고 쓰기
# 파일 객체생성
# 변수=open("파일이름","모드")
# 모드  w 파일 내용을 쓸때  a 내용을 추가  r 파일 읽을때
# 멤버함수  변수.write()                 변수.readline() .readlines()  .read()

f=open("filetest.txt",'w')
data="안녕하세요"
f.write(data)
f.close()

#   D:\Shared\JSP\workspace_py5\py1
#   D:/Shared/JSP/workspace_py5/py1/filetest2.txt
# 1 번째 줄입니다.\n
# 2 번째 줄입니다.\n
# 3 번째 줄입니다.\n
# ..
# 10 번째 줄입니다.\n
f2=open("D:/Shared/JSP/workspace_py5/py1/filetest2.txt","w")
for i in range(1,11,1):
    data="%d 번째 줄입니다.\n" % i
    f2.write(data)
f2.close()

#  filetest2.txt  11~20 출력문 추가
f3=open("D:/Shared/JSP/workspace_py5/py1/filetest2.txt","a")
for i in range(11,21,1):
    data="%d 번째 줄입니다.\n" % i
    f3.write(data)
f3.close()

# f4=open("filetest2.txt","r")
# while True:
#     line=f4.readline()
#     if not line:
#         print(not line)
#         break
#     print(line)
# f4.close()

f5=open("filetest2.txt","r")
lines=f5.readlines()  #리스트형으로 결과 저장
for i in lines:
    print(i)
f5.close()

f6=open("filetest2.txt","r")
data=f6.read()
print(data)
f6.close()

# filetest2.txt 읽어서  역순으로 .reverse() 정렬   => filetest3.txt 출력
f7=open("filetest2.txt","r")
lines=f7.readlines()  #리스트형으로 결과 저장
f7.close()
lines.reverse()
print(lines)

f8=open("filetest3.txt","w")
for i in lines:
    f8.write(i)
f8.close()



