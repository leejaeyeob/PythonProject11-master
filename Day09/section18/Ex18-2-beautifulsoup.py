'''
https / http - Hyper Text Transfer Protocol 웹서버 접속
ftp - 파일 서버 접속
mailto - 전자 메일 서버 접속
tlanet - 원격자 접속
프로토콜 : 통신규약

호스트 주소(Host) - 웹페이지를 요청할 서버의 이름
    ex) movie.naver.com

경로(path) - 웹서버에서 차원에 대한 경로 (물리적 또는 추상적 경로)
    ex)/movie/bi/mi/basic.nhn

쿼리(query) - 추가로 서버에 보내는 파라미터
    ex) code=10016
    
'''
import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/bi/mi/basic.nhn?code=10016'
param = {'code': 10016}
response = requests.get(url, params=param)
html = response.text

soup = BeautifulSoup(html, 'html.parser')

review_list = soup.find_all('div', class_='score_reple')

for review in review_list:
    print(review.find('p').text.strip())
