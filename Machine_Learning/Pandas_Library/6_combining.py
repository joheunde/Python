import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
df['F'] = s1

df.loc[dates[0], 'A'] = 0

df.iloc[0, 1] = 0

df.loc[:, 'D'] = np.array([5] * len(df))

# 6. 합치기
# 다양한 정보를 데이터가 있을 때 데이터들을 하나로 합쳐서 새로운 데이터로 만들어야 할 때가 있다.
# 같은 형태의 자료들을 이어 하나로 만들어주는 concat, 다른 형태의 자료들을 한 컬럼을 기준으로 합치는 merge를 활용할 수 있다.
# Concat을 이용하여 Pandas 오브젝트들을 일렬로 연결시켜준다.

df = pd.DataFrame(np.random.randn(10, 4))
#           0         1         2         3
# 0 -0.005893  0.585417 -0.397076  0.668809
# 1 -1.306623  0.439762  0.224434 -1.527887
# 2 -1.231418  0.745856  0.026979 -0.609338
# 3  0.015400 -0.924950  0.206390 -0.861507
# 4 -0.306602 -0.975641  0.229345 -0.337130
# 5  0.162055  1.026560 -1.492844  2.252009
# 6 -1.147978  1.152733  0.778201 -0.875890
# 7  1.183253  0.351051 -0.323251  1.030742
# 8 -0.768540  1.520397 -0.597737  0.076572
# 9 -0.826936 -1.258115 -1.037164 -0.894134

# break it into pieces
pieces = [df[:3], df[3:7], df[7:]]

# concatenate again
pd.concat(pieces)
#           0         1         2         3
# 0  1.023981  2.202269  0.661709 -0.307383
# 1  0.357838  0.260505  0.227765  1.799306
# 2 -0.289372  0.835520  1.747295 -0.105233
# 3 -1.512953  0.357285  0.378426 -0.720345
# 4  0.301678  0.201232 -1.677604 -0.470132
# 5 -0.467291 -0.058110  1.661260 -1.110210
# 6  0.281744  1.242379  0.278340 -0.616780
# 7  0.633821  1.006615  0.360956 -1.027440
# 8 -0.550760 -0.307866  0.831437  0.008311
# 9  0.965726  0.351964  0.063301 -1.363772

# Merge
# 데이터베이스에서 사용하는 SQL 스타일의 합치기 기능이다. merge 메소드를 통해 이루어진다.
# 1
left = pd.DataFrame({"key": ["foo", "foo"], "lval": [1, 2]})
#    key  lval
# 0  foo     1
# 1  foo     2

right = pd.DataFrame({"key": ["foo", "foo"], "rval": [4, 5]})
#    key  rval
# 0  foo     4
# 1  foo     5

merged = pd.merge(left, right, on="key")
#    key  lval  rval
# 0  foo     1     4
# 1  foo     1     5
# 2  foo     2     4
# 3  foo     2     5

# 2
left = pd.DataFrame({"key": ["foo", "bar"], "lval": [1, 2]})
#    key  lval
# 0  foo     1
# 1  bar     2

right = pd.DataFrame({"key": ["foo", "bar"], "rval": [4, 5]})
#    key  rval
# 0  foo     4
# 1  bar     5

merged = pd.merge(left, right, on="key")
#    key  lval  rval
# 0  foo     1     4
# 1  bar     2     5
