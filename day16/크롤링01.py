# pip install로 설치한 패키지 / 모듈
import requests
from bs4 import BeautifulSoup

# 타겟 인터넷주소(url)
url = "https://quotes.toscrape.com"

# requests로 통신.get(주소)
response = requests.get(url)
# HTML 전체 파일을 문자열로 가져온다.
# print(response.text)

# 가져온 HTML텍스트를 파이썬객체화 해줌
# 태그하나를 파이썬객체 하나로 바꿔 줌
soup = BeautifulSoup(response.text, "html.parser")


first_quote_tag = soup.find("div", class_="quote")  # soup(전체 html)에서 div 태그이면서, 클래스이름이 quote
quote_text_tag = first_quote_tag.find("span",class_="text")  # first_quote_tag 에서 span 태그이면서, 클래스값이 text 인 태그
quote_text = quote_text_tag.next # quote_text_tag가 가지고 있는 문자열 추출
print(quote_text)

# 도전! "Albert Einstein"을 추출해보세요
first_quote_tag = soup.find("div", class_="quote")
quote_text_tag = first_quote_tag.find("small", class_="author")  # first_quote_tag 안에서는 small태그가 단 한번 등장해서 바로 태그랑 클래스 이름 찾기 가능.
quote_text = quote_text_tag.text
print(quote_text)

# 강사님 답
author_tag = soup.find("small")
author_text = author_tag.text
print(author_text)

# find()로는 태그 하나만 가져올 수 있음
# 조건에 맞는 모든 태그를 가져오자 - find_all()
# -> [tag,tag,...tag]

# 총 10개 -> find_all()의 len()이 10이면 성공
# 10 아니라 14, 16... -> 조건을 좀 더 엄밀하게 할 필요 있음
all_quote_tags = soup.find_all("div", class_="quote")
result = len(all_quote_tags)
print(result)   # 10이 나오면 식별 성공!

for quote_tag in all_quote_tags:
    quote_text_tag = quote_tag.find("span", class_="text")
    text = quote_text_tag.text
    quote_author_tag = quote_tag.find("small", class_="author")
    author = quote_author_tag.text

    # <a href="이동할 주소경로"> 태그에 저장되어있는 href 속성 값
    author_link_tag = quote_tag.find("a")  # a 태그를 가지고 온 것임.
    # 태그.get("속성이름") -> 속성값을 가져옴.
    # 주소경로는 일반적으로 상대경로로 지정해놨음.
    link_url = author_link_tag.get("href")
    link_url = url + link_url

    # 도전!) 태그들의 택스트들을 추출해서 아래 tags에 추가해주세요
    tags = []
    # a태그가 div태그안에 여러개 존재 -> 안족 for 문
    a_tags = quote_tag.find_all("a", class_="tag")
    for a_tag in a_tags:
        tags.append(a_tag.text)

    # 컴프리헨션 사용 -> tags = [a_tag.text for a_tag in a_tags]
    print(f"{author}({link_url}): {text[:50]}...{tags}")
