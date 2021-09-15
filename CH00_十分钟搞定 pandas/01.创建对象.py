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
dates = pd.date_range('20210914', periods=6)
print(dates)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
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
print(dates[0])
print(df.loc[dates[0]])
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
print(df.at[dates[0], 'A'])
print('------------通过位置选择------------------')
print('1、 通过传递数值进行位置选择（选择的是行）')
print(df)
print(df.iloc[3])
print('2、 通过数值进行切片，与 numpy/python 中的情况类似')
print(df.iloc[3:5, 0:2])
print('loc利用index的名称，来获取想要的行（或列）。iloc利用index的具体位置（所以它只能是整数型参数），来获取想要的行（或列）。')
print('3、 通过指定一个位置的列表，与 numpy/python 中的情况类似')
print(df.iloc[[1, 2, 4], [0, 2]])
print('4、 对行/列进行切片')
print(df.iloc[1:3, :])
print(df.iloc[:, 1: 3])
print('6、 获取特定的值')
print(df.iloc[1, 1])
print('快速访问标量（等同于前一个方法）：')
print(df.iat[1, 1])
print('布尔索引')
print('1、 使用一个单独列的值来选择数据')
print(df.A)
print(df.A > 0)
print(df[df.A > 0])
print('2、 使用 where 操作来选择数据：')
print(df[df > 0])
print('3、 使用 isin() 方法来过滤：')
df2 = df.copy()
df2['E'] = ['one', 'one', 'two', 'three', 'four', 'three']
print(df2)
print(df2[df2['E'].isin(['two', 'four'])])
print('设置')
print('1、 设置一个新的列：')
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('2021-09-14', periods=6))
print(s1)
df['F'] = s1
print(df)
print('2、 通过标签设置新的值：')
df.at[dates[0], 'A'] = 0
print(df)
print('3、 通过位置设置新的值：')
df.iat[0, 1] = 0
print(df)
print('4、 通过一个numpy数组设置一组新值：')
df.loc[:, 'D'] = np.array([5] * len(df))
print(df)
print('5、 通过where操作来设置新的值：')
df2 = df.copy()
df2[df2 > 0] = -df2
print(df2)
print('四、 缺失值处理')
print('在 pandas 中，使用 np.nan 来代替缺失值，这些值将默认不会包含在计算中')
print('1、 reindex() 方法可以对指定轴上的索引进行改变/增加/删除操作，这将返回原 始数据的一个拷贝：')
print(df)
print(dates[0:4])
print(df.columns)
print(list(df.columns))
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
print(df1)
df1.loc[dates[0]:dates[1], 'E'] = 1
print(df1)
print('2、 去掉包含缺失值的行：')
df1_ = df1.dropna(how='any')
print(df1_)
df1_ = df1.fillna(value=5)
print(df1_)
print('4、 对数据进行布尔填充：')
print(pd.isnull(df1_))
print(df1.isnull())
print('相关操作')
print(df.mean())
print(df.mean(1))
print('3、 对于拥有不同维度，需要对齐的对象进行操作。Pandas 会自动的沿着指定的 维度进行广播：')
s = pd.Series([1, 3, 5, np.nan, 6, 8], index=dates)
print(s)
print('shift函数是对数据进行移动的操作')
s = s.shift(2)
print(s)
print(' dataframe.sub()函数用于查找数据帧和其他逐元素的减法。')
print(df.sub(s, axis='index'))
print('Apply')
print('1、 对数据应用函数：')
print(df)
df = df.apply(np.cumsum)

print(df)
print(df.apply(lambda x: x.max() - x.min()))
print('直方图')
s = pd.Series(np.random.randint(0, 7, size=10))
print(s)
print(s.value_counts())
print('字符串方法')
print('Series 对象在其 '
      'str 属性中配备了一组字符串处理方法，'
      '可以很容易的应用到 数组中的每个元素')
s = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca', np.nan, ' CABA', 'dog', 'cat'])
print(s)
print(s.str.lower())
print('六、 合并')
print('Pandas 提供了大量的方法能够轻松的对 Series ，.'
      ' DataFrame 和 Panel 对象 进行各种符合各种逻辑关系的合并操作。')
print('Concat')
df = pd.DataFrame(np.random.randn(10, 4))
print(df)
pieces = [df[:3], df[3:7], df[7:]]
print(pd.concat(pieces))
print('Join: 类似于 SQL 类型的合并')
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
print(left)
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print(right)
print(pd.merge(left, right, on='key'))
print('另一个例子：')
left = pd.DataFrame({'key': ['foo', 'bar'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'bar'], 'rval': [4, 5]})
print(left)
print(right)
print(pd.merge(left, right, on='key'))
print('Append: 将一行连接到一个 DataFrame 上')
df = pd.DataFrame(np.random.randn(8, 4), columns=['A', ' B', 'C', 'D'])
print(df)
s = df.iloc[3]
print(s)
df = df.append(s, ignore_index=True)
print(df)
