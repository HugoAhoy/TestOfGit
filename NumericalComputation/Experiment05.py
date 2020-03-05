from matplotlib import pyplot as plt
import numpy as np
import copy

# 牛顿插值法
def Newton(x, y):
    # 比较x与y是否一一对应
    if len(x) != len(y):
        return
    else:
        # 差分求系数
        coe = []
        coe.append(y[0])
        row = copy.deepcopy(y)
        for i in range(1, len(x)):
            for j in range(len(row) -1):
                row[j] = (row[j+1] - row[j])/(x[j + i]-x[j])
            coe.append(row[0])
            row.pop()
        
        # 牛顿插值函数
        def Newton_Interpolation(x_m):
            x_k = 1
            fx = 0
            print("牛顿插值系数",coe)
            for i in range(len(coe)):
                fx = fx + x_k * coe[i]
                x_k = x_k * (x_m- x[i])
            return fx

    # 返回求得的插值函数
    return Newton_Interpolation

# 拉格朗日插值
def Lagrange(x, y):
    # 比较x与y是否一一对应
    if len(x) != len(y):
        return
    else:
        # 拉格朗日插值基函数
        def L(x_m, k):
            l = 1
            for i in range(len(x)):
                if k == i:
                    continue
                else:
                    l = l * (x_m - x[i]) /(x[k] - x[i])
            return l

        # 拉格朗日插值函数
        def Lagrange_Interpolation(x_m):
            return sum(y[i]*L(x_m, i) for i in range(len(x)))

        return Lagrange_Interpolation

x = [-1, 0, 2, 3]
y = [-4, -1, 0, 3]

# 用于求逆函数的插值点
x_r = [-4, -1, 0, 3]
y_r = [-1, 0, 2, 3]

x_n = np.arange(-2,5,0.01)

# 显示图像函数
def showFig(x, *Interpolate_Func):
    plt.title("Interpolation")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    for func in Interpolate_Func:
        plt.plot(x, func(x_n), label=func.__name__)
    plt.legend()
    plt.show()

# 求f(1.5)的值
print("f(1.5)=",Newton(x, y)(1.5))
print("f(1.5)=",Lagrange(x, y)(1.5))

# 求f(x) = 0.5 时x的值
print("x = f^-1(0.5)=",Newton(x_r, y_r)(0.5))
print("x = f^-1(0.5)=",Lagrange(x_r, y_r)(0.5))

# 牛顿插值函数图像
showFig(x_n, Newton(x, y))
showFig(x_n, Newton(x_r, y_r))

# 拉格朗日插值函数图像
showFig(x_n, Lagrange(x, y))
showFig(x_n, Lagrange(x_r, y_r))

# 同时显示牛顿插值函数图像和拉格朗日插值函数图像
showFig(x_n, Newton(x, y), Lagrange(x, y))

# 显示牛顿插值函数和拉格朗日插值函数的差对比图像
showFig(x_n, lambda p: Newton(x, y)(p) - Lagrange(x, y)(p))