# 문풀 5번
import random
player = int(input("복권 번호(1-99)를 입력하시오: "))
winner = random.randint(1, 99)

print(f"당첨 번호는 {winner}입니다.")
if player == winner:
    print("1등상")
elif player // 10 == winner // 10 or player % 10 == winner % 10:
    print("2등상")
else:
    print("미당첨")