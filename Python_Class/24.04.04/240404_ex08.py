print("3", end='')

check = 1
n1 = 2
n2 = 3
n3 = 4
i = 0
while i < 10:
    if check == 1:
        print(" + ", end='')
        print(f"4 / ({n1} x {n2} x {n3})", end='')
        check -= 1
    elif check == 0:
        print(" - ", end='')
        print(f"4 / ({n1} x {n2} x {n3})", end='')
        check += 1
    n1 += 2
    n2 += 2
    n3 += 2
    i += 1
