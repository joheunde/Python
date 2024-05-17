a = 10


def a_changer():  # 변수 a의 값을 30으로 변경하는 함수
    global a
    a = 30
    print(f"a의 값 : {a}")


a_changer()
print(a)
