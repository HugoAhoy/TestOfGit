import math
import time

# 定义误差
ipsl = 0.5e-10

# 设置迭代初始值
x_0 = 2

# 定义不动点迭代格式的函数
def iter_func(x_k):
    return math.log(x_k) + 2

# 定义斯蒂芬森加速迭代格式的函数
def Steffensen(x_k):
    y_k = math.log(x_k) + 2
    z_k = math.log(y_k) + 2
    return x_k - (y_k-x_k)**2/(z_k-2*y_k+x_k)

# 不动点迭代
print("fixed-point iteration")
x_k = x_0
err = 100
i = 0
time_start=time.time()
while err > ipsl:
    i = i + 1
    x_n = iter_func(x_k)
    err = abs(x_n - x_k)
    print("iteration:", i, "  x:" ,x_n, "  error:", err)
    x_k = x_n
time_end=time.time()
print("最终迭代结果为", x_n)
print("耗时:",time_end-time_start)


# 斯蒂芬森迭代
print("\nSteffensen method")
x_k = x_0
err = 100
i = 0
time_start=time.time()
while err > ipsl:
    i = i + 1
    x_n = Steffensen(x_k)
    err = abs(x_n - x_k)
    print("iteration:", i, "  x:" ,x_n, "  error:", err)
    x_k = x_n
time_end=time.time()
print("最终迭代结果为", x_n)
print("耗时:",time_end-time_start)