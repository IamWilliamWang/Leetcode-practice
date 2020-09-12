from typing import List
import numpy as np


def 推导矩阵(matrix: List[List[int]]):
    def parse():
        for i in range(rows):
            for j in range(cols):
                if matrix[i, j] != 0:
                    continue
                if np.count_nonzero(matrix[i, :]) > 1:  # 此行可以推导出等差
                    good_j_list = np.nonzero(matrix[i, :])[0]  # 返回的是一个tuple，去除我想要的索引
                    d = (matrix[i, good_j_list[1]] - matrix[i, good_j_list[0]]) // (good_j_list[1] - good_j_list[0])  # 相差几，除以index之差，就是等差
                    matrix[i, :] = [matrix[i, 0] + j * d for j in range(cols)]  # 刷新该行
                if np.count_nonzero(matrix[:, j]) > 1:  # 此列可以推导出等差
                    good_i_list = np.nonzero(matrix[:, j])[0]  # 返回的是一个tuple，去除我想要的索引
                    d = (matrix[good_i_list[1], j] - matrix[good_i_list[0], j]) // (good_i_list[1] - good_i_list[0])  # 相差几，除以index之差，就是等差
                    matrix[:, j] = [matrix[0, j] + i * d for i in range(rows)]  # 刷新该列
        return matrix

    matrix: np.ndarray = np.array(matrix, dtype=np.int)
    rows, cols = matrix.shape
    while not (matrix.copy() == parse()).all():
        pass
    return matrix.tolist()


print(推导矩阵(
    [[2, 3, 6],
     [1, 0, 3],
     [0, 0, 0]]))
