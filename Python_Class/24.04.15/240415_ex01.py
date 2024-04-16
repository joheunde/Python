numList1 = [10, 20, 30]
numList2 = [40, 50, 60]
numList3 = [70, 80, 90]

numList4 = [numList1, numList2, numList3]

# 2차원 리스트 전체
print(numList4)

# 2차원 리스트의 요소 == 1차원 리스트
print(numList4[1])

# 2차원 리스트의 요소의 요소 == 값
print(numList4[1][2])

for n1 in numList4:  # n1은 numList4가 가진 1차원 리스트
    for n2 in n1:    # n2는 n1(1차원 리스트)의 값
        print(n2, end=' ')