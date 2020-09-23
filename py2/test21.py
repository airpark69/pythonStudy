# test21.py

# numpy패키지 설치
# 파이썬에서 과학연산(배열) 쉽고 빠르게 하는 패키지
# 다차원 배열을 효과적으로 관리
# www.numpy.org

import numpy as np
# 리스트 생성
data1=[0,1,2,3,4,5]
# numpy 배열
a1=np.array(data1)
print(a1)
print(a1.dtype)  # int32

a2=np.array([0.5,2,0.01,8])
print(a2)
print(a2.dtype)  # float64

a3=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(a3)

a4=np.arange(0,11,2)
print(a4)

a5=np.arange(5)   #arange(0,5,1)
print(a5)  #[0 1 2 3 4]

# 차원 변경가능
a6=np.arange(12).reshape(4,3)
print(a6)
print(a6.shape)  #(4, 3)

# 1~10까지 10개 일정한 간격으로 데이터 만듬
a7=np.linspace(1,10,10)
print(a7)  #[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
# 배열 0으로 10개 만듬
a8=np.zeros(10)
print(a8)  #[0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
# 배열 1로   5개 만듬
a9=np.ones(5)
print(a9)  #[1. 1. 1. 1. 1.]

#타입변환  문자 => float
str_a1=np.array(['1.567','5.123','9','8'])
num_a1=str_a1.astype(float)
print(num_a1)  # [1.567 5.123 9.    8.   ]

# 난수발생
ran_a1=np.random.randint(10,size=(3,4))
print(ran_a1)
# [[9 9 9 7]
#  [0 2 8 7]
#  [8 4 6 5]]

# 배열 연산
arr1=np.array([10,20,30,40])
arr2=np.array([1,2,3,4])
print(arr1+arr2)  #[11 22 33 44]
print(arr1>20)  #[False False  True  True]

# 통계 연산
arr3=np.arange(5)
print(arr3)  #[0 1 2 3 4]
print(arr3.sum())  #10
print(arr3.mean())
print(arr3.min())
print(arr3.max())
print(arr3.std())
print(arr3.var())

