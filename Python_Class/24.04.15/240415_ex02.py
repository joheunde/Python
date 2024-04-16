M = int(input())
List1 = []
for i in range(M):
    List2 = []
    for j in range(M):
        value = int(input())
        List2.append(value)
    List1.append(List2)
print(List1[0][0] + List1[1][1] + List1[2][2])
print(List1[0][2] + List1[1][1] + List1[2][0])

# 교수님 풀이
numList = [[11, -2, 4],
           [4, 5, 6],
           [10, -12, 9]]

# hap1 = numList[0][0] + numList[1][1] + numList[2][2]
hap1 = 0
for i in range(len(numList)):  # len(numList) == N
    hap1 += numList[i][i]

# hap2 = numList[2][0] + numList[1][1] + numList[0][2]
hap2 = 0
for i in range(len(numList)):
    hap2 += numList[len(numList)-1-i][i]

print(f"주대각선 합 : {hap1}")
print(f"부대각선 합 : {hap2}")