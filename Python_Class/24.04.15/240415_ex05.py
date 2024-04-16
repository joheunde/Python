# 지뢰 찾기 프로그램

# 지뢰 모양
mine = [['-', '*', '-', '-', '-'],
        ['-', '-', '-', '*', '-'],
        ['-', '*', '-', '-', '-'],
        ['-', '-', '-', '-', '-']]

# 인접한 지뢰의 개수를 구하기 위한 count 변수
count = 0

# 지뢰 찾기 결과를 저장할 find_mine 배열
# range(len(mine[0]))으로 mine 의 열 길이 만큼 0으로 초기화
# range(len(mine))으로 mine 의 행 길이 만큼 반복
find_mine = [[0 for col in range(len(mine[0]))] for row in range(len(mine))]

for i in range(len(mine)):  # mine 의 행 길이 만큼 반복
    for j in range(len(mine[0])):  # mine 의 열 길이 만큼 반복
        if mine[i][j] == '*':  # mine[i][j]가 '*'이라면 그대로 출력
            find_mine[i][j] = '*'
        elif mine[i][j] == '-':  # mine[i][j]가 '-'일때
            # 자신의 주위를 둘러 싼 요소들에 '*'이 몇개 있는지 구하는 중첩 반복문 코드
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    # 인덱스 범위를 벗어나는지 확인하는 조건문 코드
                    if (0 <= x < len(mine) and 0 <= y < len(mine[0])) and mine[x][y] == '*':
                        count += 1  # '*'이 하나 있으면 count 1 증가
            find_mine[i][j] = count
            count = 0
print(find_mine)
