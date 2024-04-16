# NumPy 배열 연산(operation)
# NumPy 배열은 다른 배열 또는 스칼라와의 연산을 지원한다.

import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# 원소별 덧셈
c = a + b  # [5, 7, 9]

# 원소별 곱셈
d = a * b  # [4, 10, 18]

# 스칼라와의 연산
e = a + 1  # [2, 3, 4]

# NumPy 배열의 연산에는 다양한 함수와 메소드가 있다.
# 가장 기본적인 연산은 sum, mean, min, max가 있다.
# 합계
f = np.sum(a)  # 6

# 평균
g = np.mean(a)  # 2.0

# 최솟값
h = np.min(a)  # 1

# 최댓값
i = np.max(a)  # 3

