#coding=utf-8

import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 通过rcParams设置全局横纵字体大小
mpl.rcParams['xtick.labelsize']=50
mpl.rcParams['ytick.labelsize']=24

###
np.random.seed(42)

#x轴的采样点
x=np.linspace(0,5,100)

#通过下面曲线加上噪声生成数据，所以拟合模型就用y啦
y=2*np.sin(x)+0.3*x**2
y_data=y+np.random.normal(scale=0.3,size=100)

#figure()指定图表名称
plt.figure('data1')

#‘*’标明是散点图，每个散点的形状是个*
plt.plot(x,y_data,'*')

# 画模型的图，plot函数默认画连线图
plt.figure('model')
plt.plot(x,y,'*')

#两个图画在一起
plt.figure('data & model')

#通过‘r--'设置线的颜色和线性，’r--' 表示红色虚线
#lw指定线的宽度
plt.plot(x,y,'r--',lw=3)

#scatter可以更容易地生成散点图
plt.scatter(x,y_data)

#将当前figure的图保存到文件result.png
plt.savefig('result.png')

#一定要加上这句才能让画好的图显示在屏幕上
plt.show()
(12)