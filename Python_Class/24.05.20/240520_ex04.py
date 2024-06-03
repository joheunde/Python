# 문제 14. 내적

a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]


def solution(arr1, arr2):
    hap = 0
    for i in range(len(arr1)):
        hap += arr1[i] * arr2[i]

    return hap


print(solution(a, b))
