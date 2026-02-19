# 파이썬 내장함수
# sum(리스트) -> 리스트 내부의 데이터를 모두 합한 것 리턴
nums = [100, 200, 300, 400]
result = sum(nums)
# min(), max() -> 리스트 내부에서 최소값, 최댓값 리턴
min_val = min(nums)
max_val = max(nums)
print(result)
print(min_val)
print(max_val)

# all(리스트): 리스트 내부값을 모두 and연산
# 모두 True면 True

# any(리스트): 리스트 내부값을 모두 or 연산
# -> 하나라도 True면 True
승리조건들 = [True, False, False]
print("승리?", True in 승리조건들)
print("승리?", any(승리조건들))

numbers = [1, 3, 5, 8]
# 짝수가 하나라도 있는가?
result = any([n % 2 == 0 for n in numbers])

names = ["김길동", "최길동", "김철수", "이민수"]
# 도전!) names에 박씨가 한 명이라도 있는가?
# startswith("박") 아니면 name[0] == "박"
park = any([name[0] == "박" for name in names])
print("박씨 있나요?", park)

# 함수의 변수 생존 범위(스코프)
# 1. 함수 안에서 선언된 변수는 함수 안에서만 생존 가능
def a():
    name = "홍길동"
    print("name:", name)

# print(name) # 외부에서는 인식 X

# 2. 외부(일반) 변수는 함수 안에서 "읽기"만 가능
constant = 100
def print_const():
    print("상수:", constant)
    # constant += 100 변경이 막혀있음

3. 외부(일반) 변수를 함수 안에서 변경 시 global
def change_const():
    global constant
    constant += 100
# change_const()
print(constant)

### 문법 끝 ###