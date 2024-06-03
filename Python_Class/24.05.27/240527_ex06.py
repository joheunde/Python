def solution(price, money, count):
    cost = sum([price * x for x in range(1, count + 1)])
    return max(0, cost - money)


fp = open("input.txt", 'r', encoding="UTF-8")
inputs = fp.readlines()
fp.close()

outfp = open("output.txt", 'w', encoding="UTF-8")
for line in inputs:
    params = line.strip()
    params = params.split()
    params = list(map(int, params))
    p, m, c = params

    # 함수 실행
    result = solution(p, m, c)

    # 결과를 파일에 작성
    outfp.write(f"{result}\n")
    fp.close()