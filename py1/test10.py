# test10.py
# 패키지 : 폴더 , 파이썬에서 파일을 계층적으로 관리  ,  .점으로 구분
# 폴더.폴더.파일이름
# 패키지.패키지.모듈

# import 패키지.패키지.모듈이름
# import 패키지.패키지.모듈이름  as 애칭
# echo파일 가져오기
import py1.py1_1.py1_1_1.echo
import py1.py1_1.py1_1_1.echo as e
# 함수 호출
py1.py1_1.py1_1_1.echo.echo_test()
e.echo_test()

# from 패키지.모듈이름 import 함수이름
from py1.py1_1.py1_1_1.echo import echo_test
echo_test()

# test9 모듈에  safe_sum 호출
import py1.test9
print(py1.test9.safe_sum(10,20))
import py1.test9 as t
print(t.safe_sum(1,2))
from py1.test9 import sum,safe_sum
print(safe_sum(5,10))

# 내장함수 : import 없이 사용
# 외장함수 : import 사용
# random()
import random
print(random.random())
print(random.randint(1,10))

# webbrowser
import webbrowser
webbrowser.open("www.naver.com")



