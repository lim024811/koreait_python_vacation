# 클래스
# 클래스의 쉬운설명 : 내가 새로운 자료형을 정의하는 것 ( 자료형이 사실 클래스 였음. )

a = 10
b = "abc"
print(type(a))
print(type(b))   # 결과가 <class 'str'>
print(b.upper())  # str 클래스에는 여러 함수가 존재한다.

# 클래스란 특정데이터와 동작(함수)을 묶은 것.

# 클래스 첫글자는 대문자여야함.
class Puppy:
    # __init__(self, 내가 이 클래스에 넣고싶은 데이터들) -> 생성자
    def __init__(self, name, age):
        # self는 자기자신을 의미
        # self는 생성될때 할당받은 메모리 공간
        # name, age와 같은 객체의 저장공간
        # -> 필드, 멤버변수, 속성라고 불림.
        self.name = name  # 그 메모리 공간에 name, age가 설정되어있는 것.
        self.age = age
        print(f"{self.name}가 생성되었어요!")
    def bark(self): # bark는 그저 함수임
        # self를 통해 각 객체가 가지고 있는
        # 데이터에 따라 서로 다르게 동작 가능.
        print(f"{self.name}가 짖습니다. 멍멍")

# 생성자를 통해 내가 정의한 클래스의 객체(인스턴스)를 생성할 수 있다.
puppy1 = Puppy("초코", 5)
puppy2 = Puppy("뽀삐", 5)
# class 비유
# class는 설계도(틀)이다. -> 붕어빵 틀이다.
# 그 클래스로 생성된 것은 객체(인스턴스) - 붕어빵
# 따라서 같은 틀이지만 서로 다른 객체인 것이다.

# 객체(인스턴스).bark()
puppy1.bark()
puppy2.bark()

# 직접 Car 클래스를 정의해주세요
# 저장하는 데이터는 model, price
# 내부에 drive라는 함수를 정의해주세요
# {모델명}가 주행을 시작합니다! 출력
class Car:
    # 생성자 정의 = Car()호출시 호출됨
    def __init__(self, model, price):
        self.model = model
        self.price = price

    def drive(self):
        print(f"{self.model}가 주행을 시작합니다.")

car1 = Car("벤츠", 1000)
car2 = Car("아우디", 2000)
car1.drive()
car2.drive()
