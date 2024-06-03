# 문제 20. 약수의 개수와 덧셈

left, right = map(int, input().split())


def solution(l, r):
    hap = 0
    for i in range(l, r + 1):
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1

        if cnt % 2 == 0:
            hap += i
        else:
            hap -= i

    return hap


print(solution(left, right))
