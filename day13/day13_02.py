# 클래스 변수
# 클래스내부에도 데이터를 저장할 수 있음
# 해당 클래스 객체들은 다 공유

class Student:
    # 클래스변수
    school_name = "파이썬 고등학교"
    count = 0

    def __init__(self, name):
        # 객체(인스턴스) 변수
        self.name = name
        Student.count += 1
        # 정원 100명만 받겠다
        if Student.count > 100:
            print("정원초과 ! 현재 100명")
            # 예외(에러)를 고의로 일으켜야함

st1 = Student("김학생")
st2 = Student("박학생")
print(st1.name)
print(st1.school_name)   # 클래스변수 접근"만" 가능
print(st2.school_name)   # 동일한 변수에 접근"만" 가능

# 데이터의 실제 메모리 주소
id_1 = id(st1.school_name)
id_2 = id(st2.school_name)
print(id_1)
print(id_2)

# 객체로 접근하여서 클래스변수 "변경" 불가능
st1.name = "김학생아님"
print(st1.name)

# 클래스변수 변경이 아니라
# st1에 school_name이라는 필드를 추가한 것으로 파이썬이 해석함.
st1.school_name = "파이썬대학교"
print(st2.school_name)
print(st1.school_name)

# 클래스 이름을 접근해야 변경 가능
Student.school_name = "파이썬대학교"
print(st2.school_name)

print(st1.count)

class Wallet:
    # 공용 돈 -> 클래스 변수
    total_money = 100000
    def __init__(self,name):
        self.name = name
        self.money = 0 # 지갑 생성시 0원

    def __str__(self):
        return f"{self.name}의 소지금: {self.money}"

    def take_money(self, amount):
        # 공용돈을 내 지값(moeny필드)에 옮기는 코드를 작성
        # 남은 공용돈보다 더 많은 금액을 가져갈 수 없음
        # 클래스변수 변경은 클래스. 으로 접근
        # 대소비교, 동일비교 -> 읽기
        # 객체로 접근해도 동일하게 동작
        if not isinstance(amount, int):
            print("숫자를 입력해주세요.")
            return
        if amount > self.total_money:
            print("공용돈이 모자랍니다.")
            return

        Wallet.total_money -= amount
        self.money += amount


w1 = Wallet("홍길동")
w2 = Wallet("홍길동 동생")
w1.take_money(100000)
w2.take_money(20000)  # if문 실행
print(w1)
print(w2)
