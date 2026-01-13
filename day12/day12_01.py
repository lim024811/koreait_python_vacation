# 상속
# 두개 이상의 클래스가 공통코드가 많을 때
# 이를 상위클래스(부모클래스)를 정의해서 묶어줄 수 있음.  ( 클래스간 연결시켜줌 )

class Pet:  # -> 부모 클래스 Pet
    def __init__(self, name, age):
        print("부모클래스 생성자 호출!")
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}가 밥을 먹습니다.")

class Dog(Pet):
    def sound(self):
        print(f"{self.name}가 짓습니다. 머엉")

class Cat(Pet):
    def sound(self):
        print(f"{self.name}가 말합니다. 야앙")

    # 부모의 함수를 재정의: 오버라디이(overwriting)
    def eat(self):
        print("캣잎주세요")

# __init__ 을 정의하지 않았음
# Dog와 Cat의 생성자를 호출했지만.
# 부모클래스의 __init__이 호출됨.
dog = Dog("뽀삐",5)
cat = Cat("나비",5)
dog.eat()  # 부모클래스 eat
cat.eat()

# MRO(method resolution order) 파이썬의 메소드 순서 규칙
# 자식클래스에 호출한 함수가
# 없으면 파이썬은 부모클래스에 해당 함수를 찾으러 간다.
# 있으면 부모껄 호출

# 오버라이딩 활용
class Car:
    def __init__(self, name, model):
        print("부모클래스 생성자 호출!")
        self.name = name
        self.model = model

    def drive(self):
        print(f"{self.name}이 주행을 시작합니다")

# 상속받은 자식 객체는 super(부모) 객체의 데이터 영역이
# 구분되어있다.
# 단, self의 데이터 영역은 super 객체의 데이터영역을 포함한다.
class EletricCar(Car):
    # __init__을 재정의한 것임.
    # super().__init__()이 호출되어야함.
    def __init__(self, name, model, battery):
        super().__init__(name, model)
        # super(): 부모의 메서드를 연결해주는 함수 (Car의 __init__을 호출)
        self.battery = battery

    # 오버라이딩
    def drive(self):
        super().drive()  # 부모의 drive 호출
        print("전기로!!")

class GasCar(Car):
    # __init__을 재정의한 것임.
    # super().__init__()이 호출되어야함.
    def __init__(self, name, model, gas):
        super().__init__(name, model)
        # super(): 부모의 메서드를 연결해주는 함수 (Car의 __init__을 호출)
        self.gas = gas

    # 오버라이딩
    def drive(self):
        super().drive()  # 부모의 drive 호출
        print("휘발유로!!")

# 호출된 test_car는 같은 코드임
# 같은 코드인데 동작이 달라짐.
def test_car(car):
    # 검증코드필요(car가 drive라는 함수를 가지고 있는 지 확인이 필요)
    # 매개변수로 들어온 car가 drive() 함수를 반드시 가지고 있길 원함.
    # drive는 오버라이딩된 함수
    # -> Car를 상속받은 객체인지만 확인하면 된다.
    is_car_instance = isinstance(car, Car)
    if not is_car_instance:
        print("자동차가 아닙니다.")
        return

    car.drive()  # 같은 함수 호출 중
    # drive라는 같은 함수 -> 다른 동작
    # : 다형성

e_Car = EletricCar("모델y","tesla",100)
g_Car = GasCar("x3","bmw",100)
test_car(e_Car)
test_car(g_Car)

class Payment:
    def __init__(self):
        print("결제시스템 초기화")

    # pass = 나중에 구현하겠다 에러방지
    # 상속받은 자식클래스에서 오버라이딩하면 호출이 안됨.
    def pay(self, price):
        pass


# KakaoPayment - pay 오버라이딩 15000원 이상 결제시 5퍼할인
# NaverPayment - pay 오버라이딩 20000원 이상 결제시 2000원 할인

class KakaoPayment(Payment):
    # 생성자 생략 - 생성자를 오버라이딩할때는
    # super().__init__() 필요
    def pay(self,price):   # 부모클래스의 pay 함수의 매개변수와 동일해야함.
        # super().pay() 오버라딩 시 필수 아니다.
        if price >= 15000:
            return price * 0.95

        return price

class NaverPayment(Payment):
    def pay(self,price):
        if price >= 20000:
            return price - 2000

        return price

def order(payment, price):
    is_payment = isinstance(payment, Payment)
    if not is_payment:
        print("올바른 결제방식을 선택하세요")
        return

    total_price = payment.pay(price)
    print(f"총 결제금액: {total_price}원")


# [{피자: 2},{라면: 1}...]
# 위의 리스트를 받아서 결제 총금액을 리턴
food_menu = {"피자": 25000,"치킨": 20000,"참치김밥":5000,"라면":4000,"제로콜라": 1500}

def accept(menus):
    # 메뉴들에서 메뉴를 골라 옴
    price_sum = 0

    for menu in menus:
        # menu -> {메뉴이름: 갯수}
        # menu.items() -> [(메뉴이름: 갯수)]
        for item_name, item_count in menu.items():
            price = food_menu[item_name]
            price_sum += price * item_count

    return price_sum

cart = []
while(True):
    food_list = list(food_menu.keys())
    print(food_list)
    menu_name = input("담으실 메뉴를 입력하세요:")
    count = int(input("몇개 담으시겠습니까"))

    cart_item = { menu_name: count }
    cart.append(cart_item)

    confirm = input("주문을 마치시겠습니까?(yes, no)")
    if confirm.lower() == "yes":
        break

total_price = accept(cart)
print(total_price)

kakao = KakaoPayment()
naver = NaverPayment()
order(kakao, total_price)
order(naver, total_price)
