import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
df['F'] = s1

df.loc[dates[0], 'A'] = 0

df.iloc[0, 1] = 0

df.loc[:, 'D'] = np.array([5] * len(df))

# 5. 연산
# 통계적 지표가 계산이 가능하다.
# 평균 구하기
# axis = 1 : 인덱스 기준
# axis = 0 : 컬럼 기준(default)

print(df.mean())
# A   -0.758417
# B    0.083843
# C   -0.213732
# D    5.000000
# F    3.000000
# dtype: float64

print(df.mean(1))
# 2013-01-01    1.038711
# 2013-01-02    0.850322
# 2013-01-03    1.374396
# 2013-01-04    1.495042
# 2013-01-05    1.804990
# 2013-01-06    2.134259
# Freq: D, dtype: float64

# 함수 적용
# 데이터에 대해 정의된 함수들이나 lambda 식을 이용하여 새로운 함수도 적용할 수 있다.
print(df.apply(np.cumsum))
#                    A         B         C     D     F
# 2013-01-01  0.000000  0.000000  0.502662   5.0   NaN
# 2013-01-02  0.140286 -0.746373  1.816339  10.0   1.0
# 2013-01-03  0.825133 -0.250533  1.352513  15.0   3.0
# 2013-01-04  0.763821 -0.772605 -0.633721  20.0   6.0
# 2013-01-05  1.345242  0.632093 -1.822576  25.0  10.0
# 2013-01-06  0.819004  1.931928 -2.521621  30.0  15.0

print(df.apply(lambda x: x.max() - x.min()))
# A    2.623644
# B    1.735648
# C    1.317290
# D    0.000000
# F    4.000000
# dtype: float64
