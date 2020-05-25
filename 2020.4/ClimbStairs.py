from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def climbStairs(self, n: int) -> int:
        if n is 1:
            return 1
        return self.climbStairs(n-1) + n - 1