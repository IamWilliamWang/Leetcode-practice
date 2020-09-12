from typing import List
from functools import lru_cache


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        INFINATE = 2 ** 31 - 1
        # @lru_cache(maxsize=None)
        # def dp(i: int, j: int):
        #     if not (0 <= i < rows and 0 <= j < cols):
        #         return INFINATE
        #     if i == rows - 1 and j == cols - 1:
        #         return grid[i][j]
        #     return grid[i][j] + min(dp(i + 1, j), dp(i, j + 1))
        #
        # return dp(0, 0)
        dp = [[INFINATE] * (cols + 1) for _ in range(rows + 1)]
        dp[1][0] = dp[0][1] = 0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                dp[i][j] = grid[i - 1][j - 1] + min(dp[i - 1][j], dp[i][j - 1])
        return dp[rows][cols]
