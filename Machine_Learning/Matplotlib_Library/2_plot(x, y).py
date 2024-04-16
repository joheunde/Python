import matplotlib.pyplot as plt
import numpy as np

# 사용 데이터 설정
x = np.linspace(0, 10, 100)
y = 4 + 2 * np.sin(2 * x)

# 방법1
plt.plot(x, y)

# 방법2
fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2.0)

plt.show()