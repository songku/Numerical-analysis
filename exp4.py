import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # 原数据分布图
    x_list = [3, 4, 5, 6, 7, 8, 9]
    x = np.array(x_list)  # 自变量
    y_list = [2.01, 2.98, 3.50, 5.02, 5.47, 6.02, 7.05]
    y = np.array(y_list)  # 因变量
    plt.scatter(x, y)
    plt.show()
    # 最小二乘法拟合
    N_list = [1, 2, 5]  # 拟合的多项式的次数列表
    x_list = []
    for N in N_list:
        parameter = np.polyfit(x, y, N)  # 第三个参数代表着拟合成几次多项式
        if N == 1:
            y2 = parameter[0] * x + parameter[1]
        elif N == 2:
            y2 = parameter[0] * x ** 2 + parameter[1] * x ** 1 + parameter[2]
        elif N == 3:
            y2 = parameter[0] * x ** 3 + parameter[1] * x ** 2 + parameter[2] * x + parameter[3]
        elif N == 5:
            y2 = parameter[0] * x ** 5 + parameter[1] * x ** 4 + parameter[2] * x ** 3 + parameter[3] * x ** 2 + \
                 parameter[4] * x + parameter[5]
        else:
            print("don't support N value:", N)
            exit(0)
        # 输出函数表达式
        func_string="y="
        for i in range(N+1):
            func_string=func_string+str(parameter[i])+"*x^"+str(N-i)
        print(f"For N = {N} , line funtion is :",func_string)
        # 画出拟合图像
        plt.scatter(x, y)
        plt.plot(x, y2, color='r')
        plt.show()