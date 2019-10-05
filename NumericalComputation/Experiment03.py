import math

# 定义误差
ipsl = 1e-20

# 定义迭代初始值,由于有多个根,故有多个初始值
# x_0 = -5
x_0 = -1

# 定义待求函数
def f(x):
    return (x**3-3*x**2+3*x-1)*(x+3)

# 定义待求函数的一阶导函数
def d_f(x):
    return 4*x**3-12*x+8

# 定义牛顿迭代法的迭代格式,m为修正系数,即重根数
def iter_Newton(x_k, m = 1):
    return x_k - m*(f(x_k)/d_f(x_k))

# 迭代过程
x_k = x_0
err = 100
i = 0
while err > ipsl:
    i = i + 1
    # x_n = iter_Newton(x_k)
    x_n = iter_Newton(x_k, 3)
    err = abs(x_n - x_k)
    print("iteration:", i, "  x:" ,x_n, "  error:", err)
    x_k = x_n
print("最终迭代结果为", x_n)