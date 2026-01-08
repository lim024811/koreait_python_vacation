books = []

# {"book_id": "1", "book_name": "파이썬책"}
# [{},{}...{}]
while True:
    print("== 도서관리 시스템 ==")
    print("1. 도서 등록")
    print("2. 전체 도서 조회")
    print("3. 도서 삭제")
    print("4. 종료")

    selected_menu = input("메뉴를 선택하세요: ")
    if selected_menu == "1":
        print("도서 등록메뉴입니다.")
        book_id = input("아이디: ")
        book_name = input("책이름: ")
        is_duplicated = False
        for book_dict in books:
            if book_dict["book_id"] == book_id:
                is_duplicated = True
                print("이미 존재하는 아이디입니다.")
                break
        new_book = {"book_id": book_id, "book_name": book_name}
        books.append(new_book)
        print(f"{book_id}에 {book_name}이 등록되었습니다.")
    elif selected_menu == "2":
        if len(books) == 0:
            print("등록된 책이 없습니다.")

        for book in books:
            book_id = book["book_id"]
            book_name = book["book_name"]
            print(f"{book_id}- {book_name}")

    elif selected_menu == "3":
        if len(books) == 0:
            print("등록된 책이 없습니다.")
            continue
        target_id = input("삭제할 아이디: ")

        found = False
        for book in books:
            if book["book_id"] == target_id:
                found = True
                books.remove(book)
                print(f"{book_id}의 {book_name} 삭제 완료")
                break

    elif selected_menu == "4":
        print("프로그램 종료")
        break
    else:
        print("메뉴를 다시 입력하세요: ")
        continue

        # bool([])  -> False
        # if []  -> if False
        # if 0  -> if False
        # if ""  -> if False