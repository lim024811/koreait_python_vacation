# 객체지향 프로그래밍
# 데이터를 저장할 때 안전하게 검증된 값만 저장하고 싶다
# 검증된 값들과 동작을 묶고 싶다.

# 은행계좌 클래스
class BankAccount:
    def __init__(self, name):
        # 검증하는 코드 작성 가능
        self.name = name
        self.balance = 0  # 필드를 무조건 매개변수로 지정안해도 됨. / 계좌개설시 무조건 0원

    def check_balance(self):
        print(f"{self.name}님의 잔액: {self.balance}")

    # 예금
    def deposit(self, amount):
        # amount가 숫자인지 검증
        self.balance += amount

    # 출금
    def withdraw(self, amount):
        if amount > self.balance:
            print("잔액부족!")
            return

        # 검증 이후에 객체에 담긴 데이터를 조작하는 것
        # 객체에 담긴 데이터는 언제나 신뢰가능하다.
        self.balance -= amount

acc1 = BankAccount("홍길동") # 홍길동 계좌 생성
acc2 = BankAccount("김길동") # 김길동 계좌 생성

acc1.deposit(10000)
acc2.deposit(5000)

acc1.withdraw(6000)
acc2.withdraw(6000)

acc1.check_balance()
acc2.check_balance()

# Cup 클래스
# 필드: size(최대용량), water(현재물의 양) - 생성시 0
# 함수: fill(self, amount) - size를 넘어가면 안됨
#      drink(self, amount) - water를 넘어가면 안됨
# check(self): 현재물의 양 출력
class Cup:
    def __init__(self, size):
        self.size = size
        self.water = 0

    def check(self):
        print(f"현재 물의 양: {self.water}")

    def fill(self, amount):
        if self.water + amount >= self.size:
            print("물이 넘칩니다.")
            return

        self.water += amount

    def drink(self, amount):
        if self.water < amount:
            print("물이 충분하지 않습니다.")
            return

        self.water -= amount

amount1 = Cup(30)
amount2 = Cup(20)

amount1.fill(10)
amount2.fill(30)

amount1.drink(30)
amount2.drink(30)

amount1.check()
amount2.check()