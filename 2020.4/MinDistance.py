class Solution:
    def minDistanceRecursive(self, word1: str, word2: str) -> int:
        dict = {}

        def dp(i: int, j: int):
            if (i, j) in dict:
                return dict[(i, j)]
            if i == -1:
                return j + 1
            if j == -1:
                return i + 1
            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)
            dict[(i, j)] = min(1 + dp(i - 1, j), 1 + dp(i, j - 1), 1 + dp(i - 1, j - 1))
            return dict[(i, j)]

        return dp(len(word1) - 1, len(word2) - 1)

    def minDistance(self, word1: str, word2: str) -> int:
        import numpy as np
        rows = len(word1) + 1
        cols = len(word2) + 1
        distanceMatrix = np.zeros((rows, cols), dtype=int)
        for j in range(1, cols):
            distanceMatrix[0][j] = j
        for i in range(1, rows):
            distanceMatrix[i][0] = i
        for i in range(1, rows):
            for j in range(1, cols):
                if word1[i - 1] == word2[j - 1]:
                    distanceMatrix[i][j] = distanceMatrix[i - 1][j - 1]
                else:
                    distanceMatrix[i][j] = min(1 + distanceMatrix[i - 1][j], 1 + distanceMatrix[i][j - 1],
                                               1 + distanceMatrix[i - 1][j - 1])
        return int(distanceMatrix[len(word1)][len(word2)])


print(Solution().minDistance('This is a sentence.', "I can't solve it by myself."))
