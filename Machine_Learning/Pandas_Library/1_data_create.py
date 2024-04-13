# 판다스(Pandas)는 Python에서 DB처럼 테이블 형식의 데이터를 쉽게 처리할 수 있는 라이브러리
# 데이터가 테이블 형식(DB Table, csv 등)으로 이루어진 경우가 많아 데이터 분석 시 자주 사용하게 될 Python 패키지
import numpy as np
import pandas as pd  # pd라는 축약된 이름을 관례적으로 많이 사용함

# 1. 데이터 오브젝트 생성
# 데이터 오브젝트는 '데이터를 담고 있는 그릇'이라고 생각하면 된다.
# Pandas에서는 2가지 오브젝트 Series와 DataFrame이 있다.
# Seires: 1차원 데이터와 각 데이터의 위치정보를 담는 인덱스로 구성
# DataFrame: 2차원 데이터와 인덱스, 컬럼으로 구성(하나의 컬럼만 선택한다면 Series)

# Series 생성
# Series() 안에 list로 1차원 데이터만 넘기면 됨. index는 입력하지 않아도 자동으로 0부터 입력된다.
s = pd.Series([1, 3, 5, np.nan, 6, 8])
# 0    1.0
# 1    3.0
# 2    5.0
# 3    NaN
# 4    6.0
# 5    8.0
# dtype: float64

# DataFrame 생성
dates = pd.date_range("20130101", periods=6)
# DatetimeIndex(['2013-01-01', '2013-01-02', '2013-01-03', '2013-01-04',
#                '2013-01-05', '2013-01-06'],
#               dtype='datetime64[ns]', freq='D')

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)
#                    A         B         C         D
# 2013-01-01  1.571507  0.160021 -0.015071 -0.118588
# 2013-01-02 -1.037697 -0.891196  0.495447  0.453095
# 2013-01-03 -1.682384 -0.026006 -0.152957 -0.212614
# 2013-01-04 -0.108757 -0.958267  0.407331  0.187037
# 2013-01-05  1.092380  2.841777 -0.125714 -0.760722
# 2013-01-06  1.638509 -0.601126 -1.043931 -1.330950

# Pandas의 경우 리스트 이외에 딕셔너리 형식으로도 DataFrame을 만들 수 있다.
# dict의 key값이 열을 정의하는 컬럼이 되며, 행을 정의하는 인덱스는 자동으로 0부터 시작하여 1씩 증가하는 정수 인덱스가 사용된다.
df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp("20130102"),
                    'C': pd.Series(1, index=list(range(4)), dtype="float32"),
                    'D': np.array([3]*4, dtype="int32"),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': "foo"})
print(df2)
#      A          B    C  D      E    F
# 0  1.0 2013-01-02  1.0  3   test  foo
# 1  1.0 2013-01-02  1.0  3  train  foo
# 2  1.0 2013-01-02  1.0  3   test  foo
# 3  1.0 2013-01-02  1.0  3  train  foo

# DataFrame의 .dtypes라는 값에는 각 컬럼이 어떤 데이터 형식인지가 저장되어 있다. 만약 섞여있을 경우 object가 된다.
print(df2.dtypes)
# A           float64
# B     datetime64[ns]
# C            float32
# D             int32
# E           category
# F            object
# dtype: object
