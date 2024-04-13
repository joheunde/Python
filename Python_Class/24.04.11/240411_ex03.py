# 정렬 (sort) - 리스트의 함수
numList = [20, 40, 1, 12, 55]
numList.sort()
print(numList)
numList.sort(reverse=True)
print(numList)

# 정렬 (sorted) - 파이썬의 기본함수
numList = [20, 40, 1, 12, 55]
numList2 = sorted(numList)
print(numList)
print(numList2)

# 문자열도 사전순으로 정렬 가능
strList = ["다람쥐", "가구", "나비", "악어", "사자"]
strList.sort()
print(strList)

# 리스트를 역순으로 만들기
numList = [10, 20, 30]
numList = numList[::-1]  # 슬라이싱을 이용한 역순 만드는 코드
print(numList)

# 리스트 복사
numList = [10, 20, 30]
numList2 = numList  # 얕은 복사(Swallow Copy) : 두 변수가 같은 객체
numList2 = numList.copy()  # 깊은 복사(Deep Copy, Hard Copy) : 두 변수가 독립적
numList2[1] = 200
print(f"numList : {numList}")
print(f"numList2 : {numList2}")