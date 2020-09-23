# test22.py
# https://pandas.pydata.org/
# pandas : numpy 기반 만들어져 있음, 복잡한 데이터 분석
# dataframe기반 => 엑셀 table , 2차원배열(리스트), 행,열  DB table

import pandas as pd

# Series 데이터 생성 1차원배열
s1=pd.Series([10,20,30,40,50])
print(s1)
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64
# index번호 values값
print(s1.index)  #RangeIndex(start=0, stop=5, step=1)
print(s1.values)  #[10 20 30 40 50]

s2=pd.Series(['a','b','c',1,2,3])
print(s2)

# 0    a
# 1    b
# 2    c
# 3    1
# 4    2
# 5    3
# dtype: object

import numpy as np
# np.nan => NaN 데이터 없다
s3=pd.Series([np.nan,10,30])
print(s3)
# 0     NaN
# 1    10.0
# 2    30.0
# dtype: float64
index_date=['2020-08-01','2020-08-02','2020-08-03','2020-08-04']
s4=pd.Series([100,195,np.nan,205],index=index_date)
print(s4)
# 2020-08-01    100.0
# 2020-08-02    195.0
# 2020-08-03      NaN
# 2020-08-04    205.0
# dtype: float64
s5=pd.Series({'국어':100,'영어':95,'수학':90})
print(s5)
# 국어    100
# 영어     95
# 수학     90
# dtype: int64

#날짜 생성
s6=pd.date_range(start='2020-08-01',end='2020-08-07',periods=None,freq='D')
print(s6)
# DatetimeIndex(['2020-08-01', '2020-08-02', '2020-08-03', '2020-08-04',
#                '2020-08-05', '2020-08-06', '2020-08-07'],
#               dtype='datetime64[ns]', freq='D')
s7=pd.date_range(start='2020-08-01',periods=4,freq='D')
print(s7)
# DatetimeIndex(['2020-08-01', '2020-08-02', '2020-08-03', '2020-08-04'], dtype='datetime64[ns]', freq='D')

# DataFrame 2차원 데이터 생성
index_date=pd.date_range('2020-08-01',periods=3) # 2020-08-01  3개
columns_list=['A','B','C']
df1=pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]],index= index_date,columns=columns_list )
print(df1)
print(df1.index)  #DatetimeIndex(['2020-08-01', '2020-08-02', '2020-08-03'], dtype='datetime64[ns]', freq='D')
print(df1.columns) #Index(['A', 'B', 'C'], dtype='object')
print(df1.values)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]
# index  columns
#    0  1  2
# 0  1  2  3
# 1  4  5  6
# 2  7  8  9
#             A  B  C
# 2020-08-01  1  2  3
# 2020-08-02  4  5  6
# 2020-08-03  7  8  9

# s5=pd.Series({'국어':100,'영어':95,'수학':90})
df2=pd.DataFrame({'연도':[2015,2016,2017],
                '지사':['한국','미국','한국'],
                '고객수':[200,450,300]})
print(df2)

#        봄      여름     가을    겨울
# 2012   256.5   356.5   256.5   156.5
# 2013   264.3   364.3   264.3   164.3
# 2014   215.9   315.9   215.9   115.9
# 2015   223.2   323.2   223.2   123.2
# 2016   312.8   312.8   312.8   112.8

index_date=[2012,2013,2014,2015,2016]
df3=pd.DataFrame({'봄':[256.5,264.3,215.9,223.2,312.8],
                '여름':[356.5,364.3,315.9,323.2,312.8],
                '가을':[256.5,264.3,215.9,223.2,312.8],
                '겨울': [156.5,164.3,115.9,123.2,112.8] },index=index_date)
print(df3)

# 데이터 총합, 평균, 표준편차
print(df1)
print(df1.sum())
# A    12
# B    15
# C    18
# dtype: int64
print(df1.sum(axis=1))
# 2020-08-01     6
# 2020-08-02    15
# 2020-08-03    24
# Freq: D, dtype: int64
print(df1.mean())
print(df1.mean(axis=1))
print(df1.std())
print(df1.std(axis=1))
print(df1.describe())
print(df2.describe())
print(df3.describe())

# 상위  하위 몇개 가져오기
print(df3.head(3))
print(df3.tail(3))
print(df3['봄'])
print(df3[0:2])
print(df3['봄'][0:2])
print(df3[0:2]['봄'])
print(df3.loc[2012])
print(df3.loc[2012:2014])
print(df3.loc[2012:2014]['봄'])
print(df3['봄'].loc[2012:2014])

print(df3)
print(df3.T) # 전치행렬(행,열바꿈)

# 열추가
df3['sum_0']=0
print(df3)
df3['sum']=df3['봄']+df3['여름']+df3['가을']+df3['겨울']
print(df3)
# 'avg' 열추가
df3['avg']=df3['sum']/4
print(df3)

# 열 삭제
df3_1=df3.drop('sum_0',axis=1)
print(df3_1)

# 조건 데이터 추출
# print(df3[조건식])
print(df3[df3['봄']>=300])
# 여름 강수량  350 작은 경우
print(df3[df3['여름']<350])
print(df3[df3['여름']<350]['여름'])
print(df3[df3['여름']<350][['봄','여름']])

# 정렬
print(df3)
print(df3.sort_values(by=['봄']))  #봄 오름차순
print(df3.sort_values(by=['봄'],ascending=False))  #봄 내림차순

# min max sum count mean
print(df3.min())
print(df3.max())
print(df3.sum())
print(df3.count())
print(df3.mean())

# 그룹  groupby()
print(df2)
df2_group=df2.groupby(by='지사').count()
print(df2_group)

df2_group=df2.groupby(by='지사').mean()
print(df2_group)

df2_group=df2.groupby(by='지사')['고객수'].mean()
print(df2_group)

df2_group=df2.groupby(by='지사')['고객수'].agg([min,max])
print(df2_group)

# '연도' count  '고객수' sum
agg_format={'연도':'count','고객수':'sum'}
df2_group=df2.groupby(by='지사').agg(agg_format)
print(df2_group)

# 파일 읽고 쓰기
# DataFrame => 파일로 만들기
df1.index.name='년도'
print(df1)
df1.to_csv('df1.csv')
# df2  df3  => csv 파일 만들기
df2.to_csv('df2.csv')
df3.to_csv('df3.csv')

# 파일 읽어오기
# 한글이 포함된 파일 encoding='cp949'
fdf1=pd.read_csv('height.csv', encoding='cp949')
print(fdf1)
# nation  index지정
fdf2=pd.read_csv('height.csv',index_col="nation")
print(fdf2)
print(fdf2.mean())

# 두frame 데이터 통합  행추가  열추가  병합
df4=pd.DataFrame({'1반':[95,92,98,100],
                  '2반':[91,93,97,99]})
print(df4)

df5=pd.DataFrame({'1반':[87,89],
                  '2반':[85,90]})
print(df5)
# frame 추가 append
print(df4.append(df5))

#     1반  2반
# 0   95  91
# 1   92  93
# 2   98  97
# 3  100  99
# 0   87  85
# 1   89  90
# frame 추가 append
print(df4.append(df5,ignore_index=True))
#     1반  2반
# 0   95  91
# 1   92  93
# 2   98  97
# 3  100  99
# 4   87  85
# 5   89  90

# frame 컬럼(열) 추가  join()
df6=pd.DataFrame({'3반':[90,96,88,80]})
print(df4.join(df6))
#     1반  2반  3반
# 0   95  91  90
# 1   92  93  96
# 2   98  97  88
# 3  100  99  80

# frame 열기준 통합 (병합) merge
df7=pd.DataFrame({'과목':['국어','영어','수학','과학'],
                  '1반':[95,92,98,100],
                  '2반':[91,93,97,99]
                  })

df8=pd.DataFrame({'과목':['음악','미술','수학','과학'],
                  '3반':[90,96,88,80],
                  '4반':[95,90,80,80]})
print(df7)
#    과목   1반  2반
# 0  국어   95  91
# 1  영어   92  93
# 2  수학   98  97
# 3  과학  100  99
print(df8)
#  과목  3반  4반
# 0  음악  90  95
# 1  미술  96  90
# 2  수학  88  80
# 3  과학  80  80
print(df7.merge(df8))
print(df7.merge(df8,how='inner'))
#    과목   1반  2반  3반  4반
# 0  수학   98  97  88  80
# 1  과학  100  99  80  80
print(df7.merge(df8,how='left'))
#    과목   1반  2반    3반    4반
# 0  국어   95  91   NaN   NaN
# 1  영어   92  93   NaN   NaN
# 2  수학   98  97  88.0  80.0
# 3  과학  100  99  80.0  80.0
print(df7.merge(df8,how='right'))
#    과목     1반    2반  3반  4반
# 0  음악    NaN   NaN  90  95
# 1  미술    NaN   NaN  96  90
# 2  수학   98.0  97.0  88  80
# 3  과학  100.0  99.0  80  80
print(df7.merge(df8,how='outer'))
# 과목     1반    2반    3반    4반
# 0  국어   95.0  91.0   NaN   NaN
# 1  영어   92.0  93.0   NaN   NaN
# 2  수학   98.0  97.0  88.0  80.0
# 3  과학  100.0  99.0  80.0  80.0
# 4  음악    NaN   NaN  90.0  95.0
# 5  미술    NaN   NaN  96.0  90.0
# 이상한 데이터 9999 => NaN 변경
# 결손데이터 (비어있는 데이터 처리)  NaN  => 0, 평균값 대치
mdf=df7.merge(df8,how='outer')
print(mdf)
print(mdf.isna().sum())
# NaN  => 0, 평균값 대치
print(mdf['2반'].fillna(0))
# 0    91.0
# 1    93.0
# 2    97.0
# 3    99.0
# 4     0.0
# 5     0.0
print(mdf['2반'].fillna(mdf['2반'].mean()))  #95.0
# 0    91.0
# 1    93.0
# 2    97.0
# 3    99.0
# 4    95.0
# 5    95.0

# 람다함수이용  열 추가  apply()
print(mdf)
# '1반100'  1반열 *100
mdf['1반100']=mdf['1반'].apply(lambda x:x*100)
print(mdf)
# '1반grade'     1반열>=95 'A' else 'B'  람다 매개변수 : 참값 if 조건 else 거짓값
mdf['1반grade']=mdf['1반'].apply(lambda x: 'A' if x>=95 else 'B')
print(mdf)
# 과목     1반    2반    3반    4반    1반100 1반grade
# 0  국어   95.0  91.0   NaN   NaN   9500.0       A
# 1  영어   92.0  93.0   NaN   NaN   9200.0       B
# 2  수학   98.0  97.0  88.0  80.0   9800.0       A
# 3  과학  100.0  99.0  80.0  80.0  10000.0       A
# 4  음악    NaN   NaN  90.0  95.0      NaN       B
# 5  미술    NaN   NaN  96.0  90.0      NaN       B

# train.csv 가져오기
train_df=pd.read_csv('train.csv')
print(train_df)
# 상위 5개 출력
print(train_df.head())
# 하위 5개 출력
print(train_df.tail())
# 개수 출력
print(train_df.count())

# 추출  'Pclass' 3등석  상위 3개 출력
print(train_df[train_df['Pclass']==3].head(3))
# 추출 'Age' 60보다 큰 데이터 상위 3개 출력
print(train_df[train_df['Age']>60].head(3))
# 추출 'Age' 60보다 큰 데이터중 'Name','Age' 상위 3개출력
print(train_df[train_df['Age']>60][['Name','Age']].head(3))

# 정렬
train_df_sorted=train_df.sort_values(by=['Name'])
print(train_df_sorted.head(3))

# 그룹
# 'Pclass' 기준으로  그룹  개수
train_df_groupby1=train_df.groupby(by='Pclass').count()
print(train_df_groupby1)
# 'Pclass' 기준으로 그룹  'Survived'  합계
train_df_groupby2=train_df.groupby(by='Pclass')['Survived'].agg([sum])
print(train_df_groupby2)
# 'Pclass' 기준으로 그룹  'Age'  최대값, 최소값
train_df_groupby3=train_df.groupby(by='Pclass')['Age'].agg([max,min])
print(train_df_groupby3)
# 'Pclass' 기준으로 그룹   'Age'  최대값, 'Fare' 평균
agg_format={'Age':'max','Fare':'mean'}
train_df_groupby4=train_df.groupby(by='Pclass').agg(agg_format)
print(train_df_groupby4)
# 'Sex' 기준으로 그룹   'Age' 평균, 'Survived' 합계
agg_format={'Age':'mean','Survived':'sum'}
train_df_groupby5=train_df.groupby(by='Sex').agg(agg_format)
print(train_df_groupby5)

# 열추가
train_df['age_10']=train_df['Age']*10
print(train_df)


