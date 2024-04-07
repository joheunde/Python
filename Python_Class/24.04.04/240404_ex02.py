# 홀수 합 구하는 코드

hap = 0

for i in range(1001, 2000):
    if i % 2 == 1:
        hap = hap + i
print(f"1000부터 2000까지의 홀수 합 : {hap}")