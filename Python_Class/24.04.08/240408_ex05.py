# 슬라이싱(Slicing)에 대한 내용

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# [시작 인덱스 : 끝 인덱스] => 시작 인덱스 ~ (끝 인덱스 - 1)까지의 값을 복사
new_list1 = my_list[2:7]
print(new_list1)
new_list2 = my_list[5:6]
print(new_list2)
new_list3 = my_list[5:5]
print(new_list3)

# 시작 인덱스를 생략하면 인덱스 0부터 끝 인덱스 -1 까지
new_list4 = my_list[:5]
print(new_list4)

# 끝 인덱스를 생략하면 시작 인덱스부터 리스트 끝까지
new_list5 = my_list[5:]
print(new_list5)

# 시작 인덱스와 끝 인덱스는 둘다 생략할 수 있음
# 복사체(copy)가 만들어진다고 볼 수 있음
# 원본과 복사체가 서로 영향을 주지 않는 하드카피(Hardcopy)
new_list6 = my_list[:]
print(new_list6)
