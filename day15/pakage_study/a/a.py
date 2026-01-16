print("a에서 실행!")

def add(num1, num2):
    return num1 + num2


# __name__
# py파일 실행 -> 파이썬이 내부적으로 __name__변수를 생성
# import된 py와 내가 실행한 py를 구분함
# 내가 실행한 py의 __name__은 "__main__"
# 내가 import한 py의 __name__은 "모듈이름"

# b.py에 Person class 정의
# name, age필드 가짐
# 함수 print_person : f"{이름}: {나이}살" 출력!
# main.py에서 Person class import -> 객체 생성
# print_person() 호출 까지

if __name__ == "__main__":  # 내가 a.py를 실행시켰을때 실행됨
    result = add(1, 2)
    print(result)


