# 음식점의 주문 관리 시스템

# 각각의 인덱스는 음식의 고유 코드를 나타냅니다: 0: 김밥, 1: 라면, 2: 돈까스, 3: 샐러드
food_price = [1200, 1500, 1800, 1000]
order_histoty = [1, 2, 0, 1, 1, 2, 0, 3, 2, 2, 1, 0, 3, 2, 0, 1]

total = 0
sum_list = [0] * 4
for i in order_histoty:
    total += food_price[i]
    if i == 0:
        sum_list[0] += 1
    elif i == 1:
        sum_list[1] += 1
    elif i == 2:
        sum_list[2] += 1
    elif i == 3:
        sum_list[3] += 1

if max(sum_list) == sum_list[0]:
    print(f"총 가격:{total} / 가장 많이 주문된 음식: 김밥,{sum_list[0]}회")
elif max(sum_list) == sum_list[1]:
    print(f"총 가격:{total} / 가장 많이 주문된 음식: 라면,{sum_list[1]}회")
elif max(sum_list) == sum_list[2]:
    print(f"총 가격:{total} / 가장 많이 주문된 음식: 돈까스,{sum_list[2]}회")
elif max(sum_list) == sum_list[3]:
    print(f"총 가격:{total} / 가장 많이 주문된 음식: 샐러드,{sum_list[3]}회")
