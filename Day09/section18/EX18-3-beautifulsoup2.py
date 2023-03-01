import requests
from bs4 import BeautifulSoup

url = 'https://news.naver.com/main/ranking/popularDay.naver'
headers = {}
response = requests.get(url, headers=headers)
html = response.text
soup = BeautifulSoup(html, 'html.parser')

review_list = soup.find_all('div', class_='list_content')

news_in = []
for result in result_list:
    news_in.append(result.text.strip())

print(news_in)

for rank in news_in:
    print(rank)
