# 문제 7. 핸드폰 번호 가리기

def solution(msg):
    msg = list(msg)
    for i in range(len(msg) - 4):
        msg[i] = '*'
    return ''.join(msg)


print(solution(input()))