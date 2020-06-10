from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        dpMatrix = [[0] * (1 + len(matrix[0])) for _ in range(1 + len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == '1':
                    dpMatrix[i + 1][j + 1] = min(dpMatrix[i + 1][j], dpMatrix[i][j + 1], dpMatrix[i][j]) + 1
        maxNum = 0
        for nums in dpMatrix:
            for num in nums:
                if num > maxNum:
                    maxNum = num
        return maxNum ** 2
