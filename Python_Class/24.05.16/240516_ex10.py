# 문제 10. 없는 숫자 더하기

def solution(numbers):
    hap = 0

    for i in range(0, 10):
        if i not in numbers:
            hap += i

    return hap


print(solution([5, 8, 4, 0, 6, 7, 9]))
