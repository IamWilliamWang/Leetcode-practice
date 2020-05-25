import numpy as np


class Solution:
    def updateMatrix(self, matrix: list) -> list:
        # distanceMatrix = np.zeros_like(matrix)
        distanceMatrix = [[0] * len(matrix[0]) for _ in range(len(matrix))]

        def get(i: int, j: int):
            return -1 if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]) else matrix[i][j]

        def bfs(from_i: int, from_j: int):
            queue = [(from_i, from_j)]
            queueLevel = [0]
            while len(queue) > 0:
                i, j = queue.pop(0)
                level = queueLevel.pop(0)
                if get(i, j) == 0:
                    return level
                if (i + 1, j) not in queue:
                    queue += [(i + 1, j)]
                    queueLevel += [level + 1]
                if (i, j + 1) not in queue:
                    queue += [(i, j + 1)]
                    queueLevel += [level + 1]
                if (i - 1, j) not in queue:
                    queue += [(i - 1, j)]
                    queueLevel += [level + 1]
                if (i, j - 1) not in queue:
                    queue += [(i, j - 1)]
                    queueLevel += [level + 1]
            return -1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                distanceMatrix[i][j] = bfs(i, j)
        # return distanceMatrix.tolist()
        return distanceMatrix

print(Solution().updateMatrix(
    [[0, 0, 0],
     [0, 1, 0],
     [1, 1, 1]]
))
