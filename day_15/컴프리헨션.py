# 컴프리헨션 - 표현식
# [], {}를 생성/조작하는 문법
# 생성 / for / if 한 줄에 표현
from day15.컴프리헨션 import discount_menus

# 1. [] 컴프리헨션
nums = [1, 2, 3, 4, 5]
square_nums = []
for num in nums:
    square_nums.append(num ** 2)

# [연산식 for 변수 in 리스트 (if 조건 - 필터링)]
com_nums = [num ** 2 for num in nums]
print(com_nums)

# 짝수들만 '필터링'하고 제곱
# 홀수는 추가되지 않음
com_evens = [num ** 2 for num in nums if num % 2 == 0]
print(com_evens)

# 홀수는 그대로 두고 짝수만 제곱하려면
# [연산식(삼항연산자) for 변수 in 리스트]
# 삼항 연산자) (True일 때 값) if (조건) else (False일 때 값)
com_evens_odd = [num ** 2 if num % 2 == 0 else num for num in nums]
print(com_evens_odd)

scores = [85, 40, 90, 55, 75] # 60점 커트라인
# ["합격", "불합격", "합격", "불합격", "합격"]
result = ["합격" if score >= 60 else "불합격" for score in scores]

print(result)

# 2. {} 컴프리헨션
'''
{
    1: 1,
    2: 4,
    3: 9,
    4: 16,
}
'''
square_dict = {}
for num in range(1, 5):
    square_dict[num] = num ** 2
    # square_dict.update({
    # num: num ** 2})
print(square_dict)

# {key: value for 변수 in 리스트}
square_dict = {num: num ** 2 for num in range(1, 5)}
print(square_dict)

# 예시
fruits = ["apple", "banana", "cherry", "kiwi"]
# dict 컴프리헨션으로 만들어주세요
# 문자열의 길이
# {"apple": 5, "banana": 6, "cherry": 6, "kiwi": 4}

fruits_length = {fruit: len(fruit) for fruit in fruits}

print(fruits_length)
print({fruit: len(fruit) for fruit in fruits})

# items() + {}com을 사용하면 key: value 조작이 한결 쉬워짐

menu = {
    "라면": 5000,
    "김밥": 5500,
    "햄버거": 3000
}
# [("라면", 5000), ("김밥", 5500), ("햄버거", 3000)]
discount_menu = {name: price * 0.9 for name, price in menu.items()}
print(discount_menu)

students = {
    "철수": 90,
    "영희": 60,
    "민수": 50
}
# {"파이썬-철수": 90, "파이썬-영희":60, "파이썬-민수": 50}
python_students = {f"파이썬-{name}": score for name, score in students.items()} # f"파이썬-{name}"
print(python_students)