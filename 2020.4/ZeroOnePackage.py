import sys
import time
from functools import lru_cache

sys.setrecursionlimit(100000)  # 用于解除递归调用上限次数
def zeroOnePackage(weight: list, values: list, capacity: int):
    @lru_cache(maxsize=None)
    def dp(i: int, resultCapicity: int):
        if i < 0:
            return 0
        if resultCapicity < weight[i]:
            return dp(i - 1, resultCapicity)
        else:
            return max(dp(i - 1, resultCapicity - weight[i]) + values[i], dp(i - 1, resultCapicity))

    return dp(len(weight) - 1, capacity)


def zeroOnePackageNonRecursion(weight: list, values: list, capacity: int):
    # x表示第几个item，y表示capacity
    matrix = [[0] * (capacity + 1) for _ in range(len(weight) + 1)]
    for i in range(1, len(weight) + 1):  # matrix在x和y上多一行一列的空白值
        for j in range(1, capacity + 1):
            if j < weight[i - 1]:
                matrix[i][j] = matrix[i - 1][j]
            else:
                matrix[i][j] = max(matrix[i - 1][j - weight[i - 1]] + values[i - 1], matrix[i - 1][j])
    return matrix[len(weight)][capacity]


startTime = time.time()
weight = [x for x in range(1, 1000)]
values = [x for x in range(2, 1001)]
capacity = 100
print(zeroOnePackage(weight, values, capacity))
print(time.time() - startTime)
# 时间统计：
# 使用递归的执行时间为 7.045974493026733
# 使用lru_cache后递归的执行时间为 0.007995367050170898
# 不使用lru_cache，使用dict进行优化的执行时间为 0.00997304916381836
# 使用非递归的dp执行时间为 0.04898691177368164
