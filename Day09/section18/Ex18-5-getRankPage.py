import requests
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rpeople.nhn'
response = requests.get(url)
html = response.text

soap = BeautifulSoup(html, 'html.parser')
result_list = soap.find_all('td', class_='title')
movie_in = []
for result in result_list:
    movie_in.append(result.text.strip())

print(movie_in)

for person in movie_in:
    print(person)