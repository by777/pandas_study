# -*- coding: utf-8 -*-
# @TIME : 2021/9/15 20:41
# @AUTHOR : Xu Bai
# @FILE : 改变形状.py
# @DESCRIPTION :
import numpy as np
import pandas as pd

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                    ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))
print(tuples)
index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
print(index)
df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])
# print(df)
df2 = df[:4]
print(df2)
print('stack')
stacked = df2.stack()
print(stacked)
print(stacked.unstack(1))
