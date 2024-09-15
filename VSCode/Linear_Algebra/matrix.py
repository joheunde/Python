import numpy as np


def E1(i, j):
    t = matrix[i].copy()
    matrix[i] = matrix[j].copy()
    matrix[j] = t


def E2(i, c):
    if c != 0:
        matrix[i] *= c


def E3(i, j, c):
    if c != 0:
        t = matrix[i].copy()
        t *= c
        matrix[j] = matrix[j] + t


r = 0
c = 0
matrix = []

with open("/home/ckswns/Desktop/VSCode/Linear_Algebra/input.txt", 'r') as fin:
    str = fin.readline()
    r, c = map(int, str.split())
    print(r, c)
    for i in range(r):
        str = fin.readline()
        t = list(map(float, str.split()))
        matrix.append(t)
matrix = np.array(matrix)
print("Input\n", matrix)

pivot = 0  # 초기 피벗 열을 0으로 설정
for i in range(r):  # 행(row)에 대해 반복
    while matrix[i, pivot] == 0:  # 피벗이 0이면
        col_zero = True  # 열이 모두 0인지 확인하기 위한 플래그
        for j in range(i+1, r):  # 현재 행 아래의 행들을 검사
            if matrix[j, pivot] != 0:  # 피벗 열에서 0이 아닌 값이 있는 행을 찾음
                E1(i, j)  # 현재 행(i)과 찾은 행(j)을 교환 (E1 연산)
                col_zero = False  # 0이 아닌 값이 있으므로 False로 설정
                break  # 행을 찾았으므로 종료
        if col_zero:  # 열이 모두 0이라면
            pivot += 1
            if pivot > c-1:
                break
    if matrix[i, pivot] != 0:  # 피벗이 0이 아니면
        E2(i, 1 / matrix[i, pivot])  # 현재 행을 피벗 값으로 나눠서 피벗을 1로 만듦 (E2 연산)
    for j in range(i+1, r):  # 현재 피벗 아래의 모든 행에 대해
        if matrix[j, pivot] != 0:  # 피벗이 있는 열에서 0이 아닌 값을 찾음
            E3(i, j, -matrix[j, pivot])  # 현재 행을 사용해 해당 행의 피벗 열을 0으로 만듦 (E3 연산)

# 위 단계가 끝나면, 역방향으로 이동하며 위쪽의 행들에서 피벗 열을 0으로 만듦
for i in range(r-1, -1, -1):  # 아래에서 위로 거꾸로 반복
    for j in range(c):  # 현재 행에서 피벗을 찾음
        if matrix[i, j] == 1:  # 1인 피벗을 찾으면
            pivot = j  # 피벗 열을 j로 설정
            break
    if pivot != -1:  # 피벗을 찾았다면
        for j in range(i-1, -1, -1):  # 현재 행 위의 모든 행에 대해
            if matrix[i, pivot] == 1:  # 피벗이 1인 열에서
                E3(i, j, -matrix[j, pivot])  # 피벗을 0으로 만듦 (E3 연산)

print("OUTPUT\n", matrix)
zero_cnt = 0
if r == c:
    for rows in range(r):
        for cols in range(c):
            if matrix[rows][cols] == 0:
                zero_cnt += 1
        if zero_cnt == c:
            print("have not inverse")
            break
        zero_cnt = 0
    else:
        for rows in range(r):
            print(matrix[rows][c], end=' ')
