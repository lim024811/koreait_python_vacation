# day03_01
"""
멀티라인 - 함수설명(docString)용
변수에 할당하지만 않으면, 주석처럼 사용가능
"""
name = "홍길동"
test = f"""hello
world!
my name is {name}
"""
print(test)

"""
조건문
if bool데이터:
    bool데이터가 True일때 실행되는 코드
"""
#코드블럭 - 코드의 영역
# 들여쓴 블럭을 코드블럭을 하나의 영역으로 간주한다.
if False:
    print("if문 안쪽입니다.")
print("if문 밖입니다.")

# 10만원 이상이면 10% 할인가격
# 아니면 할인이 없는 가격
# input()으로 받아온 데이터는 모두 문자열(str)이다.
price = int(input("상품가격을 입력하세요: "))

if price >= 1000000:
    price = price * 0.9
    print(price)
else:   # 위의 모든 조건이 False일때
    print(price)

# if ~ elif ~ else : 하나의 코드블록만 사용 (마지막은 else로)
# 순차적으로 검사(위부터 아래로)

age = 15

# 조건은 내림차순, 오름차순으로 작성되어야함 (그래야 단계별로 실행가능/ 범위좁히면서)
if age >= 20:
    print("성인")
elif age >= 17:  # 이전조건이 False였다
    print("고등학생")
elif age >= 14:
    print("중학생")
elif age >= 8:
    print("초등학생")
else:
    print("미취학아동")

isLogin = False
isBanned = True

if not isLogin:
    # 로그아웃상태라면
    print("로그인을 하셔야합니다.")
elif isBanned:
    print("정지된 계정입니다.")

"""
bmi 계산기
bmi = 체중(kg) /  키(m) * 키(m)
bmi가
30이상 비만 / 25이상 30미만 과체중
18.5이상 25미만 정상 / 18.5미만 저체중
철수(174cm, 70kg)의 비만도를 출력!
"""
weight = 70
height = 1.74
bmi= weight / (height * height)  #(height ** 2)로도 가능
if bmi >= 30:
    print("비만")
elif bmi >= 25:  # 위의 조건들이 Flase -> bmi < 30
    print("과체중")
elif bmi >= 18.5:  # bmi > 25
    print("정상")
else:
    print("저체중")

# 홀짝 판별
# num이라는 변수에 숫자를 입력받고
# 짝수면 짝수입니다  홀수면 홀수입니다. 출력
num = input("숫자를 입력하세요: ")
num = int(num) # str -> int 형변환
if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
