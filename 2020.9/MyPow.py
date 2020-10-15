from functools import lru_cache
from math import sqrt


class Solution:
    @lru_cache(maxsize=None)
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n > 1:
            return self.myPow(x * x, n // 2) * self.myPow(x, n - n // 2 * 2)
        else:
            n = -n
            return 1 / (self.myPow(x * x, n // 2) * self.myPow(x, n - n // 2 * 2))


print(Solution().myPow(2, -3))
