# continue : 종속코드 블럭의 마지막으로 이동

for i in range(5):
    i += 1
    print(i, 1)
    print(i, 2)
    continue
    print(i, 3)
    print(i, 4)