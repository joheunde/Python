# 세 정수의 최댓값 구하기
# 실습 1-1은 3개의 정숫값을 비교하여 최댓값을 구하는 프로그램입니다.
# a,b,c에 정숫값을 입력받아 maximum으로 최댓값을 찾을 수 있습니다.

# 세 정수를 입력받아 최댓값 구하기

print("세 정수의 최댓값을 구합니다.")
a = int(input("정수 a의 값을 입력하세요.: "))
b = int(input("정수 b의 값을 입력하세요.: "))
c = int(input("정수 c의 값을 입력하세요.: "))

maximum = a      # maximum에 a의 값을 대입
if b > maximum:  # b의 값이 maximum보다 크면, maximum에 b의 값을 대입
    maximum = b
if c > maximum:  # c의 값이 maximum보다 크면, maximum에 c의 값을 대입
    maximum = c

print(f"최댓값은 {maximum}입니다.")