# test24.py
# html => 데이터 수집
# xml , json, ... 데이터 수집  
# xls, csv, xml, json 통계데이터 

# 웹 스크래핑
# 패키지 설치  requests, BeautifulSoup4, lxml 설치

import requests
from bs4 import BeautifulSoup

r=requests.get("https://www.google.co.kr").text
# print(r)

soup=BeautifulSoup(r,'lxml')
# 태그 내용을 찾기 함수  find() find_all() select_one() select()
# print(soup.find('a'))
# print(soup.find('a').get_text())
# print(soup.find_all('a')) # 전체 리스트
site=soup.find_all('a')
# for i in site:
    # print(i)
    # print(i.get_text())

# print(soup.title)
# print(soup.body.img)
# img 태그 찾아서 => 리스트 저장
fimg=soup.find_all('img')
# for  출력
# for i in fimg:
#     print(i)

fimg2=soup.select('body img')
# for i in fimg2:
#     print(i)

# https://news.naver.com/    'a' 가져와서 출력
r=requests.get("https://news.naver.com/").text
soup=BeautifulSoup(r,'lxml')
# ali=soup.find_all('a')
# for i in ali:
#     print(ali)

#  select()  헤드라인 뉴스beta   ul class="hdline_article_list"  a
ali2=soup.select('ul.hdline_article_list a')
# for i in ali2:
#     # print(i)
#     print(i.get_text())
#     print(i.string)
#     print(i.attrs['href'])

# https://www.alexa.com/topsites    select(p a)    site
r=requests.get("https://www.alexa.com/topsites").text
soup=BeautifulSoup(r,'lxml')

li=soup.select('p a')
print(len(li))
# for i in li:
#     print(i)

# for i in range(1,11,1):
#     print(i,li[i])

# 기상청 전국날씨  xml 데이터 제공  => 파일로 저장
# http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108
import  os.path
import random
import urllib.request as req
# xml데이터 다운로드
url="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
savename="forecast.xml"
if not os.path.exists(savename):
    req.urlretrieve(url,savename)

xml=open(savename,'r',encoding="utf-8").read()
soup=BeautifulSoup(xml,"html.parser")
# print(xml)
#  find_all()  'location'
#  for  find() 'city' 'wf'
li=soup.find_all('location')
# for i in li:
#     print(i.find('city').string)
#     print(i.find('wf').string)

# JSON
# http://api.github.com/repositories
url="http://api.github.com/repositories"
savename="repo.json"
if not os.path.exists(savename):
    req.urlretrieve(url,savename)

# json파일 분석하기
import  json
items=json.load(open(savename,'r',encoding='utf-8'))
# print(items)
 # 출력 for
for i in items:
    print(i['name']+" : "+i['owner']['login'])


# 웹API 데이터 추출
# 날씨, 상품, 주가, 환율  => 웹API제공
# 웹API : 사이트가 가지고 있는 기능을 외부에서도 쉽게 사용 할수 있게 공개
# 사이트 웹API 요청 => XML,JSON

# 옥션,지마켓,아마존,.. 크롤링 => 웹API제공 서버 부하 감소

# OpenWeatherMap 날씨 정보 제공
# https://openweathermap.org
# 회원가입 => API keys

# API키
apikey="474d59dd890c4108f62f192e0c6fce01"
#날씨확인 도시 지정
cities=["Seoul,KR","Tokyo,JP","New York,US"]
#api주소
api="http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={key}"
for i in cities:
    # print(i)
    url=api.format(city=i,key=apikey)
    r=requests.get(url)
    data=json.loads(r.text)
    # print(data)
    print(data['name'])
    # data 'weather' [0] 'description'
    print(data['weather'][0]['description'])

# http://kosis.kr/index/index.do
# http://data.go.kr
# https://data.oecd.org/waste/municipal-waste.htm

# http://data.seoul.go.kr
# http://data.ex.co.kr
# http://taas.koroad.or.kr
# https://data.kma.go.kr/cmmn/main.do
# http://www.kofic.or.kr/kofic/business/main/main.do