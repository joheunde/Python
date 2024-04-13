# NumPy 주요 함수
# NumPy는 배열의 계산과 관련된 다양한 함수를 제공한다.
# 이 중에서 가장 많이 사용되는 함수들은 다음과 같습니다.

# np.zeros(): 모든 원소가 0인 배열을 생성합니다.
# np.ones(): 모든 원소가 1인 배열을 생성합니다.
# np.arange(): 범위 내의 일정 간격을 가진 배열을 생성합니다.
# np.linspace(): 범위 내에서 균등 간격으로 원하는 개수의 배열을 생성합니다.
# np.random.random(): 0부터 1사이의 난수를 가지는 배열을 생성합니다.
# np.random.randn(): 평균이 0이고 표준편차가 1인 정규 분포를 따르는 난수를 가지는 배열을 생성합니다.

# 이 외에도 np.sin(), np.cos(), np.exp(), np.log() 등 이러한 함수들은 NumPy 배열에서 사용되어 배열의 원소들을 계산합니다.

import numpy as np

# np.zeros() 함수는 모든 원소가 0인 배열을 생성합니다. 함수 인수로는 생성할 배열의 크기를 지정한다.
arr1 = np.zeros((2, 3))
print(arr1)
print()

# np.ones() 함수는 모든 원소가 1인 배열을 생성합니다.
arr2 = np.ones((2, 4))
print(arr2)
print()

# np.arange() 함수는 범위 내의 일정 간격을 가진 배열을 생성합니다. 함수의 인수로는 생성할 배열의 범위와 간격을 지정한다.
arr3 = np.arange(1, 10, 2)
print(arr3)
print()

# np.linspace() 함수는 범위 내에서 균등 간격으로 원하는 개수의 배열을 생성한다.
arr4 = np.linspace(0, 1, 5)
print(arr4)
print()

# np.random.random() 함수는 0과 1사이의 균등 분포에서 난수를 생성하여 배열을 만든다.
arr5 = np.random.random((3, 3))
print(arr5)
print()

# np.random.randn() 함수는 평균이 0이고 표준편차가 1인 정규 분포를 따르는 난수를 생성하여 배열을 만든다.
arr6 = np.random.randn(2, 4)
print(arr6)
print()


# NumPy 기타 함수

# NumPy 수학 함수
# sum(), mean(): 배열 전체 합, 평균
# cumsum(), cumprod(): 배열 누적 합, 누적 합
# std(), var(): 표준편차, 분산
# min(), max(): 최솟값, 최댓값
# argmin(), argmax(): 최소 원소의 색인 값, 최대 원소의 색인 값


# NumPy 난수 함수
# NumPy 모듈의 랜덤 함수를 사용하여 다양한 분포에서 난수를 생성할 수 있다.
# 이를 통해 데이터의 모의 실험을 수행하거나 시뮬레이션을 구현할 수 있습니다.
# seed(): 난수 발생기의 seed를 지정한다.
# permutation(): 임의의 순열을 반환한다.
# shuffle(): 리스트나 배열의 순서를 뒤섞는다.
# rand(): 균등분포에서 표본을 추출한다.
# randint(): 주어진 최소/최대 범위 안에서 임의의 난수를 추출한다.
# randn(): 표준편차가 1이고 평균값이 0인 정규분포에서 표본을 추출한다.
# binomial(): 이항분포에서 표본을 추출한다.
# normal(): 정규분포(가우시안)에서 표본을 추출한다.
# beta(): 베타분포에서 표본을 추출한다.
# chisquare(): 카이제곱분포에서 표본을 추출한다.
# gamma(): 감마분포에서 표본을 추출한다.
# uniform(): 균등(0, 1)에서 표본을 추출한다.
