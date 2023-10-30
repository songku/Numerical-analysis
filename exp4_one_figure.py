# -*- coding: UTF-8 -*-
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # 原数据分布图
    x_list = [3, 4, 5, 6, 7, 8, 9]
    x = np.array(x_list)  # 自变量
    y_list = [2.01, 2.98, 3.50, 5.02, 5.47, 6.02, 7.05]
    y = np.array(y_list)  # 因变量
    plt.plot(x, y, "ro")
    plt.show()
    # 最小二乘法拟合
    N_list = [1, 2, 5]  # 拟合的多项式的次数列表
    x_list = []
    plt.figure(figsize=(5.8 ,4.1))  # 英寸，8.27 11.69是A4纸张的大小
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
        func_string = "y="
        for i in range(N + 1):
            func_string = func_string + str(parameter[i]) + "*x^" + str(N - i)
        print(f"For N = {N} , line funtion is :", func_string)
        # 画出拟合图像
        plt.plot(x, y, "ro")
        if N == 1:
            current_color = 'r'
        elif N == 2:
            current_color = 'b'
        elif N == 3:
            current_color = 'g'
        elif N == 5:
            current_color = 'y'
        plt.plot(x, y2, label=f'Polynomial of degree {N}', color=current_color)
    plt.title("Experiment 4")
    plt.legend()  # 为了显示label/图例，图例的位置由loc参数影响
    plt.savefig("./exp4.jpg", dpi=1600)  # 需要在show()之前调用保存图像
    plt.show()
# output:
# For N = 1 , line funtion is : y=0.8275000000000001*x^1-0.3864285714285702*x^0
# For N = 2 , line funtion is : y=-0.020119047619047686*x^21.0689285714285721*x^1-1.0302380952381005*x^0
# For N = 5 , line funtion is : y=0.011374999999995802*x^5-0.3288636363635029*x^43.6658522727256497*x^3-19.6594696969602*x^251.53527272724594*x^1-50.75309523806603*x^0
