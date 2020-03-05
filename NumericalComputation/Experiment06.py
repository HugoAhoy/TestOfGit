import numpy as np
from matplotlib import pyplot as plt

# 求回归方程组系数
def getA(x, order):
    A = np.ones([len(x), order+1])
    for i in range(1, order+1):
        A[:,i] = A[:,i-1] *x
    return A

# 求拟合多项式系数
def getCoefficient(x, y, order):
    A = getA(x, order)
    LHS_Coe = np.matmul(A.T, A)
    RHS = np.matmul(A.T, y)
    coe = np.matmul(np.mat(LHS_Coe).I, RHS)
    return coe.A.tolist()[0]

# 求拟合多项式函数
def getFunction(x, y, order):
    coe = getCoefficient(x, y, order)
    print(coe)
    def func(x_in):
        ans = 0
        x_k = 1
        for i in range(len(coe)):
            ans = ans + coe[i]*x_k
            x_k = x_k* x_in
        return ans
    return func

# 原始数据
x = [-2, -1, 0, 1, 2]
y = [-0.1, 0.1, 0.4, 0.9, 1.6]

# 二次多项式函数
func2 = getFunction(x, y, 2)
# 三次多项式函数
func3 = getFunction(x, y, 3)

x_n = np.arange(-3,3, 0.01)

plt.title("Leasr Squares")
plt.xlabel("x")
plt.ylabel("f(x)")
# 原始数据点
plt.scatter(x, y, color='', marker='o', edgecolor='r', label="raw point")
# 二次多项式
plt.plot(x_n, func2(x_n), label="x^2")
# 三次多项式
plt.plot(x_n, func3(x_n), label="x^3")
# 显示图像
plt.legend()
plt.show()