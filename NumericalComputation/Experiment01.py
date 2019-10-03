import math

# 定义误差
ipsl = 0.5e-4

# 设置迭代初始值
x_0 = 1.5

# 定义4种迭代格式的函数
def iter_func1(x_k):
    return 1+1/(x_k**2)

def iter_func2(x_k):
    return pow(x_k**2+1, 1/3)

def iter_func3(x_k):
    return math.sqrt(1/(x_k-1))

def iter_func4(x_k):
    return math.sqrt(x_k**3-1)

# 迭代过程
err = 100
x_k = x_0
i = 0
while err > ipsl:
    i = i + 1

    # 此处可修改使用的迭代函数
    # x_n = iter_func1(x_k)
    # x_n = iter_func2(x_k)
    # x_n = iter_func3(x_k)
    x_n = iter_func4(x_k)
    err = abs(x_n - x_k)
    print("iteration:", i, "  x:" ,x_n, "  error:", err)
    x_k = x_n

print("最终迭代结果为", x_n)
