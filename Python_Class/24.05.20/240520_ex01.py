# 문제 11. 직사각형 별찍기

n, m = map(int, input().split())


def solution(x, y):
    for _ in range(y):
        print('*' * x)


solution(n, m)
