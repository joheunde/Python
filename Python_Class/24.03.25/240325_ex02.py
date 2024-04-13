# 100보다 크다/작다/같다를 구분하는 코드

number = int(input("숫자 ==> "))

if number >= 10:
    if number > 10:
        print("10보다 크네요.")
    else:
        print("10이네요.")
else:
    print("10보다 작네요.")