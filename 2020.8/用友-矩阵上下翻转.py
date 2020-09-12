#
# 将矩阵的二维数组进行上下翻转处理
# @param matrix int整型二维数组 矩阵
# @return int整型二维数组
#
from typing import List


class Solution:
    def convert(self, matrix: List[List[int]]) -> List[List[int]]:
        for i in range(len(matrix) // 2 + 1):
            matrix[i], matrix[len(matrix) - i - 1] = matrix[len(matrix) - i - 1], matrix[i]
        return matrix
