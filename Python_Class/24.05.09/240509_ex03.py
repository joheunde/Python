# List Comprehension
# 리스트를 만드는 방법 중 하나

# 빈 리스트를 만들고
# 특정 규칙에 따라 결정되는 값으로
# 리스트를 채워야하는 작업에 대해서 사용
# 보통은 for문을 이용해서 리스트를 만드는 경우에 사용하는 문법

# 예) 3의 배수를 8개 갖는 리스트 선언
my_list = []
for x in range(1, 9):
    my_list.append(x * 3)
print(my_list)

my_list = [x * 3 for x in range(1, 9)]
print(my_list)