coords = [(3,-3),(2,3),(1,-2),(5,6)]

my_coords = []
# 좌표들 중 1사분면에 해당하는 좌표만 모아주세요
# coord = (3,-3) -> (2,-3)....(5,6)
for coord in coords:
    x, y = coord   # x, y = (3,-3)
    if x > 0 and y > 0:
        my_coords.append(coord)

scores = {"김철수": 90,"김영희": 80,"김민수": 100,"박철수": 50,"박영희": 45}
# value들만 모아서 리스트로 가져다줄 수 있음
score_nums = scores.values()
print(score_nums)
# 평균점수 구하기
score_sum = 0
for score in score_nums:
    score_sum += score  # 누적합

score_length = len(score_nums)
score_avg = score_sum / score_length
print(score_avg)

# 60점 이상 학생들의 평균점수
# 60점 이상점수들의 합 / 60점 이상점수들의 갯수
# len() 사용안됨  -> 전체니까 len을 쓴거임 여기서는 몇개만 쓰는거라 len사용이 안됨
score_sum = 0
count_over_60 = 0
# dict에서 value들 점수만 추출
score_nums = scores.values()
for score in score_nums:
    if score >= 60:
        score_sum += score
        count_over_60 += 1

score_avg_over_60 = score_sum / count_over_60
print(score_avg_over_60)
# 또 다른 방법
score_sum = 0
score_over_60s = []
for score in score_nums:
    if score >= 60:
        score_over_60s.append(score)
        score_sum += score

length_over_60 = len(score_over_60s)
score_over_60_avg = score_sum / length_over_60
print(score_over_60_avg)

# scores에서 60점이상인 학생들의 이름을 출력해주세요
# dict -> {이름: 점수}
# [("김철수",90),("김영희",80),...]
score_items = scores.items()

for item in score_items:
    name, score = item  # 튜플 언패킹
    if score >= 60:
        print(f"{name}님 합격입니다!")

tele_book = {"김철수": "01011111111","박철수": "01022222222","최철수": "01033333333","이철수": "01044444444"}
target_number = input("찾으시는 전화번호를 - 빼고 입력해주세요 ")
# target_number가 dict에 value로 존재한다면, 이름을 출력
# 없다면, 발신자 알수없음
tele_book_item = tele_book.items()
is_exist_number = False  # flag - 찾으면, True로 업데이트

for item in tele_book_item:
    name, number = item      # 튜플 언패킹
    if target_number == number:
        print(f"{name}님의 전화입니다.")
        is_exist_number = True
        break    # 찾으면 탈출임. 더이상 반복 필요없음
    else:
        print("발신자 알 수 없음")


# 반복을 다 돌았지만, 여전히 False -> 없는 전화번호
if not is_exist_number:   # is_exist_number 가 False면은 실행이 됨
    print("발신자 알 수 없음")