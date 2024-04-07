# for문 vs while문
# for문: 반복할 횟수를 range()에서 결정한 후에, 그 횟수만큼 반복함
# while문: 반복 횟수를 결정하기 보단 참,거짓으로 판별해 반복함

# "난생처음~" 문장을 3번 반복하는 for문
# for _ in range(3):
#     print("난생처음~")

while True:
    num1 = int(input("숫자 1 입력 : "))
    num2 = int(input("숫자 2 입력 : "))
    print(f"{num1} + {num2} = {num1 + num2}")

    # brea는 for, while과 같은 반복문에서만 사용
    # 예외적으로 switch문에서도 사용
    if num1 == 0:
        break