# NumPy 배열 인덱싱과 슬라이싱

import numpy as np

a = np.array([1, 2, 3, 4, 5])

# 인덱싱
b = a[0]  # 1
c = a[2]  # 3

# 슬라이싱
d = a[1:4]  # [2, 3, 4]
e = a[:3]   # [1, 2, 3]
f = a[3:]   # [4, 5]


# 다차원 NumPy 배열에서는 각 차원의 인덱스를 콤마로 구분하여 인덱싱할 수 있다.
a1 = np.array([[1, 2, 3], [4, 5, 6]])

# 인덱싱
b1 = a1[0, 0]  # 1
c1 = a1[1, 2]  # 6

# 슬라이싱
d1 = a1[0, 1:3]  # [2, 3]
e2 = a1[:, 1]    # [2, 5]
f3 = a1[:, :2]   # [[1, 2], [4, 5]]
