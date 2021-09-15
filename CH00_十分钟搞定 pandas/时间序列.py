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
