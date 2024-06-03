# 문제 18. 부족한 금액 계산하기

price, money, count = map(int, input().split())


def solution(pr, mon, cnt):
    hap = 0
    for i in range(1, cnt + 1):
        hap += pr * i

    return hap - mon


print(solution(price, money, count))
