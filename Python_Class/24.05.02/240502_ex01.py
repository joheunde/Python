# 함수 : 입력값(파라미터)을 받아 지정한 처리 결과를 계산하고
#        계산된 결과를 반환하는 것
#
# def 함수이름(파라미터1, 파라미터2, ...):
#     처리코드
#     ... 생략
#     return 반환값

# 1. 가장 기본적인 함수(입력 X, 출력 X)
def my_func1():
    print("my_func1 호출")


my_func1()


# 2. 입력값이 1개 있는 경우
def my_func2(a):
    print(f"my_func2 호출 : {a}")


my_func2(10)


# 3. 입력값이 여러개 있는 경우
def my_func3(num1, num2, num3):
    res = num1 + num2 - num3
    print(f"my_func3 호출 : {res}")


my_func3(20, 10, 5)


# 4. 반환값이 1개 있는 경우
def my_func4(num1, num2, num3):
    res = num1 + num2 - num3
    print(f"my_func4 호출 : {res}")

    return res


my_func4(20, 5, 3)  # 반드시 변수에 담을 필요 X
v4 = my_func4(10, 5, 3)
print(f"v4 : {v4}")


# 5. 반환값이 2개 이상인 경우
def my_func5(num1, num2):
    mul = num1 * num2
    div = num1 / num2
    print(f"두 수의 곲 : {mul}, 나눗셈 : {div}")
    return mul, div


r1, r2 = my_func5(3, 5)
print(f"my_func5 결과 : {r1}, {r2}")


# 모든 프로그래밍 언어에서 함수는 값을 하나밖에 반환하지 못한다.