# # 현재시간을 다루는 모듈
#
# from datetime import datetime, timedelta
#
# # 현재시간
# now = datetime.now()
# print(f"지금: {now}")  # now는 datetime의 객체 (클래스로부터 만들어진 객체상태임.)
#
# # datetime 객체 -> 내가 원하는 문자열 포맷
# # %Y: 년 / %m: 월 / %d: 일 / %H: 시 / %M: 분
# my_time = now.strftime("%Y년도 %m월 %d일 %H시 %M분") # strftime() -> 타임을 포맷한 문자열로 만들어 주겠다
# print(my_time)
#
# # 날짜 덧셈/뺄셈
# # 현재시간 + 1일
# tomorrow = now + timedelta(days=1)
# # 현재시간 - 1일
# yesterday = now - timedelta(days=1)

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# 셀레니움 쓸려면 위 네가지 필요
from time import sleep
import openpyxl
from datetime import datetime


url = "https://www.naver.com"

# 파이썬이 내pc를 사용해서 브라우저를 열고 행동

# 크롬 설치파일 가져오기
driver_manager = ChromeDriverManager().install()
# 셀레니움에 설치
chrome_service = Service(driver_manager)
# 인터넷창(브라우저) 생성
driver = webdriver.Chrome(service=chrome_service)
def scroll_to(tag):
    script = "arguments[0].scrollIntoView();"
    driver.execute_script(script, tag)

# 여기까지가 밑작업
######################################################
# 시작
print("네이버 웹툰 크롤링을 시작합니다. ")

driver.get(url)  # 네이버 접속
sleep(1) # 로딩 대기

# a태그 - 링크 가지고 있음(href속성에 가지고 있음)
webtoon_home_link = driver.find_element(By.CSS_SELECTOR,"#shortcutArea > ul > li:nth-child(9) > a")
# href 속성값 가져오기
webtoon_home_url = webtoon_home_link.get_attribute("href")  # href 속성을 가진 것을 가져온다.

# 클릭했을때 새페이지() -새탭> get() 이동추천
# 클릭했을때 같은페이지 -> click() 이동추천
driver.get(webtoon_home_url)  # 웹툰홈으로 이동
sleep(0.5)

# 도전! 웹툰 메뉴 클릭
webtoon_home_menu = driver.find_element(By.CSS_SELECTOR,"#menu > li:nth-child(2) > a")
webtoon_home_menu.click()
sleep(2)

# 월~일 순서대로 클릭
# 메뉴바 -> 각 메뉴 추출
menu_bar = driver.find_element(By.CSS_SELECTOR,"#wrap > header > div.SubNavigationBar__snb_wrap--A5gfM > nav > ul")
# find_elements -> [태그1,태그2...태그n]
menus = menu_bar.find_elements(By.CSS_SELECTOR,"li a")  # li태그안에 a태그
# [요일전체, 월, 화...일, 매일+, 신작, 완결] -> [월~일] 슬라이싱
menus = menus[1:8]

webtoon_list = []
"""
[
    {
        "day_of_week": "월",
        "webtoon_items": [
            {
                "title": "환생천마",
                "author": "장영훈",
                "img_url": "~~~~",
                "rating": 9.89
            }
            ]
    },
    {
        "day_of_week": "화",
        "webtoon_items": []
    }
]

"""
for idx, menu in enumerate(menus):
    menu.click()
    sleep(1)
    # 각 요일별 웹툰 크롤링
    # 해당 요일 데이터 저장용 dict
    webtoon_dict = {
        "day_of_week": menu.text,
        "webtoon_items": []  # 웹툰하나당 {}하나 넣자
    }
    # 해당 요일 웹툰들 찾기
    # [웹툰태그1, 웹툰태그2...]
    webtoon_items = driver.find_elements(By.CSS_SELECTOR,"#content > div:nth-child(1) > ul > li")
    for webtoon_item in webtoon_items:
        try:
            scroll_to(webtoon_item)  # 스크롤
            sleep(0.2)

            # 데이터 들고 와서 아래의 4개 추출하여 {}로 포장 -> webtoon_dict["webtoon_items"].append()
            # 이미지, 제목, 작가, 평점

            # 이미지
            webtoon_item_img = webtoon_item.find_element(By.TAG_NAME,"img")
            img_url = webtoon_item_img.get_attribute("src")  # src라는 url을 가져와라
            # 제목 (#content > div:nth-child(1) > ul > li:nth-child(1) > div > a)
            webtoon_item_title = webtoon_item.find_element(By.CSS_SELECTOR,"div > a")  # 우리가 이미 ~~li까지 찾아왔으니 거기서 제목을 찾는 경로만 추가해주면 된다.
            title = webtoon_item_title.text
            # 작가 (class="ContentAuthor__author--CTAAP") -> 클래스 name으로 찾아가기
            webtoon_item_author = webtoon_item.find_element(By.CLASS_NAME,"ContentAuthor__author--CTAAP")
            author = webtoon_item_author.text
            # 평점
            webtoon_item_rating = webtoon_item.find_element(By.CLASS_NAME,"Rating__star_area--dFzsb")
            rating = webtoon_item_rating.text[2:].strip()
            print(f"제목: {title}")
            print(f"작가: {author}")
            print(f"평점: {rating}")
            print(f"이미지주소: {img_url}")

            # dict 포장
            webtoon_item_dict = {
                "img_url": img_url,
                "title": title,
                "author": author,
                "rating": rating
            }
            # 해당 요일 리스트 추가
            webtoon_dict["webtoon_items"].append(webtoon_item_dict)
            sleep(0.1)
        except Exception as e:
            print(f"에러처리: {e}")
            continue
    # 요일별로 모은 webtoon_dict를 전체 리스트에 추가
    webtoon_list.append(webtoon_dict)

driver.quit()
##### 크롤링완료 #####

##### 엑셀로 저장 #####
wb = openpyxl.Workbook()

for webtoon_dict in webtoon_list:
    # 요일 꺼내기
    day_of_week = webtoon_dict["day_of_week"]
    # 해당요일 웹툰들 꺼내기
    webtoon_items = webtoon_dict["webtoon_items"]

    # 해당 요일 엑셀 시트 생성
    new_ws = wb.create_sheet(f"{day_of_week}요일")

    # 헤더 추가
    new_ws.append(["제목","작가","평점","이미지 URL"])

    for webtoon_item in webtoon_items:
        title = webtoon_item["title"]
        author = webtoon_item["author"]
        rating = webtoon_item["rating"]
        img_url = webtoon_item["img_url"]
        엑셀한줄 = [title,author,rating,img_url]
        new_ws.appned(엑셀한줄)  # 웹툰하나가 엑셀 한 줄이 되는 것임.

    print(f"{day_of_week}요일 엑셀 작업 끝")

# 파일명 생성
time_stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"네이버웹툰크롤링_{time_stamp}.xlsx"
wb.save(filename)

print("엑셀파일저장완료!")

# 강사님 코드!
# https://github.com/elikese/koreait-python-vacation