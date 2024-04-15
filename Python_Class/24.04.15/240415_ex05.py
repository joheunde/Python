# 지뢰 찾기 프로그램

# 지뢰 모양
mine = [['*', '-', '-', '-'],
        ['-', '-', '*', '-'],
        ['-', '-', '-', '-'],
        ['*', '-', '-', '*']]

# 인접한 지뢰의 개수를 구하기 위한 count 변수
count = 0

print('[', end='')
for i in range(len(mine)):  # mine 의 행 길이 만큼 반복
    print('[', end='')
    for j in range(len(mine[0])):  # mine 의 열 길이 만큼 반복
        if mine[i][j] == '*':  # mine[i][j]가 '*'이라면 그대로 출력
            # 열의 마지막 값에는 값 뒤에는 ','를 쓰면 안되기에 따로 조건을 만들어줌
            if j != len(mine[0]) - 1:
                print('*', end=', ')
            else:
                print('*', end='')
        elif mine[i][j] == '-':  # mine[i][j]가 '-'일때
            # 자신의 주위를 둘러 싼 값들에 '*'이 몇개 있는지 구하는 중첩 반복문 코드
            for x in range(i - 1, i + 2):
                for y in range(j - 1, j + 2):
                    # 인덱스 범위를 벗어나는지 확인하는 조건문 코드
                    if (0 <= x < len(mine) and 0 <= y < len(mine[0])) and mine[x][y] == '*':
                        count += 1

            # 열의 마지막 값에는 값 뒤에는 ','를 쓰면 안되기에 따로 조건을 만들어줌
            if j != len(mine[0]) - 1:
                print(count, end=', ')
            else:
                print(count, end='')
            count = 0

    # 마지막 행에는 ']'뒤에 ','를 빼주는 조건문 코드
    if i != len(mine) - 1:
        print('],')
    else:
        print(']', end='')
print(']')
