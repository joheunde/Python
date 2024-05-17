# 문제풀이_1_10

# 문제 1. 문자열 내 p와 y의 개수
def solution(string):
    string.lower()
    if string.count('p') == string.count('y'):
        return print("true")
    else:
        return print("false")


s = input()
solution(s)
