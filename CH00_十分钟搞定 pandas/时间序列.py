# -*- coding: utf-8 -*-
# @TIME : 2021/9/15 20:54
# @AUTHOR : Xu Bai
# @FILE : 时间序列.py
# @DESCRIPTION :
import numpy as np
import pandas as pd

print('时间序列 Pandas '
      '在对频率转换进行重新采样时拥有简单、'
      '强大且高效的功能（如将按秒采 样的数据转换为按5分钟为单位进行采样的数据）。'
      '')
rng = pd.date_range('1/1/2012', freq='S', periods=100)
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print(ts)
print('Pandas中的resample，'
      '重新采样，是对原样本重新处理的一个方法，'
      '是一个对常规时间序列数据重新采样和频率转换的便捷的方法。'
      '降采样：高频数据到低频数据'
      '升采样：低频数据到高频数据')
print(ts.resample('5Min').mean())
print('1、 时区表示：')
rng = pd.date_range('3/6/2012 00:00', periods=5, freq='D')
print(rng)
ts = pd.Series(np.random.randn(len(rng)), rng)
print(ts)
ts_utc = ts.tz_localize('UTC')
print(ts_utc)
print('2、 时区转换：')
print(ts_utc.tz_convert('US/Eastern'))
print('3、 时间跨度转换：')
rng = pd.date_range('1/1/2012', periods=5, freq='M')
ts = pd.Series(np.random.randn(len(rng)), index=rng)
print(ts)
ps = ts.to_period()
print(ps)
print(ps.to_timestamp())
print('4、 时期和时间戳之间的转换使得可以使用一些方便的算术函数。')
prng = pd.period_range('1990Q1', '2000Q4', freq='Q-NOV')
print(prng)
# 以季度Q【季度为频率】生成13个时间
x = pd.period_range("2019-01", periods=13, freq="Q")

# 以季度Q【年为频率】生成13个时间
x = pd.period_range("2019-01", periods=13, freq="Y")

# 以季度Q【2个月为频率】生成13个时间
x = pd.period_range("2019-01", periods=13, freq="2m")
# 对于某些频率，你可以指定一个锚定后缀【后缀代表一年结束的月份,默认是12月份结束】
# 其他1-12月为结束的后缀都和单词前三个字母大写，请查询表格
