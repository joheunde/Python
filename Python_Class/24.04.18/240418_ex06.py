# 문풀 6번
import random
sum_dice = 0
dices = [random.randint(1, 6),
         random.randint(1, 6),
         random.randint(1, 6)]

total = dices[0]

for idx in range(2):
    if dices[idx] == 1:
        total += 0
    elif dices[idx] == 6:
        total += dices[idx + 1] * 2
    else:
        total += dices[idx + 1]

print(f"{str(dices)[1:-1]} -> {total}")