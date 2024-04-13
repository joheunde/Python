# 리스트에 값을 추가
# append(값) : 리스트의 제일 뒤에 값을 추가한다.
# insert(인덱스, 값) : 인덱스 위치에 값을 추가하고 기존의 값들은 뒤로 민다.

# 리스트에 있는 값을 삭제
# (1) del을 이용하는 방법
#     del(리스트) 또는 del(리스트[인덱스])
#     del은 List의 함수가 아님. 파이썬의 가본 내장 함수
#     del은 선언되어있는 객체를 삭제하는 기능을 가짐
#     remove는 값을 이용해서 삭제하는 대신
#     del은 인덱스를 이용해서 값을 삭제할 수 있음 <<<
numList = [10, 20, 30]
# del numList
# print(numList)

# (2) remove(값)을 이용하는 방법
#     주의할 점 : 값이 여러개 있으면 제일 앞에 있는 것만 지워짐
numList = [10, 20, 30, 20]
numList.remove(20)
print(f"remove를 이용한 삭제 : {numList}")

for _ in range(numList.count(20)):
    numList.remove(20)
print(f"반복문과 remove를 이용한 삭제 : {numList}")

if 55 in numList:
    numList.remove(55)
print(numList)

print(numList.count(55))