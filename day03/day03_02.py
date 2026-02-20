# (자료)형변환
num1 = int("11") # 문자열(str) -> int
print(type(num1))
num2 = int(11.0) # 실수(float) -> 숫자(int)
print(type(num2))

fnum1 = float(11)
print(type(fnum1))
fnum2 = float("11")
print(type(fnum2))

print(str(100) + "원")

# bool(): 논리값(True of False)으로 변환
print(bool("홍길동"))  # True
print(bool(""))  # False
print(bool(" ")) # True
print(bool(0)) # False
print(bool([])) # 비어있는 list, dict, tuple -> False

# if 뒤 bool데이터자리에 다른 자료형이 오면 자동형변환
if 100:
    print("실행될까요?")
if "":
    print("실행안됩니다.")
