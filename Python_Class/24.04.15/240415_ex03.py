# 튜플
t1 = 10,
print(t1)

t2 = 10, 20
print(t2)

# 읽기 전용인 튜플
# 아래는 모두 오류가 발생함
# numTup1.append(40)
# numTup1[0] = 40
# del(numTup1[0])

# 튜플 자체를 통째로 삭제하려면 del(튜플이름) 함수를 사용함
# del(numTup1)
# del(numTup2)

for n in t2:
    print(n)