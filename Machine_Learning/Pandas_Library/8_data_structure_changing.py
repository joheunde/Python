import numpy as np
import pandas as pd

df = pd.DataFrame({'A': ['one', 'one', 'two', 'three'] * 3,
                   'B': ['A', 'B', 'C'] * 4,
                   'C': ['foo', 'foo', 'foo', 'bar', 'bar', 'bar'] * 2,
                   'D': np.random.randn(12),
                   'E': np.random.randn(12)})
#         A  B    C         D         E
# 0     one  A  foo  0.901210  0.022981
# 1     one  B  foo  0.506667  0.412898
# 2     two  C  foo  0.570906 -0.721961
# 3   three  A  bar  0.057111  0.002261
# 4     one  B  bar -0.271681 -0.903043
# 5     one  C  bar  1.246075 -0.702314
# 6     two  A  foo -1.362536 -0.026226
# 7   three  B  foo  0.782929 -0.611992
# 8     one  C  foo -0.403011  0.214893
# 9     one  A  bar -0.275153 -2.420672
# 10    two  B  bar -1.042478  0.806450
# 11  three  C  bar  1.983919  0.511828


# 피벗 테이블이란?
# 피벗 테이블(pivot table)은 커다란 표(예: 데이터베이스, 스프레드시트, 비즈니스 인텔리전스 프로그램 등)의 데이터를 요약하는 통계표이다.
# 이 요약에는 합계, 평균, 기타 통계가 포함될 수 있으며 피벗 테이블이 이들을 함께 의미있는 방식으로 묶어준다.

pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
# C             bar       foo
# A     B
# one   A  0.493158 -1.750538
#       B  1.321859  0.373596
#       C -0.371116  1.108912
# three A  0.300844       NaN
#       B       NaN  0.105908
#       C -1.294059       NaN
# two   A       NaN  0.793230
#       B -0.629011       NaN
#       C       NaN  2.404901
