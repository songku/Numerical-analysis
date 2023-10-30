# 参考：
# 各种插值法的python实现 https://blog.csdn.net/ourjaycn/article/details/127684756
# 拉格朗日插值图像 https://wenku.csdn.net/answer/61gxd1majd
# Matlab实验：高次插值的龙格现象（Runge）实验 https://blog.csdn.net/didi_ya/article/details/109407891
# ⭐拉格朗日插值验证龙格现象python https://blog.csdn.net/todcode/article/details/128749371
# 往届作业中分别对比了三种方法的n=10和n=40的情况
# 拉格朗日插值增大节点数势必会增加多项式的次数，会令结果不稳定。这就是多项式插值的缺点。后两种方法都比多项式插值好，且在给定节点数的条件下，三次样条
# 精度高于分段线性插值，且光滑性要好一些。

# -*-coding:utf-8 -*-
import numpy as np
from scipy import interpolate
from scipy.interpolate import lagrange  # 拉格朗日插值
import pylab as plt

x_raw = np.linspace(-1, 1, 200)  # 原曲线，增多点使其画图效果的光滑性更好
# plt.plot(x_raw, np.array(1 / (1 + 25 * x_raw * x_raw)), 'b', label='f(x)=1 / (1 + 25*x^2)')  # 原曲线
# 原始数据是要过的插值点  插值图像/函数要尽可能接近原始图像/函数

x = np.linspace(start=-1, stop=1, num=21)  # 因为h=0.1，所以num=21 j=0~20
print("x sequence:", x)
y = np.array(1 / (1 + 25 * x * x))  # f(x)=1/(1+25*x^2)
print("y sequence:", y)
# plt.plot(x, y, "ro")  # 'ro’表示标记点为红色小圆圈

for N in [21, 41]:  # 分别取21个数据点和41个数据点进行对比
    for kind in ["lagrange", "slinear", "cubic"]:  # 插值方式
        # lagrange 拉格朗日插值 slinear 线性插值 cubic 为3阶样条插值插值
        # 将函数图像和数据点先进行展示
        # plt.figure(figsize=(5.8, 4.1))  # 英寸，8.27 11.69是A4纸张的大小
        plt.plot(x_raw, np.array(1 / (1 + 25 * x_raw * x_raw)), 'b', label='f(x)=1 / (1 + 25*x^2)')  # 原曲线
        plt.plot(x, y, "ro")  # 'ro’表示标记点为红色小圆圈
        if kind != "lagrange":
            f = interpolate.interp1d(x, y, kind=kind)  # interp1d是1维插值
            # ‘slinear’, ‘quadratic’ and ‘cubic’ refer to a spline interpolation of first, second or third order)
            xnew = np.linspace(-1, 1, N)
            ynew = f(xnew)
            plt.plot(xnew, ynew, label=f"{kind} interpolate N={N-1}")
            plt.legend()  # 为了显示label/图例，图例的位置由loc参数影响
            plt.savefig(f"./exp3-{kind}-N_{N}.jpg", dpi=1600)  # 需要在show()之前调用保存图像
            plt.show()
        else:
            p = lagrange(x, y)  # 生成对应的拉格朗日多项式  x,y来自龙格函数的样本点，点越多，龙格现象越明显
            xi = np.linspace(-1, 1, N)
            yi = p(xi)
            plt.plot(xi, yi, label=f"{kind} interpolate N={N-1}")
            plt.legend()  # 为了显示label/图例，图例的位置由loc参数影响
            plt.savefig(f"./exp3-{kind}-N_{N}.jpg", dpi=1600)  # 需要在show()之前调用保存图像
            plt.show()