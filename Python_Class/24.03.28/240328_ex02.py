# 팩토리얼(factorial) 계산기

N = int(input("N을 입력 => "))

# N! 값 계산
fac = 1
for n in range(1, N + 1):
    fac *= n

# 출력 코드
print(f"{N}!은 ", end='')
for i in range(1, N):
    print(f"{i}", end=' * ')
print(f"{N} = {fac}입니다.")
