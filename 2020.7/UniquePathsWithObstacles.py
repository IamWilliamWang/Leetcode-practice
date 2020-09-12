from typing import List, Tuple
from test_script import speedtest


class Solution:
    def uniquePathsWithObstacles_slow(self, obstacleGrid: List[List[int]]) -> int:
        def goodPosition(i: int, j: int, footsteps: List[Tuple[int, int]]):
            return 0 <= i < rows and 0 <= j < cols and obstacleGrid[i][j] == 0 and (i, j) not in footsteps

        def dfs(i: int, j: int, footsteps: List[Tuple[int, int]]):
            if i == rows - 1 and j == cols - 1:
                return 1
            retList = []
            retList.append(dfs(i + 1, j, footsteps + [(i + 1, j)]) if goodPosition(i + 1, j, footsteps) else 0)
            retList.append(dfs(i, j + 1, footsteps + [(i, j + 1)]) if goodPosition(i, j + 1, footsteps) else 0)
            # retList.append(dfs(i - 1, j, footsteps + [(i - 1, j)]) if goodPosition(i - 1, j, footsteps) else 0)
            # retList.append(dfs(i, j - 1, footsteps + [(i, j - 1)]) if goodPosition(i, j - 1, footsteps) else 0)
            return sum(retList)

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if not rows or not cols:
            return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[rows - 1][cols - 1] == 1:
            return 0
        return dfs(0, 0, [(0, 0)])

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        def goodPosition(i: int, j: int):
            return 0 <= i < rows and 0 <= j < cols and obstacleGrid[i][j] == 0

        rows, cols = len(obstacleGrid), len(obstacleGrid[0])
        if not rows or not cols:
            return 0
        dp = [[0] * cols for _ in range(rows)]
        if obstacleGrid[0][0] == 1:
            return 0
        dp[0][0] = 1
        for i in range(rows):
            for j in range(cols):
                if not goodPosition(i, j):
                    continue
                if goodPosition(i - 1, j):
                    dp[i][j] += dp[i - 1][j]
                if goodPosition(i, j - 1):
                    dp[i][j] += dp[i][j - 1]
        return dp[-1][-1]


speedtest([Solution().uniquePathsWithObstacles, lambda x: 2], [[
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]])
speedtest([Solution().uniquePathsWithObstacles, lambda x: 2], [[
    [0, 0, 0, 0, 0, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 0, 0, 0, 0]]])
speedtest([Solution().uniquePathsWithObstacles, lambda x: 0], [[[0, 1]]])
speedtest([Solution().uniquePathsWithObstacles, lambda x: 7],
          [[[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0], [0, 0, 1, 0], [0, 0, 0, 0]]])
speedtest([Solution().uniquePathsWithObstacles, lambda x: 13594824],
          [[[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]]])
