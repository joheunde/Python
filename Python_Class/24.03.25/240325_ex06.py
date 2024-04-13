# 컴퓨터와 가위바위보 프로그램
import random

me = input("가위/바위/보 중에 하나를 입력 ==> ")
cpu = random.choice(["가위", "바위", "보"])

print(f"컴퓨터 : {cpu}")
if cpu == "가위":
    if me == "가위":
        print("비겼습니다!")
    elif me == "바위":
        print("이겼습니다!")
    elif me == "보":
        print("졌습니다!")
elif cpu == "바위":
    if me == "가위":
        print("졌습니다!")
    elif me == "바위":
        print("비겼습니다!")
    elif me == "보":
        print("이겼습니다!")
elif cpu == "보":
    if me == "가위":
        print("이겼습니다!")
    elif me == "바위":
        print("졌습니다!")
    elif me == "보":
        print("비겼습니다!")