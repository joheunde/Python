import random

roll_count = 0
while True:
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    d3 = random.randint(1, 6)

    roll_count += 1
    if d1 == d2 and d2 == d3:
        print(f"주사위는 {d1}입니다.")
        print(f"주사위를 던진 횟수는 {roll_count}입니다.")
        break
