import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
df['F'] = s1

df.loc[dates[0], 'A'] = 0

df.iloc[0, 1] = 0

df.loc[:, 'D'] = np.array([5] * len(df))
print(df)

# 4. 결측 데이터
# 여러가지 이유로 우리는 데이터를 전부 다 측정하지 못하는 경우가 종종 발생한다.
# 이처럼 측정되지 못하여 비어있는 데이터를 '결측치'라고 한다. Pandas에서는 결측치를 np.nan으로 나타낸다.
# Pandas에서는 결측치를 기본적으로 연산에서 제외시키고 있다.
# 또한 머신러닝, 딥러닝의 경우 결측치가 존재한다며, 코드가 오류나는 경우도 존재하기 때문에 항상 데이터 분석을 하기 전에는 결측치를 확인하는 습관을 가지는게 중요하다.
# reindex()을 통해 컬럼이나 인덱스를 추가, 삭제, 변경 등의 작업이 가능하다. 결측 데이터를 만들기 위해 'E'컬럼을 생성한다.

df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1], 'E'] = 1

print(df1)
#                    A         B         C    D    F    E
# 2013-01-01  0.000000  0.000000  1.117891  5.0  NaN  1.0
# 2013-01-02 -0.749807 -1.891689  0.947268  5.0  1.0  1.0
# 2013-01-03 -3.087154 -2.400108  1.320403  5.0  2.0  NaN
# 2013-01-04 -1.258088  1.294294 -0.341636  5.0  3.0  NaN


# drop() 함수
# DataFrame의 dropna()를 통해 결측데이터를 삭제(drop)할 수 있다.
# how='any'는 값들 중 하나라도 NaN인 경우 삭제, how='all'은 전체가 NaN인 경우 삭제
# axis=0 일 경우 NaN값이 있는 행 기준으로 삭제, axis=1 일 경우 열 기준으로 삭제

print(df1.dropna(how="any"))
#                    A         B         C  D    F    E
# 2013-01-02 -1.037697 -0.891196  0.495447  5  1.0  1.0


# 결측 데이터 채우기
# DataFrame의 fillna()를 통해 결측데이터에 값을 넣을 수도 있다.
# 결측치가 있다면 머신러닝 알고리즘이 학습과 예측을 할 수 없다.
# 평균, 중앙, 최빈값 등으로 채우기도 하며 그룹화된 값으로 대표값을 찾아 대체해 주기도 한다.
# 결측치가 일부라면 제거하기도 한다.
# 혹은, 머신러닝을 통해 예측해서 대체하기도 합니다.

print(df1.fillna(value=5))
#                    A         B         C    D    F    E
# 2013-01-01  0.000000  0.000000 -1.131197  5.0  5.0  1.0
# 2013-01-02  0.937335 -0.156859 -0.591040  5.0  1.0  1.0
# 2013-01-03 -0.396436 -0.736438 -0.712878  5.0  2.0  5.0
# 2013-01-04  1.047553  0.773794  0.704929  5.0  3.0  5.0

# 해당 값이 결측치인지 아닌지의 여부를 알고싶다면 isna() 메소드를 이용하면 된다.
# 결측치이면 True, 값이 있다면 False로 나타난다.
# 결측치의 전체 합계를 알고 싶다면 .isna()뒤에 .sum() 함수를 활용할 수 있다.

print(pd.isna(df1))
#                 A      B      C      D      F      E
# 2013-01-01  False  False  False  False   True  False
# 2013-01-02  False  False  False  False  False  False
# 2013-01-03  False  False  False  False  False   True
# 2013-01-04  False  False  False  False  False   True