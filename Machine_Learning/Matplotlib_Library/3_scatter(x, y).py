import matplotlib.pyplot as plt
import numpy as np

# 사용 데이터 설정
x = 4 + np.random.normal(0, 2, 24)
y = 4 + np.random.normal(0, 2, len(x))

# size and color:
sizes = np.random.normal(15, 80, len(x))
colors = np.random.uniform(15, 80, len(x))

# 방법1
plt.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

# 방법2
fig, ax = plt.subplots()
ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)

plt.show()
