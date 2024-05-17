# 문제 6. 두 정수 사이의 합

def solution(x, y):
    hap = 0
    if x < y:
        for i in range(x, y + 1):
            hap += i
    else:
        for i in range(y, x + 1):
            hap += i

    return hap


a, b = map(int, input().split())
print(solution(a, b))
