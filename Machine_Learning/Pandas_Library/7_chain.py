import numpy as np
import pandas as pd

# 7. 묶기
# SQL과 유사한 group by에 관련된 내용은 아래와 같은 과정을 말한다.
# 1. Spltting : 어떠한 기준을 바탕으로 데이터를 나누는 일
# 2. applying : 각 그룹에 어떤 함수를 독립적으로 적용시키는 일
# 3. Combining : 적용되어 나온 결과들을 통합하는 일
# 아래의 예시처럼 같은 그룹의 합도 구할 수 있지만, .agg() 함수를 통해 여러가지 값을 확인할 수 있다.
# (ex. df.groupby('A').agg(['min', 'max']))

df = pd.DataFrame({'A': ['foo', 'bar', 'foo', 'bar',
                         'foo', 'bar', 'foo', 'foo'],
                   'B': ['one', 'one', 'two', 'three',
                         'two', 'two', 'one', 'three'],
                   'C': np.random.randn(8),
                   'D': np.random.randn(8)})
#      A      B         C         D
# 0  foo    one -1.090875 -1.522510
# 1  bar    one -0.255675 -1.907910
# 2  foo    two -1.953929  1.751055
# 3  bar  three  1.024903  0.697971
# 4  foo    two -0.208788 -0.013917
# 5  bar    two  1.494786  0.200477
# 6  foo    one  0.060616  0.504577
# 7  foo  three  1.061218 -0.005272

df.groupby('A').sum()
#                      B         C         D
# A
# bar        onethreetwo  2.934465 -0.946541
# foo  onetwotwoonethree -1.478399  0.380871

df.groupby(['A', 'B']).sum()
#                   C         D
# A   B
# bar one    1.527591  2.236206
#     three -0.532155 -0.101061
#     two    0.916456  0.151730
# foo one    0.587990 -2.213079
#     three  0.351429  0.469170
#     two    0.292676 -0.002052
