# *를 n개 출력하되 w개마다 줄바꿈하기 2

print("*를 출력합니다.")
n = int(input("몇 개를 출력할까요?: "))
w = int(input("몇 개마다 줄바꿈할까요?: "))

for _ in range(n // w): # n // w번 반복
    print("*" * w)

rest = n % w
if rest: # if문 판단 1번
    print("*" * rest)