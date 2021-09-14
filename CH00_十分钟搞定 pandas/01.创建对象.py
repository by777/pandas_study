# -*- coding: utf-8 -*-
# @TIME : 2021/9/14 17:43
# @AUTHOR : Xu Bai
# @FILE : 01.创建对象.py
# @DESCRIPTION :
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('-' * 20, '01.创建对象', '-' * 20)
# 1.传递一个list对象来创建一个Series,pandas会默认添加索引
print('#' * 40)
s = pd.Series([1, 3, 5, np.NAN, 6, 8])
print(s)

# 2.传递一个np array，时间索引以及列标签来创建一个DataFrame
print('#' * 40)
datas = pd.date_range('20210914', periods=6)
print(datas)
df = pd.DataFrame(np.random.randn(6, 4), index=datas, columns=list('ABCD'))
print(df)
print(list('ABCD') == ['A', 'B', 'C', 'D'])

# 3.传递一个能够被转换成类似序列结构的字典对象来创建DataFrame
print('#' * 40)
df2 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20210914'),
    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
    'D': np.array([3] * 4, dtype='int32'),
    'E': pd.Categorical(['test', 'train', 'test', 'train']),
    'F': 'foo'
})
print(pd.Timestamp('20210914'))
print(df2)

# 4.查看不同列的数据类型
print('#' * 40)
print(df2.dtypes)

print('-' * 20, '02.查看数据', '-' * 20)

# 1.查看 DataFrame 中头部和尾部的行：
print(df.head())
print(df.tail(3))
# 2.显示索引、列和底层的 numpy 数据：
print('index是第一列')
print(df.index)
print('columns是第一行')
print(df.columns)
print(df.values)
print(df.values.dtype)

# 3.describe() 函数对于数据的快速统计汇总：
print(df.describe())

# 4.对数据的转置
# 5.按轴进行排序
print(df)
print(df.sort_index(axis=1, ascending=False))
# 6.按值进行排序
print(df.sort_values(by='B'))

print('-' * 20, '03.选择', '-' * 20)
print('虽然标准的 Python/Numpy '
      '的选择和设置表达式都能够直接派上用场，但是作为工程使用的代码，我们推荐使用经过优化的 pandas 数据访问方式： .at , .iat , .loc , .iloc 和 .ix 。详')

print('1、 选择一个单独的列，这将会返回一个 Series ，等同于 df.A ')
print(df['A'])
print('2、 通过 [] 进行选择，这将会对行进行切片')
print('0 1 2行')
print(df[0:3])
print(df['2021-09-14':'2021-09-16'])
print('------------通过标签选择------------------')
print('1、 使用标签来获取一个交叉的区域(通过行索引)')
print(df)
print(datas[0])
print(df.loc[datas[0]])
print('2、 通过标签来在多个轴上进行选择')
print(df.loc[:, ['A', 'B']])
print('3、 标签切片')
print(df.loc['20210914':'20210916', ['A', 'C']])
print('4、 对于返回的对象进行维度缩减')
print(df.loc['20210914'])
print(df.loc['20210914', ['A', 'B']])
print('5、 获取一个标量')
print(df.loc['20210914', 'A'])
print('6、 快速访问一个标量（与上一个方法等价）')
print(df.at[datas[0], 'A'])
