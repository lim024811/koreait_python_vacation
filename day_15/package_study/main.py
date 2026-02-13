# main.py
# 모듈: .py 파일, 일반적으로 함수 or 클래스 정의만 존재
# 패키지: 모듈을 묶어놓는 폴더
# __init__.py는 해당 폴더를 파이썬이 패키지로 인식하게끔

# random.py 파일의 코드를 복붙한 것
import random

# a패키지에 있는 a.py 코드 복붙
import a.a
# from을 사용해서 표현 가능
from a import a
from b import b
# 함수나 클래스만 가져오기 / as로 별명
from a.a import add as 더하기함수
from b.b import Person as 사람

# b.py에 Person class 정의
# name, age 필드 가집니다
# def print_me(self): 이름과 나이 출력
# main에서 import하여 객체 생성
# print.me 호출!

if __name__ == "__main__":
    p1 = 사람("John",20)
    p1.print_me()


