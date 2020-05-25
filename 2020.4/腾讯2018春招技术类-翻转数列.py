import sys
# import numpy as np

n, m = list(map(int, sys.stdin.readline().strip().split()))
# nums = []
# for x in range(1 + m, n, 2 * m):
#     nums += [x + m for i in range(m)]
# nums = np.array(nums)
# print(sum(nums - (nums - m)))
print(m * n // 2)
