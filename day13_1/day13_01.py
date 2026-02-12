# 클래스 - 상속
# 두 개 이상의 클래스가 공통모드가 많을 때
# 상위(부모) 클래스를 정의해서 뒤에 줄 수 있음

class Pet:
    def __init__(self, name, age):
        print("pet의 생성자 호출!")
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}가 밥을 먹습니다.")

    def sleep(self):
        print(f"{self.name}가 잠듭니다.")

# 클래스 이름(상위 클래스) - 상속
# Dog 클래스에 breed 필드를 추기해주세요
class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self):
        print(f"{self.name}: 멍멍!")

    # 부모의 함수를 재정의 -> 부모의 함수는 가려짐
    # 오버라이딩
    # 함수 이름, 매개변수 동일
    def eat(self):
        print(f"{self.name}가 사료를 먹습니다.")

# Dog 클래스에는 생성자 없지만, 부모에 정의된 걸 사용
dog1 = Dog("초코", 3, "푸들")
dog1.eat()
print(dog1.age)
print(dog1.breed)

#MRO (Method Resolution Order)
# 자식클래스 객체가 호출한 함수가 자식클래스에 없으면
# 파이썬은 부모클래스에 해당 함수를 찾으러 감

# Pet을 상속받는 Cat 클래스 정의
# eat 함수를 오버라이딩 - print(f"{self.name}가 깻잎을 먹어요")
class Cat(Pet):
    # 부모로부터 물려받은 필드 말고
    # Cat만 가져오는 필드는 어떻게 정의?
    def __init__(self, name, age, color):
        # super(): 부모의 함수를 호출하게 해주는 함수
        # super()는 self 안에 super 영역만 리턴하는 함수.
        # super는 self의 부분집합이다.
        super().__init__(name, age)
        self.color = color

    def cat(self):
        print(f"{self.name}가 깻잎을 먹어요")

    def play(self):
        super().sleep() # 부모의 sleep()
        super().eat() # 부모의 eat()
        # 상속받은 자식 객체는 super(부모)영역이 구분되어 있음
        # self는 super를 포함한다(# super는 self의 부분집합이다.)
        # 필드, 함수가 동일한 경우
        # 일반적인 조회, 호출 -> 자식
        # super() 명시하면 -> 부모
        # super().name
        # super().age
        # self.name
        # self.age
        # self.color

# isinstance와 상속
# self는 super를 포함한다.
# -> 해당 클래스 정보가 포함되어 있나?
result = isinstance(dog1, Pet)
print(f"dog1이 Pet클래스 출신?: {result}")
print(result)


