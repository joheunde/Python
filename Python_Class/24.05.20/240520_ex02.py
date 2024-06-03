# 문제 12. 가운데 글자 가져오기

s = list(input())


def solution(msg):
    if len(msg) % 2 != 0:
        return msg[len(msg) // 2]
    else:
        return msg[len(msg) // 2 - 1] + msg[len(msg) // 2]


print(solution(s))
