import numpy as np
r, c = map(int, input().split())
matrix = []

for i in range(r):
    n = list(map(int, input().split()))
    matrix.append(n)

matrix = np.array(matrix)
print(matrix)


def E1(i, j):
    t = matrix[i].copy()
    matrix[i] = matrix[j].copy()
    matrix[j] = t


def E2(i, s):
    matrix[i] + s


E1(0, 1)
print(matrix)