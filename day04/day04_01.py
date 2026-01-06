# 튜플(tuple)
# 변경이 불가능한 리스트 (수정과 석제가 안된다.)
# 한번 데이터가 들어오면 "불변" (원본훼손 x)

numbers = (1,2,3,4)
number = (1,)       # 요소가 하나일때는 쉼표
fruits =("사과","바나나","포도","수박")

print(fruits[0])   # 인덱싱으로 조회가능
# fruits[0] = "망고"

# idx를 찾을 수 있음
# 0번부터 조회해서 처음발견된 idx만 가져옴
grape_idx = fruits.index("포도")
print(grape_idx)

# 갯수찾기
grape_count = fruits.count("포도")

# 슬라이싱은 가능
# 슬라이싱은 원본은 건드리지 않고
# 복사해서 가공하여 새로 만들어주는 것
names = ("홍길동","김길동","박길동")
print(names[:2])  # 슬라이싱
print(names)      # 원본은 보존 됨

# 리스트는 불변?
sample = ["데이터1","데이터2"]
print(sample)
sample.append("데이터3")
print(sample)            # 원본에 "데이터3"이 추가됨

# 튜플 언패킹
mr_kim = ("김길동","대한민국",30,"남자")
name, nationality, age, gender = mr_kim
print(name,nationality,age,gender)  # 대입확인

# 값 바꾸기
a,b,c,d = 10,20,30,40

a,b = b,a
print(a,b)

# 실습) 주어진 coord좌표가 몇사분면에 있는지 판별하여 출력!
# 원점, x축, y축 위의 경우 고려x
coord = (3,-3)
x,y = coord  # 튜플 언패킹

if x > 0 and y > 0:
    print("1사분면")
elif x < 0 and y > 0:
    print("2사분면")
elif x < 0 and y < 0:
    print("3사분면")
elif x > 0 and y < 0:
    print("4사분면")   # if로 다 써도됨

if x > 0:
    if y > 0:
        print("1사분면")
    elif y < 0:
        print("4사분면")       # 이렇게 써도됨

# 컬렉션 자료형들(list,tuple,set)
# 서로 형변환이 가능
example = ("데이터1","데이터2")
list_example = list(example)
print(list_example)    # 튜플 -> 리스트
tuple_example = tuple(list_example)
print(tuple_example)   # 리스트 -> 튜플