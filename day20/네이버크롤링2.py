from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

from day20.네이버웹툰 import webtoon_home_url, menu, webtoon_dict, img_url

url = "https://www.naver.com"

# 파이썬이 내 pc를 사용해서 브라우저를 열고 행동
# 크롬 설치파일 가져오기
driver_manager = ChromeDriverManager().install()
# 셀레니움에 설치
chrome_service = Service(driver_manager)
# 인터넷 창(브라우저) 생성
driver = webdriver.Chrome(service=chrome_service)

def scroll_to(tag):
    script = "arguments[0].scrollIntoView();"
    driver.execute_script(script, tag)

driver.get(url) # 접속
sleep(1.5)

# a태그 - 링크를 가지고 있음
webtoon_home_link = driver.find_element(By.CSS_SELECTOR, "#shortcutArea > ul > li:nth-child(9) > a")
# 새 창이 열리는 경우에는 get()으로 이동하는 게 수월하다
# 같은 페이지에서 이동 -> click()
webtoon_home_url = webtoon_home_link.get_attribute("href")
driver.get(webtoon_home_url) # 재이동
sleep(1.5)


driver.get(webtoon_home_url) # 재이동
sleep(1.5)

webtoon_menu = driver.find_element(By.CSS_SELECTOR, "#menu > li:nth-child(2) > a")
webtoon_menu.click()
sleep(1.5)


# 월 ~ 일 순서대로 클릭
# 메뉴바 추출
menu_bar = driver.find_element(By.CSS_SELECTOR, "#wrap > header > div.SubNavigationBar__snb_wrap--A5gfM > nav > ul")

# menu_bar태그에 속해있는 "li > a"들을 찾아야함
menus = menu.bar.find_elements(By.CSS_SELECTOR, "li > a")
menus = menus[1:8] # 월 ~ 일 필터링


"""
[
    {
        "day_of_week": "월"
        "webtoon_items": [{},{},...{}]
    },
    {},
    ...
    {} 요일 하나당 dict 하나
] 전체를 저장하는 list


"""

webtoon_list = [] # 전체를 저장하는 list
for menu in menus:
    menu.click() # 월~일 탭 페이지 이동
    sleep(1.5)

    webtoon_dict = {
        "day_of_week": menu.text,
        "webtoon_items": [] # 웹툰 하나당 {} 하나 넣을거임!


    }

    webtoon_items = driver.find_elements(By.CSS_SELECTOR, "#content > div:nth-child(1) > ul > li")
    print(len(webtoon_items))
    # #content > div:nth-child(1) > ul > li 풀 정보/(:nth-child(10))
    for item in webtoon_items:
        scroll_to(item) # 스크롤

        # 제목 추출
        title = item.find_element(By.CLASS_NAME, "ContentTitle__title--e3qXt").text
        # 작가
        author = item.find_element(By.CLASS_NAME, "ContentAuthor__author--CTAAP").text
        # 별점
        rating = item.find_element(By.CLASS_NAME, "rating_area").text
        rating = rating[2:].strip()
        # 썸네일 - img 태그를 찾아라
        img_url = item.find_element(By.CLASS_NAME, "Poster__image--d9XTI").get_attribute("src")


        print(f"제목: {title}")
        print(f"작가: {author}")
        print(f"평점: {rating}")
        print(f"이미지 url: {img_url}")

        webtoon_dict["webtoon_items"].append({
            "title": title,
            "author": author,
            "rating": rating,
            "img_url": img_url
        })
        sleep(0.1)

    # 해당 요일에서 모은 웹툰들을 저장한 webtoon_dict를 전체 리스트에 추가
    count = len(webtoon_dict["webtoon_items"])
    print(f"{menu.text}요일: {count}건 크롤링 완료")
    webtoon_list.append(webtoon_dict)

driver.quit()
######### 크롤링 완료 #########

#### 엑셀 저장 ####
from openpyxl import Workbook

# 엑셀 파일 생성
wb = Workbook()

for webtoon_dict in webtoon_list:
    # 요일
    day_of_week = webtoon_dict["day_of_week"]
    # 해당 요일 웹툰들
    items = webtoon_dict["webtoon_items"]

    # 해당 요일 시트생성
    new_ws = wb.create_sheet(f"{day_of_week}요일")
    # 헤더 추가
    new_ws.append(["제목", "작가", "평점", "썸네일URL"])

    for item in items:
        title = item["title"]
        author = item["author"]
        rating = item["rating"]
        img_url = item["img_url"]

        line = [title, author, rating, img_url]
        new_ws.append(line)

    print(f"{len(items)}개 작성하였습니다")
    print(f"{day_of_week}요일 엑셀 작업 완료")

# 파일명
from datetime import datetime # 시계 모듈
# 현재시간을 문자열로 가져옴
now = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"네이버웹툰크롤링_{now}.xlsx"
wb.save(f"./{filename}")

print("엑셀 파일 저장 완료!")
