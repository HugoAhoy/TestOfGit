# LU分解
from functools import reduce
import math
import numpy as np

mat = np.array([[1, 8, 0],
                [2, 4, 1],
                [2, 1, 1]])

# 带分解矩阵的形状和行列数
shape = mat.shape
dim = shape[1]

# 初始化L和U
L = np.identity(dim)
U = np.zeros(shape)

U[0,:] = mat[0,:]

for i in range(dim):
    L[i,0] = mat[i,0] / U[0,0]

# 杜利特尔分解
for r in range(1,dim):
    for i in range(r, dim):
        sum = reduce(lambda x,y:x+y, [L[r,k]*U[k,i] for k in range(r)])
        U[r,i] = mat[r,i] - sum

    for i in range(r, dim):        
        sum = reduce(lambda x,y:x+y, [L[i,k]*U[k,r] for k in range(r)])
        L[i, r] = (mat[i,r] - sum)/ U[r,r]

# 输出结果
print("L\n", L)
print("U\n", U)
