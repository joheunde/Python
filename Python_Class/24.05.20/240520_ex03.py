# 문제 13. 행렬의 덧셈

arr1 = [[1, 2],
        [2, 3]]

arr2 = [[3, 4],
        [5, 6]]

return_list = []


def solution(list1, list2):
    for i in range(len(list1)):
        my_list = []
        for j in range(len(list1[0])):
            my_list.append(list1[i][j] + list2[i][j])
        return_list.append(my_list)

    return return_list


print(solution(arr1, arr2))
