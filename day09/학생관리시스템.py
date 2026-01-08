# 학생관리시스템

students = []
# { "name": "이름","student_id": 1, "major": "컴공" }
# [ {},{},{}...{}]

# 메인 루프
while(True):
    print("=== 학생관리 시스템 ===")
    print("1. 학생 등록")
    print("2. 전체 학생 조회")
    print("3. 학생 삭제(이름)")
    print("q. 종료")

    selected_menu = input("메뉴 번호 입력: ")
    if selected_menu == "1":
        # 학생 등록
        print("학생 등록메뉴 입니다.")
        name = input("이름: ")
        stu_id = input("학번: ")
        major = input("전공: ")
        # 1. 중복 학번이 입력되면
        # "이미 존재하는 학번입니다." 출력
        # continue
        for stu_dict in students:    # 리스트에서 꺼내온건 dict
            # dict에서 필요한 value만 꺼냄
            std_id = stu_dict["student_id"]
            if std_id == stu_id:
                print("이미 존재하는 학번입니다.")
                continue

        new_stu = {"name": name, "student_id": stu_id, "major": major}
        students.append(new_stu)
        print(f"{name} 학생이 등록되었습니다.")

    elif selected_menu == "2":
        # 2. 학생이 아무도 없으면, "등록된 학생이 없습니다." 출력
        # 자동형변환 & len()
        if len(students) == 0:
            print("등록된 학생이 없습니다.")
        # 학생 전체 조회
        for student in students:
            stu_id = student["student_id"]
            name = student["name"]
            major = student["major"]
            print(f"{stu_id}: 이름-{name}, 전공-{major}")
    elif selected_menu == "3":
        # 학생 삭제
        if len(students) == 0:
            print("등록되어있는 학생이 없습니다.")
            continue
        target_id = input("삭제할 학생의 학번: ")

        found = False    # -> if문 부터 for문 전까지는 아이디 못찾았다를 명확하게 하기 위해서 found =  False 사용
        for stu_dict in students:
            std_id = stu_dict["student_id"]
            if std_id == target_id:
                found = True        # -> for문을 거쳐 아이디를 찾았다는 것을 명확하게 하기 위해 found = True 사용
                students.remove(stu_dict)
                print(f"{std_id} 학번 학생 삭제 완료")
                break

        if not found:       # 아이디를 지인짜로 못찾았으면
            print("해당 id의 학생을 찾을 수 없습니다.")

    elif selected_menu == "q":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 입력입니다. 다시 입력하세요.")
        continue
