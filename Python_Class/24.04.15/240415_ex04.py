# 딕셔너리
# 키(Key)와 값(Value)의 쌍으로 이루어짐
# 키(Key): 단어, 값(Value): 뜻

# 딕셔너리 생성하기
# 키(Key)가 1, 2, 3이, 값(Value)이 'a', 'b', 'c'인 딕셔너리
myDict1 = {1: 'a', 2: 'b', 3: 'c'}
print(myDict1)

my_dict = {'a': "apple", 1: "일", "이": 2, "my_list": [1, 2, 3]}
print(my_dict)

# 딕셔너리는 순서가 없기 때문에 인덱싱이 불가능하다. 그러므로 for문에도 활용이 불가능하다.

# 값 참조 딕셔너리[키]
print(my_dict['a'])
print(my_dict[1])

# 딕셔너리에 값을 추가 (존재하지 않는 키와 값 쌍을 대입연산자로)
my_dict["오"] = 100
print(my_dict)

# 딕셔너리에 값을 수정 (존재하는 키와 값 쌍을 대입연산자로)
my_dict["오"] = 500

# 딕셔너리의 키는 중복되지 않고 유일함
# 만약 동일한 키를 갖는 딕셔너리를 생성한다면 오류가 발생하지는 않고,
# 마지막에 있는 키의 값이 적용되어 생성됨
empDict = {"사번": 1000, "이름": "홍길동", "사번": 2000}
print(empDict)

print(list(my_dict.keys()))
# 키를 이용한 딕셔너리 출력
for k in my_dict.keys():
    print(my_dict[k])

# values()를 이용한 값 출력
print(list(my_dict.values()))

print(my_dict.items())
for k, v in my_dict.items():
    print(f"key: {k} / value: {v}")