# 내장 함수
# sum(리스트) -> 다 더한결과 리턴
nums = [1,2,3,4]
result = sum(nums)
print(result)

min_val = min(nums)
max_val = max(nums)

# all([]): 모두 True여야 True : 전체 and연산
# any([]): 하나라도 True면 True : 전체 or연산

나의선택 = "가위"
컴퓨터선택 = "보"

승리조건1 = 나의선택 == "가위" and 컴퓨터선택 == "보"
승리조건2 = 나의선택 == "바위" and 컴퓨터선택 == "가위"
승리조건3 = 나의선택 == "보" and 컴퓨터선택 == "바위"
승리조건들 = [승리조건1, 승리조건2, 승리조건3]
print("승리했나요?", True in 승리조건들)
print("승리했나요?", any(승리조건들))  # 승리조건들 중 하나라도 True라면 승리했다.

numbers = [1,3,5,8]
# 짝수가 하나라도 있는가?
result = any([n % 2 == 0 for n in numbers])
print(result)

### 함수의 변수 생존범위(스코프)
# 1. 함수안에 선언된 변수는 함수안에서만 생존
# 2. 일반변수는 함수안에서 읽기만 가능
# 3. 일반변수를 함수안에서 변경시 global 필요
x = 10
def print_x():
    global x   # 일반변수 x를 지정
    x += 1  # 변경 가능해진다.
    print(x)


