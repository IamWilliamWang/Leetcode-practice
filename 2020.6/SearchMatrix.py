from typing import List, Tuple
from test_script import binary_search, speedtest
import sys

sys.path.append('./2020.4')
import OfferFindNumberIn2DArray


class Solution:
    def searchMatrix_multiBiSearch(self, matrix: List[List[int]], target: int) -> bool:
        for line in matrix:
            if binary_search(line, target) != -1:
                return True
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(left: int, right: int, top: int, bottom: int) -> Tuple[int, int]:
            if left > right or top > bottom:
                return -1, -1
            mid = (left + right) // 2
            row = top
            while row <= bottom and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return row, mid
                row += 1
            searchLeftDown = search(left, mid - 1, row, bottom)
            if searchLeftDown != (-1, -1):
                return searchLeftDown
            searchRightUp = search(mid + 1, right, top, row - 1)
            return searchRightUp

        if not matrix:
            return False
        return search(0, len(matrix[0]) - 1, 0, len(matrix) - 1) != (-1, -1)

    def searchMatrix_extremelyFast(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        i, j = len(matrix) - 1, 0
        while i >= 0 and j < len(matrix[0]):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                i -= 1
            elif matrix[i][j] < target:
                j += 1
        return False


speedtest([Solution().searchMatrix_multiBiSearch, Solution().searchMatrix, Solution().searchMatrix_extremelyFast],
          ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 21))
speedtest([Solution().searchMatrix_multiBiSearch, Solution().searchMatrix, Solution().searchMatrix_extremelyFast],
          ([[1, 4, 6, 8, 10, 12] + list(range(13, 1000)),
            [3, 5, 7, 8, 11, 13] + list(range(14, 1001)),
            [5, 6, 7, 9, 13, 15] + list(range(16, 1003)),
            [6, 9, 11, 12, 13, 16] + list(range(18, 1005))], 1004))
import numpy as np

matrix = np.zeros((5000, 5000))
for i in range(matrix.shape[0]):
    for j in range(matrix.shape[1]):
        matrix[i][j] = i + j
speedtest([Solution().searchMatrix_multiBiSearch, Solution().searchMatrix, Solution().searchMatrix_extremelyFast], (matrix.tolist(), 10000))
