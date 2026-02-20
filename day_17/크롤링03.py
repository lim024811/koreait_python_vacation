import requests
from bs4 import BeautifulSoup
import time

# 여러 페이지 크롤링 - 페이지 url 패턴 파악
# https://quotes.toscrape.com/page/{페이지 숫자}/
# https://quotes.toscrape.com/page/3/
total_page = 10
for page in range(1, total_page + 1):
    url = f"https://quotes.toscrape.com/page/{page}/"
    print(f"현재 크롤링 주소: {url}")
    response = requests.get(url)
    html = BeautifulSoup(response.text, "html.parser")

    divs = html.select("body > div > div:nth-child(2) > div.col-md-8 > div")
    for div in divs:
        text = div.find("span", class_="text").text
        author = div.find("small", class_="author").text
        print(f"{author}: {text}")

    print(f"현재 페이지: {page}페이지 완료")
    time.sleep(1) # 1초 정지(너무 빠르면 공격으로 간주됨)

