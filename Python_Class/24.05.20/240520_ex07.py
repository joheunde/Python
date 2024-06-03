# 문제 17. 이상한 문자 만들기

s = list(input())


def solution(arr):
    for i in range(len(arr)):
        if i % 2 == 0:
            print(arr[i].upper(), end='')
        else:
            print(arr[i].lower(), end='')


solution(s)
