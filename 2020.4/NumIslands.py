class Solution:
    def numIslands(self, grid: list) -> int:
        if len(grid) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])

        def dfs(i: int, j: int):
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return
            if grid[i][j] == '0':
                return
            grid[i][j] = '0'
            dfs(i + 1, j)
            dfs(i, j + 1)
            dfs(i - 1, j)
            dfs(i, j - 1)

        ans = 0
        while True:
            found = False
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == '1':
                        dfs(i, j)
                        ans += 1
                        found = True
            if not found:
                break
        return ans


print(Solution().numIslands(
    [["1", "1", "0", "0", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "1", "0", "0"], ["0", "0", "0", "1", "1"]]))
