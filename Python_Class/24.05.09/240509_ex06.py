# 지역변수와 전역변수
# local variable, global variable

# 종속코드는 부모(조상)코드에서 선언된 변수에 접근이 가능
# (+) 함수는 종속코드로 간주
a = 10
b = 20
c = 20

def my_func():
    c = 10
    print(c)

print(c)
my_func()
