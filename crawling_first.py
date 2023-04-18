import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

baseUrl = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query="
plusUrl = input("블로그 검색어를 입력하세요:")
url = baseUrl + urllib.parse.quote_plus(plusUrl) # quote_plus 활용 > 한글을 웹 기준언어로 인코딩

html = urllib.request.urlopen(url).read() # urllib.request.urlopen을 통해 읽어서 html을 "전부" 가져온다.
soup = BeautifulSoup(html, "html.parser") # BeautifulSoup을 이용한 html 분석

title = soup.find_all(class_='api_txt_lines total_tit _cross_trigger') # 변수 지정을 통한 원하는 부분을 설정
contents = soup.find_all(class_='api_txt_lines dsc_txt') # 변수 지정을 통해 간략한 줄임글을 가져온다.

#제목을 찾고 출력
for idx, title in enumerate(title,start=1):
    print(f"{idx}, {title.get_text(strip=True)}")

# 본문을 찾고 출력
for idx, contents in enumerate(contents, start=1):
    print(f"{idx}, {contents.get_text(strip=True)}")
        