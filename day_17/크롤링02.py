import requests
from bs4 import BeautifulSoup

from day17.크롤링02 import top_ten_tag

url = "https://quotes.toscrape.com"

# HTTP 통신 - 요청/응답
response = requests.get(url)

# 파이썬 객체화
html = BeautifulSoup(response.text, "html.parser")  # 여기까지가 고정

# find로는 태그 하나만 가져올 수 있음
# 조건에 맞는 태그를 가져와보자(리스트) - find all()
# -> [tag1, tag2...]
all_quote_tags = html.find_all("div", class_="quote")
# 10이면 다 가져온 것, 14, 16 -> 조건을 더 엄밀하게
result = len(all_quote_tags)
print(result)

# 팁) 0번째 데이터 기준으로 로직을 작성해보자
for idx, quote_tag in enumerate(all_quote_tags):
    text_tag = quote_tag.find("span", class_="text")
    author_tag = quote_tag.find("small", class_="author")
    text = text_tag.text
    author = author_tag.text

    # 저자 url을 가져와보자 - 태그에 숨겨져있는 정보
    # <a href="상대경로 주소">
    author_link_tag = quote_tag.find("a") # 처음 발견한 a태그
    link_url = author_link_tag.get("href") # href 속성 값을 가져와
    # 상대경로를 절대경로로 변환
    link_url = url + link_url
    print(f"{idx + 1}: {author} - {text}")

# 도전!) 태그들의 텍스트들을 추출해서 아래 tags에 append해주세요
tags = []
# find_all(), for문 사용
# 1. a태그이면서 class 이름이 tag인 것 다 찾기
# 2. for문으로 a태그들의 텍스트만 추출하기
# 3. 추출해서 tags 리스트에 append하기
a_tags = quote_tag.find_all("a", class_="tag")
for a_tag in a_tags:
    tags.append(a_tag.text)

# 컴프리헨션으로 한 줄 작성 ok
tags = [a_tag.text for a_tag in a_tags]
print(f"연관 태그 - {tags}")

# select 방식
# CSS 선택자 방식 -> 브라우저가 태그 위치를 인식하는 방식
# .어쩌고 -> 저쩌고 클래스인 태그들 다 가져와
# 어쩌고 -> 어쩌고 태그들 다 가져와
# 어쩌고.저쩌고 -> 어쩌고 태그이면서 저쩌고 클래스 태그들
# #어쩌고 -> 어쩌고 id인 태그들
html.select(".quote") # quote 클래스인 태그들 다 가져와

# 한 번에 조건을 지정할 수 있음
# ".a .b"
# -> a클래스 태그 안쪽에 b클래스 태그들
author_tags = html.select(".quote .author")
for a_tag in author_tags:
    print(author_tag.text)

# 브라우저에 copy selector 기능
# 반복되는 태그에 copy selector를 하고 마지막 부분의 :nth-child(숫자)를 지운다
# body > div > div:nth-child(2) > div.col-md-4.tags-box > span > a
top_ten_tags = html.select("body > div > div:nth-child(2) > div.col-md-4.tags-box > span > a")
for tag in top_ten_tags:
    print(tag.text)

# copy selector 기능 사용하여서
# 명언들만 추출해주세요!
quote_tags = html.select("body > div > div:nth-child(2) > div.col-md-8 > div:nth-child(1) > span.text")
for tag in quote_tags:
    print(tag.text)