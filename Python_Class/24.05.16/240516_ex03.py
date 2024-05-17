# 문제 3. 정수 내림차순으로 배치하기

def solution(msg):
    solution_list = list(str(msg))
    solution_list.sort(reverse=True)
    return solution_list


my_List = solution(int(input()))
for i in my_List:
    print(i, end='')
