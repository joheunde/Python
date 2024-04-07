# for 반복문
# for (변수) in (순서가 있는 데이터)
# {순서가 있는 데이터}에서 데이터를 하나씩 변수에 대입해서 사용한다

# 예시 1. 기본형
for n in [1, 2, 3]:
    print(n)

# 예시 2. 순서가 있는 데이터의 변경
for n in [59, 22, 11, 32]:
    print(n)

# 예시 3. 변수명을 변경
for std_no in [59, 22, 11, 32]:
    print(f"학번 : {std_no}")

# 예시 4. 파이썬에서 for문은 가져와야 하는 데이터의 개수에 따라 반복 횟수가 결정됨
for std_no in [1, 2, 3, 4, 5, 6, 7]:
    print("안녕하세요 ^^")

# 예시 5. range 객체를 이용해 반복 횟수 제어
#        range({시작값}, 끝값, {증감값})
#        range(끝값) ==> 0부터 (끝값 - 1) 까지의 숫자를 생성
#        range(시작값, 끝값) ==> 시작값부터 (끝값 - 1) 까지의 숫자를 생성
#        range(시작값, 끝값, 증감값) ==> 시작값부터 증감값을 더하면서 (끝값 - 1)을 넘어서지 않는 숫자를 생성
for n in range(1, 10, 2):
    print(n, end=' ')

# 예시 6. 가져온 데이터가 반복문의 실행과 연관이 없을때
for _ in range(5):              # 언더바(_)는 와일드카드(wildcard)/ 버린다는 뜻
    print("다섯번 반복~")

# 예시 7. "순서가 있는 데이터"는 모두 사용가능하다
msg = "AABACDEF"
a_count = 0
for c in msg:
    if c == 'A':
        a_count += 1
print(f"A의 개수 : {a_count}")

for n in range(1, 11):
    print(n, end=' ')

# range는 순서가 있는 데이터형이므로 다른 비슷한 유형인 list로 변환도 가능함
var1 = range(1, 11)  # 1 ~ 10
my_list = list(var1)
print(my_list)

# 팩토리얼 구하는 프로그램
# 팩토리얼 => 자연수 n이 주어졌을때 1부터 n까지의 곱

n = int(input("n을 입력하시오 => "))
fac = 1

for num in range(1, n + 1):
    fac = fac * num
print(f"{n}!은 ", end='')
for i in range(1, n):
    print(f"{i}", end=' * ')
print(f"{n}은 {fac}입니다.")