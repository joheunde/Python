def my_func():
    a = 100
    c = 10
    def my_func2(v):
        b = 10
        print(c)
        return a + v
    print(b)
    print(my_func2(30))

my_func()