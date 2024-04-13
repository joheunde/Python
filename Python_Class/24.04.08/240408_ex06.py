# 음식점의 주문 관리 시스템

# 각각의 인덱스는 음식의 고유 코드를 나타냅니다: 0: 김밥, 1: 라면, 2: 돈까스, 3: 샐러드
food_price = [1200, 1500, 1800, 1000]
order_history = [1, 2, 0, 1, 1, 2, 0, 3, 2, 2, 1, 0, 3, 2, 0, 1]

total = 0
sum_list = [0] * len(food_price)
for i in order_history:
    total += food_price[i]
    sum_list[i] += 1

if max(sum_list) == sum_list[0]:
    print(f"총 가격: {total} / 가장 많이 주문된 음식: 김밥,{sum_list[0]}회")
if max(sum_list) == sum_list[1]:
    print(f"총 가격: {total} / 가장 많이 주문된 음식: 라면,{sum_list[1]}회")
if max(sum_list) == sum_list[2]:
    print(f"총 가격: {total} / 가장 많이 주문된 음식: 돈까스,{sum_list[2]}회")
if max(sum_list) == sum_list[3]:
    print(f"총 가격: {total} / 가장 많이 주문된 음식: 샐러드,{sum_list[3]}회")


# 교수님 풀이
food_price = [1200, 1500, 1800, 1000]
order_history = [1, 2, 0, 1, 1, 2, 0, 3, 2, 2, 1, 0, 3, 2, 0, 1]

total = 0
order_cnt = [0] * len(food_price)

for order in order_history:
    total += food_price[order]
    order_cnt[order] += 1

# 가장 많이 팔린 횟수 (max)
max_cnt = 0
for c in order_cnt:
    if c > max_cnt:
        max_cnt = c

print(f"총 가격 : {total} / ", end='')
print("가장 많이 주문된 음식 : ", end='')
food_names = ["김밥", "라면", "돈까스", "샐러드"]
for idx in range(len(order_cnt)):
    if order_cnt[idx] == max_cnt:
        print(food_names[idx], end=', ')
print(f"{max_cnt}회")