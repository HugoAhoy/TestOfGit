# 第五章第8题
import numpy as np
import math
from matplotlib import pyplot as plt

# 原始数据
x = [1.0, 1.4, 1.8, 2.2, 2.6]
y = [0.931, 0.473, 0.297, 0.224, 0.168]

# 得到数据矩阵A
firstCol = np.ones([len(x),1])
A = np.c_[firstCol, np.array(x).reshape(-1,1)]
print("得到的矩阵A为:\n",A)
# 对y进行转换
y_Trans = np.array(list(map(lambda y:1/y, y))).reshape(-1, 1)
print("转换后的y为\n:", y_Trans)

# 最小二乘求系数
coef = np.matmul(np.linalg.inv(np.matmul(A.T, A)), np.matmul(A.T, y_Trans))

print("得到的系数是:\n",coef)

def getFunc(coef):
    def func(x):
        return 1/(coef[0]+x*coef[1])
    return func

# 得到拟合的函数
func = getFunc(coef)
x_n = np.arange(0.9,2.7, 0.01)
y_n = func(x_n)

print("拟合的y对应的值:\n",func(np.array(x)))

plt.title("Leasr Squares")
plt.xlabel("x")
plt.ylabel("y")
# 画出原始数据点
plt.scatter(x, y, color='', marker='o', edgecolor='r', label="raw point")
# 画出拟合函数
plt.plot(x_n, y_n, label="y=1(a+bx)")

# 显示图像
plt.legend()
plt.show()