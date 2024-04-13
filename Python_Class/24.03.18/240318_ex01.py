people = int(input("여행에 참여하는 총 인원 수: "))
lodge_money = int(input("숙박 비용의 총액: "))
eat_money = int(input("식비의 총액: "))
ect_money = int(input("기타 경비의 총액: "))

total_money = lodge_money + eat_money + ect_money
p_c = total_money / people
print(f"전체 여행 경비는 {total_money}원이며, 인원 수가 {people}명일 때 각자 부담해야 할 금액은 {p_c}원입니다.")