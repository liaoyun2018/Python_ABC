# -*- coding: utf-8 -*-
"""
Created on Mon Dec 30 21:35:30 2019

@author: HYZX
"""

import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
fig = plt.figure(num='低硫煅后焦数据分析-201912',figsize=(10, 8),facecolor='gray',edgecolor='g')
#h = text(0.5,1.0,'title')
#set(h,'fontsize',18,'HorizontalAlignment','center')
"""
figure:
figsize:以英寸为单位的宽高(1英寸等于2.54厘米)
facecolor:背景色
edgecolor：边框色

subplot:
subplot(numRows, numCols, plotNum)
图表的整个绘图区域被分成 numRows 行和 numCols 列
plotNum 参数指定创建的 Axes 对象所在的区域
numRows,numCols和plotNum这三个数都小于10的话,可以把它们缩写为一个整数,
例如 subplot(323) 和 subplot(3,2,3) 是相同的.

颜色：
b:blue
g:green
r:red
c:cyan,青绿色
y:yellow
k:black
w:white
purple ：紫色
"""
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel(
    r'C:\Users\HYZX\Desktop\报表\2019年12月\2019年12月分析结果汇总表.xlsx', sheet_name='煅后焦', header=1)  # 代码过长
df = df[(df['取样地点'] == '煅烧车间') & (df['规格/型号'] == '低硫')]  # &逻辑与，|逻辑或

plt.subplot(2, 2, 1)
df1 = df['灰分\n（%）']
x = df.index.astype('float')
y1 = df1
y2 = [0.70] * 34
plt.scatter(x, y1, label='灰分')
# plt.figure(figsize=(1.28, 0.85))
plt.plot(x, y2, 'r')
plt.ylabel('灰分')
plt.xticks([])  # 不显示x轴刻度
plt.title('灰分数据分析',  fontsize=14)
plt.legend()

plt.subplot(2, 2, 3)
df2 = df['硫分\n（%）'].drop([0, 1, 2, 7]).astype('float')
x = df2.index.astype('float')
y3 = df2
y4 = [0.50] * 30
plt.scatter(x, y3, label='硫含量')
#plt.figure(figsize=(1.28, 0.85))
plt.plot(x, y4, 'r')
plt.ylabel('硫含量')
plt.xticks([])  # 不显示x轴刻度
plt.title('硫含量数据分析',  fontsize=14)
plt.legend()

plt.subplot(2, 2, 4)
df3 = df['粉末电阻率\n(μΩ·m)'].astype('float')
x = df.index.astype('float')
y5 = df3
y6 = [500.0] * 34
plt.scatter(x, y5, label='粉末电阻率')
#plt.figure(figsize=(1.28, 0.85))
plt.plot(x, y6, 'r')
plt.ylabel('粉末电阻率')
plt.xticks([])  # 不显示x轴刻度
plt.title('粉末电阻率数据分析',  fontsize=14)

suptitle('低硫煅后焦数据分析-201912',  fontsize=20)
plt.legend()
plt.show()
