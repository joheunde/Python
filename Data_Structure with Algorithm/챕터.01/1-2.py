# 세 정수의 최댓값 구하기

def max3(a, b, c):
    maximum = a
    if b > maximum:
        maximum = b
    if c > maximum:
        maximum = c
    return maximum # 최댓값 반환

print(f"max3(3, 2, 1) = {max3(3, 2, 1)}") # a > b > c
print(f"max3(3, 2, 2) = {max3(3, 2, 2)}") # a > b = c
print(f"max3(3, 1, 2) = {max3(3, 1, 2)}") # a > c > b
print(f"max3(3, 2, 3) = {max3(3, 2, 3)}") # a = c > b
print(f"max3(2, 1, 3) = {max3(2, 1, 3)}") # c > a > b
print(f"max3(3, 3, 2) = {max3(3, 3, 2)}") # a = b > c
print(f"max3(3, 3, 3) = {max3(3, 3, 3)}") # a = b = c
print(f"max3(2, 2, 3) = {max3(2, 2, 3)}") # c > a = b
print(f"max3(2, 3, 1) = {max3(2, 3, 1)}") # b > a > c
print(f"max3(2, 3, 2) = {max3(2, 3, 2)}") # b > a = c
print(f"max3(1, 3, 2) = {max3(1, 3, 2)}") # b > c > a
print(f"max3(2, 3, 3) = {max3(2, 3, 3)}") # b = c > a
print(f"max3(1, 2, 3) = {max3(2, 3, 3)}") # c > b > a