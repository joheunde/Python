# Matplotlib 활용
# Matplotlib 란?
# 파이썬에서 데이터를 시각화해주는 라이브러리이다.
# 간단한 plot(바 차트, 파이차트, 히스토그램 등)을 그릴 수 있다.

# Matplotlib 사용 방법
# matplotlib을 사용하기 위해서 다음과 같이 모듈을 import한다.
# 임포트를 할 때에는 plt라는 축약된 이름을 관례적으로 많이 사용한다.
# import matplotlib.pyplot as plt


# Matplotlib을 활용해서 그림을 그리는 방법은 여러가지가 있다.
# 그 중에서 간단하게 쓸 수 있는 pyplot API와 객체지향 API가 있다.

# 1. Pyplot API를 이용
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, 50)
y1 = np.cos(4*np.pi*x)
y2 = np.cos(4*np.pi*x)*np.exp(-2*x)

plt.plot(x, y1, "r-*", lw=1)
plt.plot(x, y2, "b--", lw=1)
plt.show()

# 2. 객체지향 API를 이용
x = np.linspace(0, 1, 50)
y1 = np.cos(4*np.pi*x)
y2 = np.cos(4*np.pi*x)*np.exp(-2*x)

# Figure 객체를 생성 후 직접 axes를 생성
fig = plt.figure()
ax = fig.subplots()
ax.plot(x, y1, 'r-*', lw=1)
ax.plot(x, y2, 'b--', lw=1)
plt.show()
