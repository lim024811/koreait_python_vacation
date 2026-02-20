# 클래스메서드 / 정적메서드

class Person:
    # 클래스변수
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1   # 객체가 하나씩 생성될때마다 population의 수도 증가

    # 인스턴스 메서드
    # self를 매개변수로 받고있는 것. -> 객체가 아니면 호출이 안됨.
    # 객체.메서드() 형태로 호출
    def print_person(self):   # self는 p1의 주소, p2의 주소
        print(f"{self.name} 입니다.")

    # 클래스메서드
    # 클래스이름으로 호출가능
    # 객체로도 호출가능
    @classmethod  # @: 어노테이션( 파이썬이 어노테이션을 읽으면 다르게 동작함. / 그저 파이썬을 최적화하기 위함임. )
    def print_population(cls):   # cls : class의 줄임말
        print(f"현재인구수: {cls.population}")

    # 클래스로부터 생성된 객체들이
    # 자주 사용할 것 같은 일반메서드 -> 정적메서드( 따로 빠져도 무관, 그냥 묶어만 둔것임. )
    @staticmethod
    def is_adult(age):
        return age > 19

    # 인스턴스 메서드
    def is_adult2(self):
        return self.age < 19

    # __init__을 간접적으로 호출해서
    # 객체를 생성하는 방법
    @classmethod
    def from_dict(cls, data):
        # dict에 담긴 정보로
        # Person객체를 만들어보자
        return cls(data["name"], data["age"])

p1 = Person("홍길동",10)
p2 = Person("길동이동생",8)
p1.print_person()
p2.print_person()
# 클래스메서드 호출
p1.print_population()
Person.print_population()

p1.is_adult(p1.age)  # p1의 age를 모름. p1.age 로 알려줘야함
p1.is_adult2()   # p1의 age를 알아서 안넣어줘도됨

dict_person = {"name": "김철수","age": 25}
p3 = Person(dict_person["name"], dict_person["age"])
p4 = Person.from_dict(dict_person)

"""
1. 인스턴스메서드 -> self -> 필드값 조작 or 활용할때 사용
2. 클래스메서드 -> cls -> 클래스변수, 객체생성시 사용
3. 정적메서드 -> 일반함수 -> 일반함수가 자주쓰이면 묶어줌
"""