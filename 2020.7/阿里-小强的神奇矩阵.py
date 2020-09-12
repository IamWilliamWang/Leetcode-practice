from typing import List, Tuple

import numpy as np


def 最小连续和(matrix: List[List[int]]):
    matrix: np.ndarray = np.array(matrix)
    rows, cols = matrix.shape
    assert rows == 3
    minDiffSum = 2 ** 31 - 1
    for row in range(rows):
        i, j = row, 0
        steps: List[Tuple[int, int]] = []
        diffSumI = 0
        while True:
            steps += [(i, j)]
            if len(steps) > 1:
                diffSumI += abs(matrix[steps[-1]] - matrix[steps[-2]])
            if j == cols - 1:
                break
            i, j = np.abs(matrix[:, j + 1] - matrix[i, j]).argmin(), j + 1  # 指向下一列，最接近matrix[i][j]的位置
        minDiffSum = min(minDiffSum, diffSumI)  # 比较每一次是否更佳
    return minDiffSum


print(最小连续和(
    [[5, 9, 5, 4, 4],
     [4, 7, 4, 10, 3],
     [2, 10, 9, 2, 3]]))
