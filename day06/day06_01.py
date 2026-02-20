# day06_01
# 정보처리기사 실기 기출
a = ["Seoul","Kyeonggi","Incheon","Daejun","Daegu","Pusan"]
str = "S"

for i in a:
	str = str + i[1]

print(str)

# 이중 for문 - 비교
s1 = ["a","b","c"]
s2 = ["com","b","d","p","c"]
# s1과 s2 배열의 유사도를 출력 - 같은 요소가 몇개?

count = 0

for x in s1:
    for y in s2:
        if x == y:
            print(f"{x}와 동일한 데이터 {y}발견")
            count += 1

print(count)

# break & continue
# break를 읽으면 반복문을 한번 탈출
for num in range(10):
    # 10번 반복 중 num이 5가 되면 탈출
    if num == 5:
        print("5가 되었습니다. 탈출!")
        break                        # for문을 바로 탈출

    print(num)

# continue를 읽으면 다음반복을 즉시 실행
for num in range(10):
    # 10번 반복 중 num이 5가 되면 다음반복 실행
    if num == 5:
        print("5가 되었습니다. 스킵!")
        continue

    print(num)  # num이 5면 실행되지 않음

# 짝수만 출력 !
for num in range(10):
    if num % 2 != 0:  # 홀수면
        continue   # 다음반복

    print(num)

foods = ["계란","우유(상함)","사과","김치","수박(상함)"]

# "(상함)"이 포함되지 않은 음식만 출력!
for food in foods:
    if "(상함)" in food:
        continue          # (상함)이 있는 음식만 스킵, 즉 제외하고 넘어가서 결과 출력

    print(food)

# 원본을 수정하려면? 인덱스정보가 필요하다
# enumerate(): 리스트 데이터를 (인덱스, 데이터) 튜플형태로 만들어준다
# ["계란","우유(상함)","사과","김치","수박(상함)"]
# [(0,"계란"),(1,"우유(상함)")...(4,"수박(상함)")]

samples = enumerate(foods)
# idx, food = (0,"계란")
for sample in samples:        # for idx, food in samples: -> 튜플언패킹
    print(sample)             #     print(f"{idx}: {food}")

for idx, food in enumerate(foods):
    # "(상함)"
    if "(상함)" in food:
        # 원본 수정
        foods[idx] = food[:-4]
print(foods)

fruits = ["사과","바나나","체리","포도","망고"]
# 홀수 인덱스에 있는것만 출력해 주세요!
# continue 사용, enumerate()사용
# enumerate() 를 쓰면 [(0,"사과"),(1,"바나나"),....(4,"망고")]
# idx, fruit = (0,"사과")

for idx, fruit in enumerate(fruits):
    if idx % 2 == 0:  # 짝수 인덱스면
        continue      # 스킵(다음반복)

    print(fruit)




