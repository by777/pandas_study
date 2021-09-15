# -*- coding: utf-8 -*-
# @TIME : 2021/9/15 20:32
# @AUTHOR : Xu Bai
# @FILE : 分组.py
# @DESCRIPTION :
import pandas as pd
import numpy as np

print('分组\n'
      '对于”group by”操作，我们通常是指以下一个或多个操作步骤： \n'
      '（Splitting）按照一些规则将数据分为不同的组； \n'
      '（Applying）对于每组数据分别执行一个函数； \n'
      '（Combining）将结果组合到一个数据结构中；\n')
df = pd.DataFrame(
    {'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
     'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
     'C': np.random.randn(8),
     'D': np.random.randn(8)}
)
print(df)
print('1、 分组并对每个分组执行 sum 函数：')
print(df.groupby('B').groups)
print(df.groupby('A').sum())
print('2、 通过多个列进行分组形成一个层次索引，然后执行函数：')
print(df.groupby(['A', 'B']).groups)
