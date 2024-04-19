# 문풀 4번
r = 3
n = 2
sign = 1
for _ in range(3):
    mul = 1
    for i in range(n, n + 3):
        mul *= i

    r += sign * 4 / mul
    print(f"결과 : {r}")
    n += 2
    sign = -sign