# else: 예외없이 성공했을 경우
try:
    age = "10살"
    age = int(age)
except ValueError as e:
    print("숫자가 아니네요")
else:
# try 안에 코드가 에러 없이 작동될 가정 하에 작성됨
    if age > 19:
        print("성인!")
    else:
        print("미성년자!")

# finally: 예외가 발생하건 말건 항상 실행
file = None
try:
    file = open("./hi.txt", "r", encoding="utf-8")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    print("hi.txt 없는데요")
# finally: # 예외와 상관없이
    # 주로 자원반납
    if file is not None:
        file.close()

# 도전) 아래의 코드를 try-except-else-finally
# 에러 없이 성공시 result를 출력
# 에러 발생과 무관하게 "계산완료!" 출력
# num1 = input("첫 번째 숫자 입력 > ")
# num1 = int(num1)
# num2 = input("두 번째 숫자 입력 > ")
# num2 = int(num2)
# result = num1 / num2

# try:
#     num1 = int(input("첫 번째 숫자 입력 > "))
#     num2 = int(input("두 번째 숫자 입력 > "))
#     result = num1 / num2
# except ValueError as e:
#     print("숫자만 입력 가능")
# except ZeroDivisionError as e:
#     print("0으로 나눌 수 없습니다.")
# # except (ValueError, ZeroDivisionError) as e:
# else:
#     print("결과:", result)
# finally:
#     print("계산 완료!")

# 예외객체를 의도적으로 생성하는 문법
# raise 에러클래스()
try:
    raise ValueError("저는 님이 만든 에러입니다.")
except ValueError as e:
    # e를 출력하면 생성할 때 넣어준 메시지가 출력됨
    print(e)
    print(f"오류 내용: {e}")
# 커스텀(비즈니스) 예외정의
# Exception 클래스를 상속받으면 ok
class ScoreError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

class TestScore:
    def __init__(self, score):
        if not (0 <= score <= 100):
            raise ScoreError("0 ~ 100 사이의 값만 가능합니다")
        self.score = score

t1 = TestScore(50)
try:
    t2 = TestScore(999)
except ScoreError as e:
    print(e)
    # 에러 상황 시 분기시키고 싶은 코드를 작성

email = input("이메일 >>> ")

# @가 없으면 EmailError를 발생시켜주세요
# EmailError를 만들어주세요
class EmailError(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class EmailError2(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.message = message

class Email:
    def __init__(self, email):
        if '@' not in email:
            raise EmailError("@가 없습니다")
        self.email = email

try:
    if "@" not in email: # @ 포함 조건문
        raise EmailError("@가 없습니다")
    if "." not in email:
        raise EmailError2("올바른 이메일 형식이 아닙니다")
    user_email = Email(email)
except EmailError as e:
    print(e) # 에러 메시지 출력 ex) "@가 없습니다"
except EmailError2 as e:
    print(e)
else:
    print("올바른 이메일 형식입니다.")