# 문제 4. x만큼 간격이 있는 n개의 숫자

def solution(msg, inc):
    solution_list = []
    add = msg
    for i in range(1, inc + 1):
        solution_list.append(add * i)

    return solution_list


x, n = map(int, input().split())
print(solution(x, n))
