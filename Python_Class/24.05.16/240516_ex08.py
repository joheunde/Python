# 문제 8. 나누어 떨어지는 숫자 배열

def solution(arr, div):
    solution_list = []

    for i in arr:
        if i % div == 0:
            solution_list.append(i)

    solution_list.sort()
    if len(solution_list) == 0:
        return -1
    return solution_list


print(solution([2, 36, 1, 3], 1))
