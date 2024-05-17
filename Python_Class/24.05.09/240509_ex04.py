# 파이썬은 C언어 파생
# 전통적인 언어들은 함수를 정의할 때 반환값의 자료형을 써야함
def my_func():
    print("함수 호출")
    val = int(input("사용자 입력(0이면 종료) : "))

    if val == 0:
        return

    result = val + 5
    return result

