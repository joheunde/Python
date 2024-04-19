# 문풀 2번
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 7, 8, 9, 10]

same_number = False

for n1 in list1:
    if n1 in list2:  # if 변수 in 리스트 => 변수가 리스트에 있는지?
        same_number = True

    if same_number:
        break

print(same_number)
