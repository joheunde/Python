# NumPy 배열 형태 변경

import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])

# 배열의 형태 변경
b = a.reshape((2, 3))  # [[1, 2, 3], [4, 5, 6]]

# 배열 전치
c = a.T  # [[1, 3, 5], [2, 4, 6]]
