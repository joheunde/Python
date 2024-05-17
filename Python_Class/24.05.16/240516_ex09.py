# 문제 9. 음양 더하기

def solution(absolutes, signs):
    hap = 0

    for i in range(len(absolutes)):
        if signs[i] == "true":
            hap += absolutes[i]
        if signs[i] == "false":
            hap += -absolutes[i]

    return hap


print(solution([1, 2, 3], ["false", "false", "true"]))

