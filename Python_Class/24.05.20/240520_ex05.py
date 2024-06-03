# 문제 15. 문자열 다루기 기본

s = input()


def solution(msg):
    if len(msg) == 4 or len(msg) == 6:
        return msg.isdigit()
    else:
        return False


print(solution(s))
