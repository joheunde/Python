def p2_func(v1, v2):
    print(v1, v2)


# 함수 파라미터에 기본값을 설정할 수 있음
# 기본값 => 값이 지정되지 않았을 때 사용할 값
def hap_func(v1, v2, v3 = 5, v4 = 0, v5 = 0, v6 = 0):
    print(f"{v1}, {v2}, {v3}")
    print(v1 + v2 + v3 + v4 + v5 + v6)


hap_func(1, 2, 3, 4, 5, 6)


def hap2(list_num):
    print(f"hap2 : {sum(list_num)}")


hap2([1, 2, 3])
hap2([1, 2, 3, 4, 5])
hap2([1, 2, 3, 4, 5, 6, 7])


def hap3(*nums):
    print(nums)
    print(type(nums))


hap3(1, 2)
hap3(1, 2, 3, 4, 5)


def hap4(v1, v2, *nums1):
    print(nums1)
    print(type(nums1))


hap4(1, 2, 3, 4, 5, 6, 7)


# 기본값이 있는 파라미터는 없는 파라미터보다 뒤에 작성되어야 한다
def p_func4(v1, v3, v2=5):
    print(sum(v1, v2, v3))


p_func4(1, 2, 3)
p_func4(v1=1, v2=2, v3=3)  # 각 값을 어떤 파라미터에 대입할지 직접 지정
