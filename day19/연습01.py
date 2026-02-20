from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
# 셀레니움 쓸려면 위 네가지 필요
from time import sleep

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

# # 네이버에 접속해서 "부산날씨" 검색
# search_n = "부산날씨"
# driver.get(url)
# sleep(2)
#
# search_input = driver.find_element(By.CSS_SELECTOR, "#query")
# search_input.send_keys(search_n)
# sleep(0.5)
# search_btn = driver.find_element(By.CLASS_NAME, "btn_search")
# # search_btn = driver.find_element(By.CSS_SELECTOR, "#sform > fieldset > button") -> copy selector로 찾기
# search_btn.click()
# sleep(3)


# local_list에 있는 지역온도를 셀리니움으로
# 네이버에 검색하여서 출력해 주세요.
local_list = ["부산","대구","대전","인천","서울","광주","울산"]
for local_n in local_list:
    driver.get(url)
    sleep(2)

    search_input = driver.find_element(By.CSS_SELECTOR, "#query")
    search_input.send_keys(f"{local_n} 날씨")
    sleep(0.5)

    search_btn = driver.find_element(By.CLASS_NAME, "btn_search")
    # search_btn = driver.find_element(By.CSS_SELECTOR, "#sform > fieldset > button") -> copy selector로 찾기
    search_btn.click()
    sleep(3)

    tem_tag = driver.find_element(By.CLASS_NAME, "temperature_text")
    scroll_to(tem_tag)
    print(f"{local_n}: {tem_tag.text}")

