# 모듈: .py파일, 보통은 함수 or 클래스 정의만 있음 ( 정의만 있으면 실행했을때 결과가 안나옴 )
# 패키지: 모듈들을 묶어놓은 폴더
# __init__.py : 해당 폴더를 파이썬이 패키지로 인식하도록 해주는 것

# random.py 파일의 코드를 복붙한 것
import random  # 라이브러리는 from 생략 가능
from a import a  # a 패키지 안에 있는 a.py를 복붙한 것
from b import b

# a.py안에 있는 add함수 as 별명
from a.a import add as 더하기함수
from b.b import Person

if __name__ == "__main__":
    더하기함수(1,2)
    p1 = Person("길동이",20)
    p1.print_person()


