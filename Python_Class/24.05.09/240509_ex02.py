# 계산기 만드는 문제

def calc(v1, v2, op):
    if op == '+':
        return v1 + v2
    elif op == '-':
        return v1 - v2
    elif op == '*':
        return v1 * v2
    elif op == '/':
        return v1 / v2


op = input("계산입력(+, -, *, /) : ")
v1 = int(input("숫자 1 입력 : "))
v2 = int(input("숫자 2 입력 : "))
result = calc(v1, v2, op)
print(f"계산결과 : {v1} {op} {v2} = {result}")