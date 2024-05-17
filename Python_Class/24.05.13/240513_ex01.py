people = [
    {"name": "Eva", "age": 40, "job": "Engineer", "city": "Chicago"},
    {"name": "Alice", "age": 25, "job": "Engineer", "city": "New York"},
    {"name": "Bob", "age": 30, "job": "Doctor", "city": "San Francisco"},
    {"name": "Charlie", "age": 35, "job": "Teacher", "city": "Los Angeles"},
    {"name": "David", "age": 28, "job": "Designer", "city": "New York"}
]
sort_key_list = []


def filter_and_sort(people, sort_key, filter_key, filter_value):
    res_list = []
    for p in people:
        if p[filter_key] == filter_value:
            sort_key_list.append(p[sort_key])

    # 데이터를 정렬하는 코드
    sort_key_list.sort()
    for i in sort_key_list:
        for j in range(len(people)):
            if people[j][sort_key] == i:
                res_list.append(people[j])

    return res_list


result = filter_and_sort(people, "age", "job", "Engineer")
print(result)


# 교수님 풀이
def filter_and_sort(people, sort_key, filter_key, filter_value):
    filtered = [p for p in people if p[filter_key] == filter_value]
    # x는 정렬하기 위해 가져온 filtered의 item
    filtered = sorted(filtered, key=lambda x: x[sort_key])
    return filtered


result = filter_and_sort(people, "age", "job", "Engineer")
print(result)
