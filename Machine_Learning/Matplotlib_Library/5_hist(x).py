import matplotlib.pyplot as plt
import numpy as np

# 사용 데이터 설정
x = 4 + np.random.normal(0, 1.5, 200)

# 방법1
plt.hist(x, bins=8, linewidth=0.5, edgecolor="white")

# 방법2
fig, ax = plt.subplots()
ax.hist(x, bins=8, linewidth=0.5, edgecolor="white")

plt.show()