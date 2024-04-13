# NumPy 배열 생성(create)

import numpy as np

# 1차원 배열 생성
a = np.array([1, 2, 3])

# 2차원 배열 생성
b = np.array([[1, 2, 3], [4, 5, 6]])

# 3차원 배열 생성
c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# NumPy 배열의 크기를 확인하는 방법은 shape 속성을 사용함
print(a.shape)
print(b.shape)
print(c.shape)
