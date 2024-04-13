# 숫자 4개 입력 받은 후 합 계산

numList = [0] * 4
hap = 0

# 리스트의 모든 데이터를 '인덱스를 이용해 순차적으로 접근'할 때엔
# range(len(리스트))를 많이 사용함
for i in range(len(numList)):
    numList[i] = int(input("숫자 : "))
    hap += numList[i]

print("합계 ==> ", hap)