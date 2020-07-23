from typing import List
from functools import lru_cache
import numpy as np

from test_script import speedtest


class Solution:
    def findLength_recursive(self, A: List[int], B: List[int]) -> int:
        @lru_cache(maxsize=None)
        def dp(i, j, x):
            nonlocal maxAns
            if x > maxAns:
                maxAns = x
            if i < 0 or j < 0:
                return
            dp(i - 1, j - 1, x + 1 if A[i] == B[j] else 0)
            dp(i, j - 1, 0), dp(i - 1, j, 0)

        maxAns = -2 ** 31
        dp(len(A) - 1, len(B) - 1, 0)
        return maxAns

    def findLength(self, A: List[int], B: List[int]) -> int:
        dp = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]
        result = 0
        for i in range(1, len(A) + 1):
            for j in range(1, len(B) + 1):
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    result = max(result, dp[i][j])
        return result


speedtest((Solution().findLength, Solution().findLength_recursive),
          ([5, 14, 53, 80, 48, 6, 7, 8], [6, 7, 8, 50, 47, 3, 80, 83]))
array1 = np.array(range(1000))
array2 = array1
speedtest((Solution().findLength, Solution().findLength_recursive), (array1, array2))
array1[:] = 59
array2 = array1.copy()
array1[3] = 91
array2[-1] = 94
speedtest((Solution().findLength, Solution().findLength_recursive), (array1, array2))
