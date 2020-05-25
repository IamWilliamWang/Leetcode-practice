import sys
import numpy as np


class Solution:
    def __init__(self):
        self.rows = self.cols = self.maxLimit = 0
        self.visited = []
        self.movableCount = 0

    def _parse(self, number: int) -> int:
        result = 0
        for ch in str(number):
            result += int(ch)
        return result

    def _reachable(self, x: int, y: int) -> bool:
        return 0 <= x <= self.rows - 1 and 0 <= y <= self.cols - 1 and self.visited[x][y] == 0 and self._parse(
            x) + self._parse(y) <= self.maxLimit

    def dfs(self, i: int, j: int) -> None:
        if not self._reachable(i, j):
            return
        self.visited[i][j] = 1
        self.movableCount += 1
        self.dfs(i + 1, j)
        self.dfs(i, j + 1)
        self.dfs(i - 1, j)
        self.dfs(i, j - 1)

    def bfs(self, i: int, j: int) -> None:
        queue = [(i, j)]
        while len(queue) != 0:
            x, y = queue.pop(0)
            self.visited[x][y] = 1
            self.movableCount += 1
            if self._reachable(x + 1, y) and (x + 1, y) not in queue:
                queue += [(x + 1, y)]
            if self._reachable(x, y + 1) and (x, y + 1) not in queue:
                queue += [(x, y + 1)]
            if self._reachable(x - 1, y) and (x - 1, y) not in queue:
                queue += [(x - 1, y)]
            if self._reachable(x, y - 1) and (x, y - 1) not in queue:
                queue += [(x, y - 1)]

    def movingCount(self, m: int, n: int, k: int) -> int:
        self.rows, self.cols, self.maxLimit = m, n, k
        self.visited = np.zeros((self.rows, self.cols))
        self.bfs(0, 0)
        return self.movableCount


m, n, k = sys.stdin.readline().strip().split()
print(Solution().movingCount(int(m), int(n), int(k)))
