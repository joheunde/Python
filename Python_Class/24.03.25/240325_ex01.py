num = int(input("숫자를 입력 ==> "))

if num > 100:
    if num < 1000:
        print("100보다 크고 1000보다 작군요.")
    else:
        print("와~ 1000보다 크군요.")
else:
    print("음~ 100보다 작군요.")
