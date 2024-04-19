# 문풀 1번
import random

msg = ["aba", "xyz", "abc", "121"]

cnt = 0
for m in msg:
    if m[0] == m[len(m) - 1]:
        cnt += 1

print(f"같은 문자열 개수 = {cnt}")
