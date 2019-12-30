# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 20:15:58 2019

@author: HYZX
"""

import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel(
    r'C:\Users\HYZX\Desktop\报表\2019年12月\
    \2019年12月分析结果汇总表.xlsx', sheet_name='煅后焦', header=1)  # 代码过长
df = df[(df['取样地点'] == '煅烧车间') & (df['规格/型号'] == '低硫')]  # &逻辑与，|逻辑或
# df = df[(df['规格/型号'] == '低硫')]
df = df['硫分\n（%）'].drop([0, 1, 2, 7])
df = df.astype('float')
x = df.index.astype('float')
y1 = df
# print(len(y1))
y2 = [0.50] * 29
# print(type(y1), type(x), x, y1)

plt.scatter(x, y1, label='硫含量')
plt.plot(x, y2, 'r')
plt.ylabel('硫含量')
plt.xticks([])  # 不显示x轴刻度
plt.title('低硫煅后焦硫含量数据分析-201912',  fontsize=18)
plt.legend()
plt.show()
