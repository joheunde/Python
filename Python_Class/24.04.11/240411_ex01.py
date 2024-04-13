# 특정 위치의 값 변경

numList = [10, 20, 30]
numList[1] = 200
print(numList)

# 2. 일정 범위의 값 변경 (슬라이싱 이용)
numList = [10, 20, 30]
numList[1:2] = [200, 201]
print(numList)
print(f"numList의 길이 : {len(numList)}")

numList = [10, 20, 30]
numList[1] = [200, 201]
print(numList)
print(f"numList의 길이 : {len(numList)}")