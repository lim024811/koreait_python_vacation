import random  # 외부에서 코드를 빌려오는 것

# random.randint(1,6) -> 1 ~ 6 사이 랜덤 숫자 생성
my_random_num = random.randint(1,6)
fruits = ["사과","바나나","포도","배"]
random_fruit = random.choice(fruits)    # 리스트 중 무작위 하나 선택해옴

# 업다운게임
answer_num = random.randint(1,100)

while True:
    my_guess = input("1~100 사이 숫자를 입력하세요: ")
    # 문자열.isdecimal(): 0~9 문자로 이루어졌는가?
    if not my_guess.isdecimal():
        print("숫자만 입력하세요")
        continue

    my_guess = int(my_guess)   # 형변환 ( 문자열 -> 정수 )
    # my_guess가 answer보다 크면 "다운!"을 출력
    # my_guess가 answer보다 작으면 "업!"을 출력
    # my_guess가 answer보다 같으면 정답:{번호}을 출력하고 탈출
    if my_guess < 1 or my_guess > 100:
        print("1~100 사이 입력하세요: ")
        continue
    if my_guess > answer_num:
        print("업!")
    if my_guess < answer_num:
        print("다운!")
    if my_guess == answer_num:
        print(f"정답: {my_guess}")



# 가위 바위 보
가위바위보 = ["가위","바위","보"]
나의선택 = ""
컴퓨터선택 = ""

while True:
    나의선택 = input("가위,바위,보 중 하나를 입력해주세요: ")

    # 입력값 검증
    if 나의선택 not in 가위바위보:
        print("다시 입력하세요")
        continue

    컴퓨터선택 = random.choice(가위바위보)

    승리조건1 = 나의선택 == "가위" and 컴퓨터선택 == "보"
    승리조건2 = 나의선택 == "바위" and 컴퓨터선택 == "가위"
    승리조건3 = 나의선택 == "보" and 컴퓨터선택 == "바위"
    승리조건들 = [승리조건1, 승리조건2, 승리조건3]
    if 나의선택 == 컴퓨터선택:
        print("무승부")
        continue
    elif True in 승리조건들:
        print("승리!")
        break
    else:
        print("패배..")

# 3판 2선
# 사용자점수, 컴퓨터점수가 있고 먼저 3점을 획득하면 승리
가위바위보 = ["가위", "바위", "보"]
나의선택 = ""
컴퓨터선택 = ""

while True:
    나의선택 = input("가위,바위,보 중 하나를 입력해주세요: ")
    나의선택 = 나의선택.srtip()    # 공백 삭제
    # **특가 할인**.strip("*") -> * 삭제됨.
    나의점수 = 0
    컴퓨터점수 = 0
    # 입력값 검증
    if 나의선택 not in 가위바위보:
        print("다시 입력하세요")
        continue

    컴퓨터선택 = random.choice(가위바위보)

    승리조건1 = 나의선택 == "가위" and 컴퓨터선택 == "보"
    승리조건2 = 나의선택 == "바위" and 컴퓨터선택 == "가위"
    승리조건3 = 나의선택 == "보" and 컴퓨터선택 == "바위"
    승리조건들 = [승리조건1, 승리조건2, 승리조건3]
    if 나의선택 == 컴퓨터선택:
        print("무승부")
        continue
    elif True in 승리조건들:
        print("승리!")
        나의점수 += 1
    else:
        print("패배..")
        컴퓨터점수 += 1
    if 나의점수 == 2:
        print("승리!")
        break
    elif 컴퓨터점수 == 2:
        print("컴퓨터승리!")
        break

    print(f"나 - {나의점수} : 컴퓨터 - {컴퓨터점수}")
print("게임종료")