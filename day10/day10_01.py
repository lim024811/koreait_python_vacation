# file 입출력
# 메모리(ram) - 실행도중에만 데이터 존재(칠판에 적었다가 지운다)
# 파일(HDD / SSD) - 반영구적으로 존재(노트에 적어서 보관)

file = open("./example.txt","w",encoding="utf-8")
file.write("Hello world!")
file.close()

# open(파일경로, 파일모드, 인코딩)
"""
- 경로( 절대경로, 상대경로 )
절대경로(드라이브부터 실제 파일 위치까지)
c:/koreait-python-vacation/day10/day10_01.py

상대경로(../, ./)
../: 현재 파일 위치에서 한 단계 위인 폴더
./: 현재파일이 속한 폴더

day10_01.py는 "./example.txt" 상대경로로 접근가능.
day10_01.py는 "../day09/함수심화.py" 상대경로로 접근가능.

- 파일모드
r: read
w: write

- 인코딩
컴퓨터는 숫자만 알아들음
글자들을 숫자로 바꿔줘야함
이때 필요한 규칙(인코딩)
ascii(영어만), eus-kr(옛), cp949(옛), utf-8(웹표준)
"""

# 파일 읽기
# open이 리턴을 해주는 건 실제 데이터가 아니라 특수한 자료형이다.
file = open("./example.txt","r",encoding="utf-8")
my_text = file.read()
file.close()  # 자료형 반납
print(my_text)


# day05에 있는 test.txt 파일을 읽어서 콘솔에 출력!
test_path = "../day05/test.txt.py"
test_file = open(test_path,"r",encoding="utf-8")
test_text = test_file.read()
print(test_text)

# day01폴더 안에 test 폴더 안에 test2.txt 읽고 출력!
test2_path = "../day01/test/test2.txt"
test2_file = open(test2_path,"r",encoding="utf-8")
test2_text = test2_file.read()
print(test2_text)
test2_file.close()  # 반납

with open(test_path,"r", encoding="utf-8") as test2_file:  # -> open한 파일을 test2_file에 담겠다.
     # with ~ as: 자동으로 자원 반납
    test2_text = test2_file.read()
    print(test2_text)

# 문자열(txt)말고, python 자료형들을 저장할 파일형식이 필요함.
# [{},{}...] 이런경우가 많다. -> 문자열로 저장할 수가 없음. list, dict처럼 인식하게 해줄 파일형식이 필요하다.
# 참고) csv, xml, yml -> 주고받는 용도로 쓰이는 애들
# JSON 파일 형식 - 웹, 소프트웨어에서 데이터를 주고받는 용도
"""
JSON 형식( dict 랑 똑같이 생김)
{"name": "홍길동", "age": 30, "is_student": false}
"""

dict_data = {"name": "홍길동", "age": 30, "is_student": False}
import json # 코드 빌려오기

with open("./data.json","w",encoding="utf-8") as f:
    # json.dump(파이썬데이터, f(파일), 아시키, 들여쓰기)
    # 아스키: 한글이 포함되면 무조건 False 로 지정
    # indent(들여쓰기): 4칸 들여쓰겠다.
    json.dump(dict_data,f, ensure_ascii=False, indent=4)

# json파일 불러오기
with open("./data2.json","r",encoding="utf-8") as f:
    new_dict_data = json.load(f)   # -> .load(): 파일을 찾아서 python 자료 형태로 만들어준다.
    print(new_dict_data)

# menu.json 에 메뉴가 존재합니다.
# 해당 메뉴를 불러와서 "떡볶이": 5000원 추가
# 라면가격을 5000원으로 인상하여
# 다시 menu.json으로 저장해주세요

with open("./menu.json","r",encoding="utf-8") as f:
    new_menu = json.load(f)
    new_menu["떡볶이"] = 5000
    new_menu["라면"] = 5000
    # menu.json 덮어쓰기
    with open("./menu.json","w",encoding="utf-8") as f:
        json.dump(new_menu,f,ensure_ascii=False,indent=2)

# 함수: 반복되는 코드 저장

# json 불러오기 함수
def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        json_data = json.load(f)
        return json_data

load_json("./menu.json")

# json 저장하기 함수
def save_json(path, data):
    with open(path,"w",encoding="utf-8") as f:
        json.dump(data,f,ensure_ascii=False,indent=2)

nums = [1,2,3,4,5]
save_json("./menu.json",nums)
print(load_json("./menu.json"))
