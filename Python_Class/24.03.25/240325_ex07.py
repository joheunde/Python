# 도서관 책 대여 시스템

borrow = int(input("현재 대여중인 권수 => "))
user_grade = input("회원등급(Gold/Silver/Bronze) => ")
event = input("특별기간여부(예/아니오) => ")

if event == "예":  # 특별기간이면 4권까지 대여 가능
    cap = 4
else:
    cap = 3

if user_grade == "Gold" or user_grade == "Silver":
    if borrow < cap:
        print("대여가 가능합니다.")
    else:
        print("대여가 불가능합니다.")
else:
    print("대여가 불가능합니다.")