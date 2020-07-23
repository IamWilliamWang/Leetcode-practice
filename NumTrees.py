from functools import lru_cache

class Solution:
    def numTrees(self, n: int) -> int:
        @lru_cache(maxsize=None)
        def counter(start: int, end: int):
            if end - start <= 1: # 只有一个数或者没有数
                return 1
            ans = 0
            for centerI in range(start, end):
                ans += counter(start, centerI) * counter(centerI + 1, end)
            return ans
        return counter(1, n + 1)