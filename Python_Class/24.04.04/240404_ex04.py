# 구구단 프로그램

for i in range(2, 10):
    if i % 2 == 1:
        continue
    print(f"===== {i}단 =====")
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}")