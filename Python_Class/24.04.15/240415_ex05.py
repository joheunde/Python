# 지뢰 찾기 프로그램

# 지뢰 모양
shape_mine = [['-', '*', '-', '-', '-'],
              ['-', '-', '-', '*', '-'],
              ['-', '*', '-', '-', '-'],
              ['-', '-', '-', '-', '-']]

# 인접한 지뢰의 개수를 위한 count 변수
count = 0

# 지뢰 찾기 결과를 저장할 result_mine 배열
result_mine = []
for i in range(len(shape_mine)):  # mine 의 행 길이 만큼 반복
    col_mine = []  # 가로 저장 배열
    for j in range(len(shape_mine[i])):  # mine 의 열 길이 만큼 반복
        if shape_mine[i][j] == '*':  # mine[i][j]가 '*'이라면 그대로 출력
            col_mine.append('*')
        elif shape_mine[i][j] == '-':  # mine[i][j]가 '-'일때
            # 자신의 주위를 둘러 싼 요소들에 '*'이 몇개 있는지 구하는 중첩 반복문 코드
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    # 인덱스 범위를 벗어나는지 확인하는 조건문 코드
                    if (0 <= x < len(shape_mine) and 0 <= y < len(shape_mine[i])) and shape_mine[x][y] == '*':
                        count += 1  # '*'이 하나 있으면 count 1 증가
            col_mine.append(count)
            count = 0
    result_mine.append(col_mine)
print(result_mine)
