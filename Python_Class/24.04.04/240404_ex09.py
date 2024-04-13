# 3 + 4/(2*3*4) - 4/(4*6*8) + ...

r = 3
n = 2
sign = 1
for _ in range(100):
    mul = 1
    for i in range(n, n + 3):
        print(i, end=' ')
        mul = mul * i
    print(f"곱 : {mul}")
    # 누적값 계산
    r += sign * 4 / mul
    print(f"결과 : {r}")

    # 다음 곱 시작 숫자와 부호 변경
    n = n + 2
    sign = -sign