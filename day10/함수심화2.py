# 함수 심화2
# 람다함수
# def로 정의해줘야하는데, 그럴필요없이 단순한 함수면
# 람다함수를 사용한다.
# 성능차이 x / 간결하게 작성이 되지 않으면 굳이 쓸 필요없다. (def 권장)
def mulitply(num1, num2):
    return num1 * num2

lambda_multi = lambda num1, num2: num1 * num2

print(mulitply(5,5))
print(lambda_multi(5,5))

# 함수를 받는 함수 : 고차함수
# 함수를 매개변수로 전달받아 호출하는 함수
def calc(num1, num2, fx):
    result = fx(num1, num2)
    return result

# 콜백함수: 전달되는 함수 ( 직접 호출하는 것이 아니라 함수에 의해 호출이 된 함수 )
def plus(num1, num2):
    return num1 + num2

calc_result = calc(10,5,plus)
print(calc_result)
calc_result2 = calc(10,5, lambda num1, num2: num1 * num2)   # -> 람다함수는 콜백함수로 많이 쓰임.
print(calc_result2)

# 람다함수와 자주쓰이는 내장함수
# 1. filter(): 함수결과가 True인 요소들만 남겨주는 함수 ( 함수를 받는 함수임. )
# filter(함수, 리스트)
nums = [1,2,3,4,5]
result = filter(lambda n: n % 2 == 0, nums)
# filter 결과는 list로 형변환해야 리스트처럼 사용 가능.
print(list(result))

nums = [1, 5, 10, 30, 60, 100]
# filter를 사용해서
# 10~60 사이 숫자들만 리스트로 모아서 출력
result = filter(lambda n : 10 <= n <= 60, nums)
print(list(result))

names = ["김철수", "박철수", "김길동", "최영희"]
# filter를 사용해서
# 김씨만 리스트로 모아서 출력
result = filter(lambda n : n[0] == "김", names)
print(list(result))
