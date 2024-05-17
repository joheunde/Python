# 문제 5. 콜라츠 추측

def solution(msg):
    if msg == 1:
        return 0

    cnt = 0
    while msg != 1:
        if cnt == 500:
            return -1
        if msg % 2 == 0:
            msg //= 2
        else:
            msg = msg * 3 + 1

        cnt += 1

    return cnt


print(solution(int(input())))
