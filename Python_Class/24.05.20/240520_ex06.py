# 문제 16. 같은 숫자는 싫어

arr = [1, 1, 3, 3, 0, 1, 1]


def solution(arr1):
    my_list = []
    for i in range(len(arr1)):
        if i == 0:
            my_list.append(arr1[i])
        elif arr1[i] != arr1[i - 1]:
            my_list.append(arr1[i])

    return my_list


print(solution(arr))
