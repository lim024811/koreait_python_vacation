class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_person(self):
        print(f"{self.name}: {self.age}살")

if __name__ == "__main__":
    print("b를 실행했어요")
else:
    print("b를 실행했네요.")