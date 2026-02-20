def add(num1, num2):
    print("a에서 만든 add 호출됨")
    return num1 + num2

print("저는 a.py에 있는 코드입니다.")

# __name__
# py파일 실행 -> 파이썬에 내부적으로 py별로 __name__변수 생성
# import된 py파일과 내가 실행한 py파일을 구분
# 내가 실행한 py파일의 __name__은 "__main__"이 된다
# import한 py파일의 __name__은 "모듈 이름"

if __name__ == "__main__":
    add(1, 2)
    print("a에서 실행하셨군요")
else:
    print("a를 import하셨군요")
