import numpy as np

M, K, N = list(map(int, input().strip().split()))
mat1, mat2 = [], []
for _ in range(M):
    mat1.append(list(map(int, input().strip().split())))
for _ in range(K):
    mat2.append(list(map(int, input().strip().split())))
result = np.dot(mat1, mat2)
for row in result:
    print(' '.join(map(str, row)))
