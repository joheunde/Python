import matplotlib.pyplot as plt
import numpy as np

# 사용 데이터 설정
x = 0.5 + np.arange(8)
y = np.random.uniform(2, 7, len(x))

# 방법1
plt.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

# 방법2
fig, ax = plt.subplots()
ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

plt.show()