# 문제 2. 하샤드 수

def solution(msg):
    my_list = list(str(msg))
    hap = 0
    for i in my_list:
        hap += int(i)

    if msg % hap == 0:
        return True
    else:
        return False


print(solution(int(input())))
