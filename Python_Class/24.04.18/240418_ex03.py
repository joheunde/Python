# 문풀 3번
import random

lottery = []

# Hint. if 변수 in 리스트 => 변수가 리스트에 있는지?
while len(lottery) < 6:
    num = random.randint(1, 45)
    if num in lottery:
        continue
    else:
        lottery.append(num)
lottery.sort()
print(lottery)

# 문풀 3번 다른 방법 풀이1
lottery_range = list(range(1, 46))
lottery = random.choices(lottery_range, k=6)
print(lottery)

# 문풀 3번 다른 방법 풀이 2
lottery_range = list(range(1, 46))
random.shuffle(lottery_range)
lottery = lottery_range[:6]
print(lottery_range)
print(lottery)